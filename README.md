# Binance-Project
A live data pipeline project integrating Binance API, SQL, Python, and Power BI. The project fetches real-time market data from Binance, stores it in SQL, applies sentiment analysis in Python, and visualizes insights with interactive Power BI dashboards for easier decision-making.

# CryptoSentinel

Real-time cryptocurrency price and sentiment analysis system.

## Features
- Pulls live data from Binance API
- Fetches real crypto news
- Analyzes sentiment (VADER)
- Stores in SQL Server (Windows Auth)
- Ready for Power BI dashboards

## Setup
1. `pip install -r requirements.txt`
2. Get API keys from [Binance](https://binance.com) and [NewsAPI](https://newsapi.org)
3. Fill `.env`
4. Run `python main.py`