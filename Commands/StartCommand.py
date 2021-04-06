from telebot import types
from speedbot import bot

from Commands.Command import Command


class StartCommand(Command):
    def types(self, message):
        keyboard = types.InlineKeyboardMarkup()
        yes_bt = types.InlineKeyboardButton(text='Да', callback_data='yes')
        no_bt = types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(yes_bt, no_bt)
        bot.send_message(message.chat.id, 'Привет, хочешь проверить скорость интернета?', reply_markup=keyboard)

    def universe(self, call):
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



