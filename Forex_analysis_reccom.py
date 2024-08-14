import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to fetch news headlines from a financial news website
def get_news_headlines(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract headlines (adjust selector based on the website's structure)
    headlines = soup.select('h3')  # Example selector, adjust as necessary
    return [headline.text for headline in headlines]

# Function to perform sentiment analysis on the headlines
def analyze_sentiment(headlines):
    sentiment_scores = []
    
    for headline in headlines:
        analysis = TextBlob(headline)
        sentiment_scores.append(analysis.sentiment.polarity)
    
    return sentiment_scores

# Function to fetch forex data using Alpha Vantage API
def get_forex_data(from_symbol, to_symbol, api_key):
    url = f"https://www.alphavantage.co/query?function=FX_DAILY&from_symbol={from_symbol}&to_symbol={to_symbol}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    
    # Convert data to DataFrame
    df = pd.DataFrame.from_dict(data['Time Series FX (Daily)'], orient='index')
    df = df.astype(float)
    return df

# Function to analyze sentiment and economic data, and provide a recommendation
def forex_analysis(pair, news_url, from_symbol, to_symbol, api_key):
    # Fetch and analyze news sentiment
    headlines = get_news_headlines(news_url)
    sentiment_scores = analyze_sentiment(headlines)
    
    sentiment_df = pd.DataFrame({'Headline': headlines, 'Sentiment': sentiment_scores})
    average_sentiment = sentiment_df['Sentiment'].mean()

    # Fetch forex economic data
    forex_df = get_forex_data(from_symbol, to_symbol, api_key)
    recent_close = forex_df['4. close'].iloc[0]
    
    # Analyze data and make a recommendation
    if average_sentiment > 0 and recent_close > forex_df['4. close'].mean():
        recommendation = "Bullish"
    else:
        recommendation = "Bearish"
    
    print(f"{pair} Sentiment: {average_sentiment:.2f}, Recent Close: {recent_close:.2f}, Recommendation: {recommendation}")
    
    # Visualize sentiment distribution
    sns.histplot(sentiment_scores, kde=True)
    plt.title(f'{pair} News Sentiment Distribution')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Frequency')
    plt.show()

# Alpha Vantage API key (Replace with your actual API key)
API_KEY = '0VOA68UWDH4T4HA1'

# Forex pairs to analyze
forex_pairs = {
    'EUR/USD': ('https://www.reuters.com/markets/currencies', 'EUR', 'USD'),
    'GBP/USD': ('https://www.reuters.com/markets/currencies', 'GBP', 'USD'),
    'USD/JPY': ('https://www.reuters.com/markets/currencies', 'USD', 'JPY'),
    'AUD/USD': ('https://www.reuters.com/markets/currencies', 'AUD', 'USD'),
    'USD/CHF': ('https://www.reuters.com/markets/currencies', 'USD', 'CHF')
}

# Perform analysis for each forex pair
for pair, (news_url, from_symbol, to_symbol) in forex_pairs.items():
    forex_analysis(pair, news_url, from_symbol, to_symbol, API_KEY)
