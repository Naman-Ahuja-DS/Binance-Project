# binance_client.py

from binance import Client
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

client = Client(os.getenv('BINANCE_API_KEY'), os.getenv('BINANCE_API_SECRET'))

def get_crypto_price(symbol):
    """Fetch latest 1-minute kline from Binance"""
    try:
        klines = client.get_klines(symbol=symbol, interval=Client.KLINE_INTERVAL_1MINUTE, limit=1)
        k = klines[0]
        
        # Convert Unix timestamp (ms) to datetime object
        open_time_dt = datetime.fromtimestamp(k[0] / 1000.0)
        close_time_dt = datetime.fromtimestamp(k[6] / 1000.0)

        return {
            'symbol': symbol,
            'open_price': float(k[1]),
            'high_price': float(k[2]),
            'low_price': float(k[3]),
            'close_price': float(k[4]),
            'volume': float(k[5]),
            'open_time': open_time_dt,
            'close_time': close_time_dt
        }
    except Exception as e:
        print(f"❌ Error fetching {symbol}: {e}")
        return None