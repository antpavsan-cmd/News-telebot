from random import choice
import telebot as tb
from telebot import types
from dotenv import load_dotenv
import os
from pythonpart import build_news
from anekdot import get_anekdot
import json

load_dotenv(dotenv_path=".env")
token = os.getenv("TOKEN")
if not token:
	print("TOKEN not found")
	
bot=tb.TeleBot(token)

with open("citaty.json","r",encoding="utf-8") as f:
	citaty=json.load(f)

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
	item3=types.KeyboardButton("цитата")
	markup.add(item3)
	bot.send_message(message.chat.id,'всё работает', reply_markup=markup)

@bot.message_handler(content_types=["text"])
def reply_news(message):
	if message.text == "новость" or message.text == "Новость":
		news = build_news()
		bot.send_message(message.chat.id,f"{news}")
	elif message.text == "анекдот" or message.text == "Анекдот":
		joke = get_anekdot()
		bot.send_message(message.chat.id,f"{joke}")
	elif message.text == "цитата" or message.text == "Цитата":
		citata = choice(citaty)
		bot.send_message(message.chat.id,f"{citata}")
@bot.inline_handler(lambda query: True)
def inline_anek(query):
	anek = get_anekdot()
	news = build_news()
	citata = choice(citaty)
	result1 = types.InlineQueryResultArticle(id="1",title = "новость",description=news[:50], input_message_content = types.InputTextMessageContent(news))
	result2 = types.InlineQueryResultArticle(id="2",title = "анекдот",description=anek[:50], input_message_content = types.InputTextMessageContent(anek))
	result3 = types.InlineQueryResultArticle(id="3",title = "цитата",description=citata[:50], input_message_content = types.InputTextMessageContent(citata))
	bot.answer_inline_query(query.id,[result1,result2,result3],cache_time=1)

bot.delete_webhook()
bot.infinity_polling()