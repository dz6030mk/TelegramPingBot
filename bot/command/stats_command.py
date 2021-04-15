from bot.command.command import Command
import requests


class Stats(Command):
    def execute(self, message, bot):
        urls = ['http://dev.api.handwriter.ru/converter/ping', 'http://dev.api.handwriter.ru/store/ping',
                'http://api.handwriter.ru/store/ping', 'http://api.handwriter.ru/converter/ping']

        for i in urls:
            r = requests.head(i)
            if r.status_code == 200:
                print(1)
                bot.send_message(message.chat.id, '' + 'Ну с этим все збс' + i)

            else:
                print(0)
                bot.send_message(message.chat.id, '' + 'А этому надо помочь' + i)


def get_name(self):
    return 'stats'
