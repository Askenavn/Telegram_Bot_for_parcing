import requests
from bs4 import BeautifulSoup
import csv
import telebot
import time

token = "" # token of your bot
channel_id = "" # login of channel for posting
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text']) #Bot

def commands(message):
    
    if message.text == "Старт":
        
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
    URL = 'https://vc.ru/new/' #URL of site for parcing

    r = requests.get(URL)
    soup = BeautifulSoup(r.content, "html.parser")
    item = soup.find('div', class_='feed__item') 
    clock = item.find('time', class_='time', title=True)
    clock = clock["title"]


    if clock != back_clock:
        link = item.find('a', class_='content-link', href=True)["href"].strip()
        title = item.find('div', class_='content-title content-title--short l-island-a').text.strip()
        description = item.find('p').text.strip()

        return f"{title}\n\n{description}\n\n{link}", clock
    else:
        return None, clock

bot.polling()
