# db_connector.py

import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    server = os.getenv('DB_SERVER')
    database = os.getenv('DB_NAME')
    
    # Connection string using Windows Authentication
    conn_str = (
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'TRUSTED_CONNECTION=yes;'
    )
    return pyodbc.connect(conn_str)

def insert_price_data(symbol, open_price, high_price, low_price, close_price, volume, open_time, close_time):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO CryptoPrices (Symbol, OpenPrice, HighPrice, LowPrice, ClosePrice, Volume, OpenTime, CloseTime)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (symbol, open_price, high_price, low_price, close_price, volume, open_time, close_time))
    conn.commit()
    conn.close()

def insert_sentiment_data(symbol, headline, sentiment, score):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO SentimentData (Symbol, Headline, Sentiment, Score)
    VALUES (?, ?, ?, ?)
    """, (symbol, headline, sentiment, score))
    conn.commit()
    conn.close()

def insert_aggregated_sentiment(symbol, avg_score, sentiment_type):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO Sentiments (Symbol, SentimentScore, SentimentType, Timestamp)
    VALUES (?, ?, ?, ?)
    """, (symbol, avg_score, sentiment_type, None))  # None → uses DEFAULT GETDATE()
    conn.commit()
    conn.close()