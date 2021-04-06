#from Command import Command

#class Callback(Command):
 #   def universe(self, call):
  #      @bot.callback_query_handler(func=lambda call: True)
   #     def callback_inline(call):
    #        if call.data == 'yes':
     #           keyboard = types.InlineKeyboardMarkup()
      #          url_btn = types.InlineKeyboardButton(text="Перейди сюда", url="https://www.speedtest.net")
       #         keyboard.add(url_btn)
        #        bot.send_message(call.message.chat.id, 'Ссылка ниже', reply_markup=keyboard)
         #   elif call.data == 'no':
          #      keyboard = types.InlineKeyboardMarkup()
           #     no1_btn = types.InlineKeyboardButton(text="Узнать IP", url="https://2ip.ru")
            #    keyboard.add(no1_btn)
             #   bot.send_message(call.message.chat.id, 'Может хочешь узнать свой IP?', reply_markup=keyboard)