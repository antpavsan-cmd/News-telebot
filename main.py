from random import choice
import telebot as tb
from telebot import types
from dotenv import load_dotenv
import os
from pythonpart import build_news
from anekdot import get_anekdot

load_dotenv(dotenv_path=".env")
token = os.getenv("TOKEN")
if not token:
	print("TOKEN not found")
	
bot=tb.TeleBot(token)

#telebot part
#start
@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,'это бот по созданию абсурдных новостей\n для получения новости напишите "новость" или нажмите на кнопку "новость"')
#buttons
	markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1=types.KeyboardButton("новость")
	markup.add(item1)
	item2=types.KeyboardButton("анекдот")
	markup.add(item2)
	bot.send_message(message.chat.id,'всё работает', reply_markup=markup)

@bot.message_handler(content_types=["text"])
def reply_news(message):
	if message.text == "новость" or message.text == "Новость":
		news = build_news()
		bot.send_message(message.chat.id,f"{news}")
def anekdot(message):
	if message.text == "анекдот" or message.text == "Анекдот":
		joke = get_anekdot()
		bot.send_message(message.chat.id,f"{joke}")
while True:
	try:
		bot.delete_webhook()
		bot.infinity_polling()
	except Exception as e:
		print(e)
