import telebot

from bot.command.checker_command import CheckerCommand
from bot.command.command import Command
from bot.command.start_command import StartCommand



class TelegramBot(telebot.TeleBot):
    def __init__(self, token: str):
        super().__init__(token)
        self.commands = {}

    async def on_ready(self):
        print("Hello there!")

    def register_command(self, command: Command):
        self.commands[command.execute(self)] = command


bot = TelegramBot("1632911220:AAFC7admsTyGkpO0bU1N3FW-Br0MPg09q34")

bot.register_command(StartCommand())
bot.register_command(CheckerCommand())

bot.polling(none_stop=True, interval=0, timeout=0)
