import telebot
import datetime as dt
import requests
from log import *

bot = telebot.TeleBot("TOKEN")

print('Start')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    log(m)
    bot.send_message(m.chat.id, 'Я - чат-бот версии 1.0. \nКоманды: \nпривет (приветствие), \nпогода (за бортом), \nсколько (до Нового года)')

@bot.message_handler(content_types=["text"])
def hello_user(message):
    log(message)
    if 'привет' in message.text:
        bot.reply_to(message, 'привет, ' + message.from_user.first_name)
    elif message.text == 'погода':
        r = requests.get('https://wttr.in/?0T') ## покажет прогноз погоды
        bot.reply_to(message, r.text)
    elif message.text == 'сколько':
        current_date = dt.datetime.now()
        new_year = dt.datetime(current_date.year +1,1,1)
        res = (new_year - current_date).days
        bot.reply_to(message, f'До нового года осталось {res} дней.')
        bot.send_photo(message.chat.id, 'https://melkovskiisvet.ru/media/catalog/products/4690389139390_1.jpg')

bot.infinity_polling()
