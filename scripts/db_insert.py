import pandas as pd
import psycopg2
import os

# Database connection parameters
DB_NAME = "telegram_data"
DB_USER = "postgres"  # Change if you have a different username
DB_PASSWORD = "user"  # Replace with your actual password
DB_HOST = "localhost"
DB_PORT = "5432"

def connect_db():
    """Establish a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
        )
        return conn
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return None

def insert_data_from_csv(file_path):
    """
    Inserts cleaned Telegram data into the PostgreSQL database.

    :param file_path: Path to the cleaned CSV file.
    """
    df = pd.read_csv(file_path)

    # Ensure connection
    conn = connect_db()
    if conn is None:
        return

    cursor = conn.cursor()

    # Insert data
    for _, row in df.iterrows():
        try:
            cursor.execute(
                """
                INSERT INTO messages (message_sender, message_text, message_timestamp, message_channel, emoji_used, links)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (row["message_sender"], row["message_text"], row["message_timestamp"], row["message_channel"], row["emoji_used"], row["links"]),
            )
        except Exception as e:
            print(f"⚠️ Error inserting row: {e}")

    conn.commit()
    cursor.close()
    conn.close()

    print(f"✅ Data from '{file_path}' inserted into PostgreSQL successfully!")

if __name__ == "__main__":
    csv_file_path = os.path.join(os.path.dirname(__file__), "../cleaned_tg_data.csv")  # Adjust path if needed
    insert_data_from_csv(csv_file_path)
