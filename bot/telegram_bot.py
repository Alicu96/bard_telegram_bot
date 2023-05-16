import telebot
import dotenv
import os
import bardapi

dotenv.load_dotenv()

telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

bot = telebot.TeleBot(telegram_bot_token)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Hello! I am a bot that replies to your chat.")

@bot.message_handler(content_types=["text"])
def reply(message):
    query = message.text
    response = bardapi.core.Bard().get_answer(query)['content']
    bot.send_message(message.chat.id, response)

bot.polling()
