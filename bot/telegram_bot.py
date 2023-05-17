import telebot
import dotenv
import os
from bardapi import Bard

dotenv.load_dotenv()

telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

bot = telebot.TeleBot(telegram_bot_token)

bard = Bard(timeout=10) # Set timeout in seconds

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Hello! I am a bot that replies to your chat.")


@bot.message_handler(commands=["heartbeat"])
def heartbeat(message):
    bot.send_message(message.chat.id, "I am still alive!")


@bot.message_handler(content_types=["text"])
def reply(message):
    query = message.text
    response = bard.get_answer(query)['content']
    bot.send_message(message.chat.id, response)


bot.polling()
