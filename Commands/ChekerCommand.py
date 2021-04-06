import requests
from Commands.Command import Command
import json

from speedbot import bot


class ChekerCommand(Command):
    def universe(self, Message):
        path = '../data.json'
        with open(path, 'r') as f:
            dat = json.loads(f.read())
            for i in dat['urls']['url']:
                neural = (i['first'])
        r = requests.head(neural)
        if (r.status_code == 200):
            bot.send_message('its okey')
        else:
            bot.send_message('its not okay')
