import requests
from Command import Command
import json


class CheckerCommand(Command):
    def universe(self, call):
        path = 'data.json'
        with open(path, 'r') as f:
            dat = json.loads(f.read())
            for i in dat['urls']['url']:
                neural = (i['first'])
        r = requests.head(neural)
        if r.status_code == 200:
            print(1)
        #           bot.send_message('its okey')
        else:
            #          bot.send_message('its not okay')
            print(0)

    def get_name(self):
        return 'Check'
