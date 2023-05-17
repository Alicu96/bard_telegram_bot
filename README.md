# bard_telegram_bot
google bart telegram bot, can have conversation in any language

## how to run the bot
```bash
# create .env file contain secret keys
nano .env
# copy these lines to .env file
TELEGRAM_BOT_TOKEN=<your telegram bot token>
_BARD_API_KEY=<value of __Secure-1PSID cookie>
```
To get the TELEGRAM_BOT_TOKEN:
1. Search for @botfather in Telegram
2. Start a conversation with BotFather by clicking on the Start button
3. Type /newbot, and follow the prompts to set up a new bot. The BotFather will give you a token that you will use to authenticate your bot and grant it access to the Telegram API

To get the _BARD_API_KEY: 
1. Visit https://bard.google.com/
2. F12 for console
3. Session: Application → Cookies → Copy the value of  `__Secure-1PSID` cookie.
For more detail, visit: https://github.com/dsdanielpark/Bard-API

- Run the bot locally
```bash
pip install -r requirements.txt
sh ./scripts/run_app.py
```

- Using Docker
```bash
# build docker image
docker build -t bard_bot . -f Dockerfile
# run
docker compose up -d
```

## License
[MIT](https://opensource.org/license/mit/) 


## Bugs and Issues


## Contacts
Core maintainer: https://github.com/Alicu96

## Reference 
[1] https://github.com/dsdanielpark/Bard-API

  
