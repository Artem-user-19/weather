import telebot
import requests
import math
import json

bot = telebot.TeleBot("6520587473:AAFOgdlRfi0Hpkh4NNri9DdMWGDTSAEXdZc")
API = "30e3962919f1d3a18d3939d8b88969b3"

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Де ти живеш?")

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "Цей бот показує погоду у різних регіонах, просто вказуючи місто чи ПМТ. Напиши '/start' або перейди в 'menu' та натисни '/start' там")

@bot.message_handler(content_types=["text"])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric")
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Зараз погода: {math.ceil(temp)} °C')
    else:
        bot.reply_to(message, "Місто вказане невірно")


bot.polling(none_stop=True)