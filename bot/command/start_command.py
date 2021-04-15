from telebot import types

from bot.command.command import Command


class StartCommand(Command):

    def execute(self, message, bot):
        bot.send_message(message.chat.id, 'Все команды которые есть:', 'stats: ')

    def get_name(self):
        return 'start'
