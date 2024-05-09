import random
import time, os, sys

import requests, telebot
from telebot import apihelper
from bs4 import BeautifulSoup

channel_id = "@Xanuntitle_kanal"
TOKEN_API = "6769765002:AAEaFanVNjlhL-6-lFXNApaNRugYoNwG4Is"
apihelper.ENABLE_MIDDLEWARE = True
apihelper.SESSION_TIME_TO_LIVE = 5 * 60
bot = telebot.TeleBot(TOKEN_API)
ti = random.randint(3,5)*3600
do = "r"


@bot.message_handler(commands=["start567"])
def start(message):
    global number, do
    if do == "r":
        bot.send_message(message.chat.id, "Бот запущен для того чтобы остановить повторно введите /start567")
        while True:
            with open("Number.txt", "r") as f:
                number = int(f.read())
            ti = random.randint(1,2) * 3600
            rn = random.randint(1,2)
            if rn == 1:
                try:
                    page = requests.get("https://ru.citaty.net/tsitaty/sluchainaia-tsitata/")
                    soup = BeautifulSoup(markup=page.text, features='html.parser')
                    item = soup.find("div", {"class": "mb-3"}).select("div.mb-3 a")
                    link = [it['href'] for it in item][0]
                    page_picture = requests.get("https://ru.citaty.net"+str(link)).text
                    soup_picture = BeautifulSoup(markup=page_picture, features='html.parser')
                    picture = soup_picture.find("div",class_="mt-4").select("picture source")
                    link_picture = "https://ru.citaty.net"+str([pic['srcset'] for pic in picture][0].split()[0])
                    bot.send_photo(chat_id=channel_id, photo=link_picture, caption=(str(soup.find("h1", {"class": "mb-3"}).text))+"\n\n"+str(soup.find("div", {"class": "mb-3"}).text)+"\n\n")
                except Exception:
                    pass
            if rn == 2:
                page = requests.get("https://randstuff.ru/fact/")
                soup = BeautifulSoup(markup=page.text, features="html.parser")
                bot.send_message(chat_id=channel_id, parse_mode="HTML", text=f"<b>Интересный факт</b> №{number}:"+str(soup.find(name="table", class_="text").text))
                with open("Number.txt", "w") as f:
                    f.write(str(number+1))
            do = "w"
            time.sleep(ti)
    else:
        bot.send_message(message.chat.id, "Бот остановлен для запуска /start567")
        python = sys.executable
        os.execl(python, python, *sys.argv)


bot.infinity_polling()