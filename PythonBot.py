import telebot
import schedule
import time
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('TOKEN')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет, меня зовут Бот Результатор и я буду говорить пришли результаты олимпиады Ломоносов или нет	 =)")
	message1 = "Чтобы узнать пришли ли резы -- отправь /result"
	message2 = "Автор данного tg bota @nikitass228 \nАдмин паблика https://vk.com/nikitasbotaet"
	bot.send_message(message.chat.id, message1)
	bot.send_message(message.chat.id, message2)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	url = "https://olymp.msu.ru/rus/event/5835/page/1614"
	flag = False
	page = requests.get(url).text

	soup = BeautifulSoup(page, features="html.parser")
	h2s = soup.find_all('h2')
	for h2 in h2s:
		if h2.text == "Заключительный этап":
			flag = True

	if flag:
		text1 = "Результаты пришли!!!"
	else:
		text1 = "Результатов пока нет!!!"


	bot.reply_to(message, text1)

# @bot.message_handler(commands=['result'])
# def start(message):
    # bot.send_message(message)

bot.polling()

