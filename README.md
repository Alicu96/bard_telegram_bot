# bard_telegram_bot
google bart telegram bot

## how to run the bot
- Run the bot locally
```bash
pip install -r requirements.txt
# create .env file contain secret keys
nano .env
# copy these lines to .env file
TELEGRAM_BOT_TOKEN=<your telegram bot token>
_BARD_API_KEY=<value of __Secure-1PSID cookie>
```
To get the TELEGRAM_BOT_TOKEN: TODO
To get the _BARD_API_KEY: 
1. Visit https://bard.google.com/
2. F12 for console
3. Session: Application → Cookies → Copy the value of  `__Secure-1PSID` cookie.
For more detail, visit: https://github.com/dsdanielpark/Bard-API
- Using Docker
TODO

## License
[MIT](https://opensource.org/license/mit/) 


## Bugs and Issues


## Contacts
Core maintainer: https://github.com/Alicu96

## Reference 
[1] https://github.com/dsdanielpark/Bard-API

  