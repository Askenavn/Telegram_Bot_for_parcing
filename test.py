import requests
from bs4 import BeautifulSoup

URL = 'https://vc.ru/new/'  # URL сайта для парсинга

r = requests.get(URL)
soup = BeautifulSoup(r.content, "html.parser")
item = soup.find('div', class_='feed__item')  # находим последнюю опубликованную новость
time = item.find('time', class_='time', title=True)["title"].strip()
description = item.find('p').text.strip()
link = item.find('a', class_='content-link', href=True)["href"].strip()
title = item.find('div', class_='content-title content-title--short l-island-a').text.strip()  # находим название
item_id = item.find('div', class_='l-mb-28')
item_idid = item_id["class"]

print(title)
print(item_idid)
print(description)
print(time)
print(link)
