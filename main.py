from intpl import tools
import json
import threading

config = json.load(open('config.json'))

login = config['login']
password = config['password']
recovery = config['recovery']

print(f"Loaded config! Username: {login}, Password: {password}, Recovery email: {recovery}")
amount = input("How many to generate?: ")

for amount in range(int(amount)):
    thread = threading.Thread(target=tools.create_account, args=(login, password, recovery))
    thread.start()
    #tools.create_account(login, password, recovery)
