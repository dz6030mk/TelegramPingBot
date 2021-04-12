

from telebot import AsyncTeleBot
from telebot.types import Message

from bot.command.checker_command import CheckerCommand
from bot.command.command import Command
from bot.command.start_command import StartCommand
prefix = '/'

class TelegramBot(AsyncTeleBot):
    def __init__(self, token: str):
        super().__init__(token)
        self.commands = {}

    async def on_ready(self):
        print("Hello there!")

    #  async def on_message(self, message):
    # text = message.split()[0]
    # if text not in self.commands:
    #     return
    #  await self.commands[text].execute(message)

    def register_command(self, command: Command):
        self.commands[command.get_name()] = command


bot = TelegramBot("1632911220:AAFC7admsTyGkpO0bU1N3FW-Br0MPg09q34")

bot.register_command(StartCommand())
bot.register_command(CheckerCommand())


@bot.message_handler(func=lambda m: True)
def on_message(message: Message):
    tex = message.text
    tex = tex[len(prefix):]
    content = tex.split()
    cmd = content[0]
    if cmd not in bot.commands:
        return

    bot.commands[cmd].execute(message, bot)


bot.polling(none_stop=True, interval=0, timeout=0)




