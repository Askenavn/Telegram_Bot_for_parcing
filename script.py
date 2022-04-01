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
        back_item_id = None
        while True:
            post_text = parser(back_item_id)
            back_item_id = post_text[1]

            if post_text[0] != None:
                bot.send_message(channel_id, post_text[0])
                time.sleep(120)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши Старт")

#Parcing
def parser(back_item_id):
    URL = 'https://vc.ru/new/' #URL сайта для парсинга

    r = requests.get(URL)
    soup = BeautifulSoup(r.content, "html.parser")
    item = soup.find('div', class_='feed__item') #находим последнюю опубликованную новость
    item_id = item.find('div', class_='l-mb-28')
    item_id = item_id["class"]


    if item_id != back_item_id:
        link = item.find('a', class_='content-link', href=True)["href"].strip()  # находим ссылку на нее
        title = item.find('div', class_='content-title content-title--short l-island-a').text.strip()  # находим название
        description = item.find('p').text.strip()

        return f"{title}\n\n{description}\n\n{link}", item_id
    else:
        return None, item_id

bot.polling()
