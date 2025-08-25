# news_client.py

import requests
from dotenv import load_dotenv
import os

load_dotenv()

def fetch_crypto_news(coin="Bitcoin"):
    """Fetch real crypto news from NewsAPI"""
    url = "https://newsapi.org/v2/everything"
    params = {
        'q': coin,
        'language': 'en',
        'sortBy': 'publishedAt',
        'pageSize': 10,
        'apiKey': os.getenv('NEWS_API_KEY')
    }
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        print(f"News API Error: {response.status_code} - {response.text}")
        return []

    articles = response.json().get('articles', [])
    headlines = [article['title'] for article in articles if article['title']]
    return headlines