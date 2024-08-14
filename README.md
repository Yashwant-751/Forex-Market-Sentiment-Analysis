Forex Market Sentiment Analysis
This project performs sentiment analysis on live news headlines and combines it with economic data to provide trading recommendations for the top 5 forex pairs: EUR/USD, GBP/USD, USD/JPY, AUD/USD, and USD/CHF. The analysis helps traders gauge the market sentiment and make informed trading decisions.

Features
Real-time News Sentiment Analysis: Scrapes news headlines from financial news websites and performs sentiment analysis using Natural Language Processing (NLP).
Forex Data Retrieval: Fetches real-time forex data using the Alpha Vantage API.
Trading Recommendations: Combines sentiment analysis with recent forex data to provide a recommendation (Bullish/Bearish) for each forex pair.
Sentiment Visualization: Visualizes the sentiment distribution for each forex pair.

Table of Contents
Installation
Usage
Project Structure
Examples
License
Installation
Clone the Repository:


git clone https://github.com/your-username/forex-market-sentiment-analysis.git
cd forex-market-sentiment-analysis
Install Required Libraries:
Make sure you have Python installed. Then, install the necessary Python libraries:


pip install requests beautifulsoup4 textblob pandas matplotlib seaborn
Get an Alpha Vantage API Key:
Sign up at Alpha Vantage to get your free API key.

Add Your API Key:
Replace 'your_alpha_vantage_api_key' in the script with your actual Alpha Vantage API key.

Usage
Run the Script:
Execute the Python script to perform sentiment analysis and get recommendations:


python Forex_analysis_reccom.py
View Output:
The script will output the sentiment score, recent close price, and recommendation (Bullish/Bearish) for each forex pair. Additionally, it will display a sentiment distribution plot for each pair.

Project Structure
Forex_analysis_reccom.py: The main script that performs the sentiment analysis and data retrieval.
README.md: This README file providing an overview of the project.
Examples
After running the script, you will see outputs similar to the following:


EUR/USD Sentiment: 0.15, Recent Close: 1.1234, Recommendation: Bullish
GBP/USD Sentiment: -0.05, Recent Close: 1.2345, Recommendation: Bearish
...
Each currency pair's sentiment distribution will also be displayed as a histogram plot.

License
This project is licensed under the MIT License. See the LICENSE file for details.
