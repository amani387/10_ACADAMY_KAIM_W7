# **Task 1 & Task 2 - Data Scraping, Cleaning, and Storage**

## **Task 1: Data Scraping**
### **Objective:**
Scrape relevant data from Telegram channels related to Ethiopian medical businesses.

### **Steps Taken:**
1. **Set Up Telegram API Access**
   - Registered a Telegram app to get `api_id` and `api_hash`.
   - Used `Pyrogram` for data extraction.

2. **Scraped Messages from Public Telegram Channels**
   - Extracted text, sender, timestamp, and channel name.
   - Saved raw data in `raw_tg_data.csv`.

3. **Extracted Images for Object Detection**
   - Downloaded media files from Telegram messages.
   - Stored images for further YOLO processing.

### **Technologies Used:**
- `Pyrogram` for Telegram scraping.
- `pandas` for data handling.
- `logging` for tracking progress.

---

## **Task 2: Data Cleaning & Transformation**
### **Objective:**
Clean and transform the scraped data for structured storage.

### **Cleaning Steps:**
1. **Removed Duplicates**
   - Dropped duplicate messages based on timestamp & text.

2. **Handled Missing Values**
   - Filled missing senders with `Unknown Sender`.
   - Replaced empty messages with `No Message`.

3. **Standardized Text Data**
   - Removed emojis and unnecessary spaces.
   - Extracted and removed links from messages.

4. **Stored Cleaned Data in PostgreSQL**
   - Created a `messages` table with structured columns.
   - Inserted cleaned data into PostgreSQL.

### **Technologies Used:**
- `pandas` for text processing.
- `psycopg2` for database integration.
- `regex` for text standardization.

---

## **How to Run the Scripts**
### **1️⃣ Run Data Scraping:**
```bash
python scripts/tg_scraper.py
```

### **2️⃣ Run Data Cleaning & Storage:**
```bash
python scripts/db_insert.py
```

### **3️⃣ Verify Data in PostgreSQL:**
```sql
SELECT * FROM messages LIMIT 10;
```

---

## **Next Steps**
✅ **Prepare YOLO for object detection on images.**  
✅ **Develop a FastAPI backend to expose the data via APIs.**

Let me know if you need any modifications! 🚀
