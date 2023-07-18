# tesla-stock-tracking
sending telegram message if TESLA stocks have changed more than 5%

## Installation
- ```cd tesla-stock-tracking```
- Create Python environment using ```mkvirtualenv tesla-stoc-tracking -p Python3```
- Unfortunately, there is no requirements.txt so you must install the packages by hand
- for packages -> ```pip install requests, dotenv```

##  Set up
- on your machine go to .env file
- Briefly you can create a .env file using ```code .env```
- ALPHAVANTAGE_API_KEY= ```your alphavantage api key```
- NEWS_API_KEY=```your news api key```

## Telegram Bot Set up
- for telegram bot set up you should take a look at this article [Using Python To Send Telegram Messages In 3 Simple Steps](https://medium.com/codex/using-python-to-send-telegram-messages-in-3-simple-steps-419a8b5e5e2)
- after done this steps on the article 
- go to your .env file
- TOKEN=```your token```
- CHAT_ID=```your chat id```

- python main.py
