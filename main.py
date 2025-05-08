import requests
from config import *
from twilio.rest import Client



STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"



stock_api_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_api_key,
}
r = requests.get(STOCK_ENDPOINT,params=stock_api_params)
data = r.json()
print(data)

time_series = data["Time Series (Daily)"]
yesterday = list(time_series.keys())[0]
yesterday_closing_price = float(time_series[yesterday]["4. close"])
day_before = list(time_series.keys())[1]
day_before_closing_price = float(time_series[day_before]["4. close"])

price_difference = yesterday_closing_price - day_before_closing_price
print(price_difference)
up_down = None
if price_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

difference_percentage = round((price_difference/day_before_closing_price) * 100)
print(difference_percentage)
if abs(difference_percentage) > 1:
    news_params = {
        "apiKey": news_api_key,
        "q": COMPANY_NAME,
        "searchIn": "title",
        "language": "en",
        "sortBy": "publishedAt",
    }
    news_response = requests.get(NEWS_ENDPOINT,params=news_params)
    news_data = news_response.json()
    articles = news_data["articles"]
    three_articles = articles[:3]
    print(three_articles)
    article_list = [f"{STOCK_NAME}: {up_down}{difference_percentage}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(article_list)

    client = Client(twilio_account_sid,twilio_auth_token)
    for article in article_list:
        message = client.messages.create(
            body=article,
            from_=my_twilio_no,
            to=receivers_mobile_no
        )
