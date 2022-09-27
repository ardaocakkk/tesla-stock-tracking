import requests
from dotenv import load_dotenv
import os
from pathlib import Path
dotenv_path = Path('stock-news-normal-start\.env')
load_dotenv(dotenv_path=dotenv_path)
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
alphavantage_api_key = os.getenv("ALPHAVANTAGE_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

parameters_of_alphavantage = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : alphavantage_api_key
}

    ##  Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

alphavantage_response = requests.get(url="https://www.alphavantage.co/query", params=parameters_of_alphavantage)
alphavantage_data = alphavantage_response.json()

# - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
y = alphavantage_data["Time Series (Daily)"]["2022-09-16"]["4. close"]
yesterday_data = float(y)


# - Get the day before yesterday's closing stock price
d_b_y = alphavantage_data["Time Series (Daily)"]["2022-09-15"]["4. close"]
before_yesterday_data = float(d_b_y)

# - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp


difference = abs(yesterday_data - before_yesterday_data)
# - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (difference / float(before_yesterday_data)) * 100 

# - If  percentage is greater than 5 then print("Get News").
    ##  https://newsapi.org/  


if diff_percent <  5:
    parameters_of_news = {
        "q" : "tesla",
        "from" : "2022-09-16",
        "sortBy": "publishedAt",
        "apiKey" : news_api_key,
    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=parameters_of_news)
    article = news_response.json()["articles"]
#. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = article[:3]
   


 


# ---------------------------------------------------------

# ----------------------------------------------------------------

# Create a new list of the first 3 article's headline and description using list comprehension.

    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles ]

     
    # Sending messages via telegram
    for article in formatted_articles:
        TOKEN = os.getenv("TOKEN")
        chat_id = os.getenv("CHAT_ID")
        message = article
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        print(requests.get(url).json()) # this sends the message


# Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

