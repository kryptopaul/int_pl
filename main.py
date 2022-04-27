from intpl import tools
import json

config_json = open('config.json')
config = json.load(config_json)

login = config['login']
password = config['password']
recovery = config['recovery']


for x in range(5):
    tools.create_account(login, password, recovery)