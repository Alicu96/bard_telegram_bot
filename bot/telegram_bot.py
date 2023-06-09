import telebot
import dotenv
import os
from bardapi import Bard
from googletrans import Translator
from get_system_stats import get_system_stats
from get_image import get_image
translator = Translator()

dotenv.load_dotenv()

telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

bot = telebot.TeleBot(telegram_bot_token)

bard = Bard(timeout=10) # Set timeout in seconds

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Hello! I am a bot that replies to your chat.")

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "Here is a list of available commands:")
    bot.send_message(message.chat.id, "/start \n/heartbeat \n/stats \n/image <keyword>")


@bot.message_handler(commands=["heartbeat"])
def heartbeat(message):
    bot.send_message(message.chat.id, "I am still alive!")


@bot.message_handler(commands=["stats"])
def get_stats(message):
    ipv4_addr, cpu_usage, mem_usage, cpu_temperature, speed_download = get_system_stats()
    bot.send_message(message.chat.id, f"ipv4_addr: {ipv4_addr}")
    bot.send_message(message.chat.id, f"cpu_usage: {cpu_usage}% \nmemory_usage: {mem_usage}% \ncpu_temperature: {cpu_temperature} *C")
    bot.send_message(message.chat.id, "speed_download: {:.2f}Mbps".format(speed_download))


@bot.message_handler(commands=["image"])
def show_image(message):
    keyword = message.text.replace("/image ", "")
    bot.send_message(message.chat.id, f"Showing image of '{keyword}':")
    file_image = "/opt/temp/000001.jpg"
    get_image(keyword)
    photo = open(file_image, 'rb')
    bot.send_photo(message.chat.id, photo)
    os.remove(file_image)


@bot.message_handler(content_types=["text"])
def reply(message):
    query = message.text
    # translate to english
    translator_result = translator.translate(query, dest="en")
    query_en = translator_result.text
    user_lang = translator_result.src
    bot.send_message(message.chat.id, f'you are texting in {user_lang.upper()}')
    # get response from bard
    if user_lang == 'en':
    	response = bard.get_answer(query)['content']
    	bot.send_message(message.chat.id, response)
    else:
    	response = bard.get_answer(query_en)['content']
    	# translate back to user's language
    	response_user_lang = translator.translate(response, src="en", dest=user_lang).text
    	bot.send_message(message.chat.id, response_user_lang)


bot.polling()
