from intpl import tools
import json


config = json.load(open('config.json'))

login = config['login']
password = config['password']
recovery = config['recovery']

amount = input("How many to generate?: ")

for x in range(int(amount)):
    tools.create_account(login, password, recovery)
