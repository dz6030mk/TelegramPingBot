import requests

import json

from bot.command.command import Command


class CheckerCommand(Command):
    def execute(self, message):
        path = '../data.json'
        with open(path, 'r') as f:
            dat = json.loads(f.read())
            for i in dat['urls']['url']:
                neural = (i['first'])
        r = requests.head(neural)
        if r.status_code == 200:
            print(1)
            # bot.send_message('its okey')
        else:
            # bot.send_message('its not okay')
            print(0)


def get_name(self):
    return 'check'
