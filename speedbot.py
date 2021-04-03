import asyncio
import json
import aiohttp
import speedtest
import telebot
from telebot import types

bot = telebot.TeleBot("1632911220:AAFC7admsTyGkpO0bU1N3FW-Br0MPg09q34")


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    yes_bt = types.InlineKeyboardButton(text='Да', callback_data='yes')
    no_bt = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(yes_bt, no_bt)
    bot.send_message(message.chat.id, 'Привет, хочешь проверить скорость интернета?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'yes':
        keyboard = types.InlineKeyboardMarkup()
        url_btn = types.InlineKeyboardButton(text="Перейди сюда", url="https://www.speedtest.net")
        keyboard.add(url_btn)
        bot.send_message(call.message.chat.id, 'Ссылка ниже', reply_markup=keyboard)
    elif call.data == 'no':
        keyboard = types.InlineKeyboardMarkup()
        no1_btn = types.InlineKeyboardButton(text="Узнать IP", url="https://2ip.ru")
        keyboard.add(no1_btn)
        bot.send_message(call.message.chat.id, 'Может хочешь узнать свой IP?', reply_markup=keyboard)


@bot.message_handler(commands=['pingsites'])
async def poping(message):
    path = 'data.json'
    with open(path, 'r') as f:
        dat = json.loads(f.read())
        for i in dat['urls']['url']:
            neural = (i['first'])
    while True:
        async with aiohttp.ClientSession() as session:
            async with session.get(neural) as resp:
                if resp.status == 200:
                    print(1)
                else:
                    print(0)
        await asyncio.sleep(10)


@bot.message_handler(commands=['ping'])
def ping(message):
    bot.send_message(call.message.chat.id, 'Отправь сайт для пингования')
    r = pyping.ping('aqulasoft.com')
    if r.ret_code == 0:
        bot.send_message(call.message.chat.id, 'Success')
    else:
        bot.send_message(call.message.chat.id('Failed with {}'.format(r.ret_code)))


@bot.message_handler(commands=['speed'])
def speed(message):
    st = speedtest.Speedtest()
    option = bot.send_message(call.message.chat.id, '''
     Выбери тип проверки:   
     1 - Скорость скачивания   
     2 - Скорость загрузки   
     3 - Пинг
     4 - Все вместе 
     Твой выбор: ''')

    if option == 1:
        print(st.download())
    elif option == 2:
        print(st.upload())
    elif option == 3:
        servernames = []
        st.get_servers(servernames)
        print(st.results.ping)
    elif option == 4:
        bot.send_message(call.message.chat.id, st.download, st.upload, st.results.ping)
    else:
        bot.send_message(call.message.chat.id, 'Пожалуйста, введите цифру от 1 до 4!')


@bot.message_handler(commands=['graphics'])
def graphics(message):
    ...


bot.polling(none_stop=True, interval=0, timeout=0)
