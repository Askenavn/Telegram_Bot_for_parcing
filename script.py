import requests
from bs4 import BeautifulSoup
import csv
import telebot
import time

token = "5087065097:AAHPxP5l6FD99eObncKMpWNcPlp4RXjGMLE" # Я изучил много информации, но так и не нашел как сделать бота без токена
channel_id = "@fsdgfsdg" # логин канала куда постятся новости
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text']) #Bot

def commands(message):
    #bot.send_message(channel_id, message.text)
    if message.text == "Старт":
        #bot.send_message(channel_id, "Hello")
        back_clock = None
        while True:
            post_text = parser(back_clock)
            back_clock = post_text[1]

            if post_text[0] != None:
                bot.send_message(channel_id, post_text[0])
                time.sleep(1800)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши Старт")

#Parcing
def parser(back_clock):
    URL = 'https://vc.ru/new/' #URL сайта для парсинга

    r = requests.get(URL)
    soup = BeautifulSoup(r.content, "html.parser")
    item = soup.find('div', class_='feed__item') #находим последнюю опубликованную новость
    clock = item.find('time', class_='time', title=True)
    clock = clock["title"]


    if clock != back_clock:
        link = item.find('a', class_='content-link', href=True)["href"].strip()  # находим ссылку на нее
        title = item.find('div', class_='content-title content-title--short l-island-a').text.strip()  # находим название
        description = item.find('p').text.strip()

        return f"{title}\n\n{description}\n\n{link}", clock
    else:
        return None, clock

bot.polling()