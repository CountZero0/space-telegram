# Space Telegram

This programm downloads pictures from NASA and SPACEX and posts it in telegram.
***

## Getting started

### Prerequisites

To work with this programm you will need to install Python 3.6+
And you have to register bot in telegram and to get token to Telegram API 
[How to register bot](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html)

### Installation

In order to start, you have to clone the repository and type in terminal
```angular2html
pip install -r requirements.txt
```

### Configuration

#### Environment Variables

You need to set these 4 variables in your working system enviroment:
* TG_BOT_TOKEN: It's the Bot Token that you received from [BotFather](https://t.me/BotFather).
* TG_CHAT_ID: Channel id where pictures will be published
* POSTING_INTERVAL: Pictures' publication interval in seconds
* NASA_API_KEY: Key to access NASA API, you can get [here](https://api.nasa.gov)

## Execution

Download pictures:
```angular2html
python fetch_spacex.py
```
```angular2html
python fetch_nasa.py
```
After this step directory "images" will be automatically created and pictures will be downloaded into it.

Next step, you can run:
```angular2html
python main.py
```
And pictures will start publishing