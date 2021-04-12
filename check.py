from bot.command.command import Command
import json
import requests


class Check(Command):
    def execute(self, call, bot):
        path = 'data.json'
        with open(path, 'r') as f:
            data = json.loads(f.read())
            for value in data:
                print(value)

    def get_name(self):
        return 'check'


Checkcer = Check()
