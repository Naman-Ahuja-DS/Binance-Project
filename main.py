# main.py

from binance_client import get_crypto_price
from news_client import fetch_crypto_news
from sentiment_analyzer import analyze_headline, get_sentiment_label
from db_connector import insert_price_data, insert_sentiment_data, insert_aggregated_sentiment
import time
from datetime import datetime

# List of 5 cryptos
CRYPTOS = [
    {"symbol": "BTCUSDT", "name": "Bitcoin"},
    {"symbol": "ETHUSDT", "name": "Ethereum"},
    {"symbol": "BNBUSDT", "name": "Binance Coin"},
    {"symbol": "SOLUSDT", "name": "Solana"},
    {"symbol": "ADAUSDT", "name": "Cardano"}
]

def run_pipeline():
    print(f"🚀 Starting pipeline at {datetime.now()}")
    
    for crypto in CRYPTOS:
        symbol = crypto['symbol']
        name = crypto['name']
        
        # 1. Fetch price
        try:
            data = get_crypto_price(symbol)
            insert_price_data(
                symbol=data['symbol'],
                open_price=data['open_price'],
                high_price=data['high_price'],
                low_price=data['low_price'],
                close_price=data['close_price'],
                volume=data['volume'],
                open_time=data['open_time'],
                close_time=data['close_time']
            )
            print(f"✅ {symbol} price stored")
        except Exception as e:
            print(f"❌ Error fetching {symbol} price: {e}")

        # 2. Fetch news & analyze sentiment
        try:
            headlines = fetch_crypto_news(name)
            scores = []
            for headline in headlines:
                score = analyze_headline(headline)
                sentiment = get_sentiment_label(score)
                insert_sentiment_data(symbol, headline, sentiment, score)
                scores.append(score)
            
            if scores:
                avg_score = sum(scores) / len(scores)
                sentiment_type = 'UP' if avg_score > 0 else 'DOWN' if avg_score < 0 else 'NEUTRAL'
                insert_aggregated_sentiment(symbol, avg_score, sentiment_type)
                print(f"📊 {symbol} sentiment: {len(headlines)} headlines analyzed, avg={avg_score:.3f}")
        except Exception as e:
            print(f"❌ Error processing news for {symbol}: {e}")

    print("💤 Waiting 5 minutes before next run...\n")
    time.sleep(300)  # Wait 5 minutes

# Run continuously
if __name__ == "__main__":
    while True:
        run_pipeline()