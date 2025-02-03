{{ config(
    materialized='table'  -- Store cleaned data as a table
) }}
WITH raw_data AS (
    -- Selecting raw data from the messages table
    SELECT 
        id, 
        message_sender, 
        message_text, 
        message_timestamp, 
        message_channel, 
        emoji_used, 
        links
    FROM {{ source('public', 'messages') }}
)

SELECT * FROM raw_data;
