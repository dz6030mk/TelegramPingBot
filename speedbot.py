import telebot

from Commands import Command
from site_cheker import SiteChecker

bot = telebot.TeleBot("1632911220:AAFC7admsTyGkpO0bU1N3FW-Br0MPg09q34")


class TelegramBot(bot):
    def __init__(self):
        super().__init__()
        self.commands = {}

    async def on_ready(self):
        print("Hello there!")

    def register_command(self, command: Command):
        self.commands[command.universe(self)] = command


bot = TelegramBot()

bot.register_command(SiteChecker)

bot.polling(none_stop=True, interval=0, timeout=0)
