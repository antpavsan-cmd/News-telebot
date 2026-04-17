from random import choice
import telebot as tb
from telebot import types
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")
token = os.getenv("TOKEN")
bot=tb.TeleBot(token)
def get_news():
	first_words = ["учёные","в госдуме","депутаты","в москве","учёные из Лондона","в Питере","ркн","распиздяи"]
	second_words = ["изобрели","предложили","разработали","высчитали","нашли","придумали","заблокировали","арестовали","запустили","доказали","разьебали"]
	third_words = ["огурец","на луну","ещё одну соцсеть","новый законопроект","новое изобретение","что земля плоская","какашки","туалетный юмор","лекарство от рака","тспу","чебурашку"]
	first_word = choice(first_words)
	second_word = choice(second_words)
	third_word = choice(third_words)
	news = first_word +" "+ second_word +" "+ third_word
	return news
#telebot part
#start
@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,'это бот по созданию абсурдных новостей\n для получения новости напишите "новость" или нажмите на кнопку "новость"')
#buttons
	markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1=types.KeyboardButton("новость")
	markup.add(item1)
	bot.send_message(message.chat.id,'всё работает', reply_markup=markup)

@bot.message_handler(content_types=["text"])
def reply_news(message):
	if message.text == "новость" or message.text == "Новость":
		news = get_news()
		bot.send_message(message.chat.id,f"{news}")
bot.infinity_polling(skip_pending=True)
