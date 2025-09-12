import json
from datetime import date
# from replit import db
import time

item_data = {}
db = {}
VERSION = {}

def check(num):
	if num % 2 == 0:
		return True
	else:
		return False

def write_user_data():
	with open("users.json", "w") as json_file:
		# db = json.load(json_file)
		json_file.write(json.dumps(db))

def read_data():
	global item_data
	global db
	with open("data.json") as json_file:
		item_data = json.load(json_file)
	
	VERSION = '1.' + str(len(item_data))

	with open("users.json") as json_file:
		db = json.load(json_file)


def write_user(id, towrite):
	id = str(id)
	db[id] = towrite


def update_version(id, towrite):
	id = str(id)
	db[id]['data']['version'] = VERSION


def signup(user, password):
	today = str(date.today())
	rn = str(int(time.time()))
	id = len(user) + len(password)
	if check(id):
		id = id + 15
	else:
		id = id - 15
	temp = {
	 'username': user,
	 'password': password,
	 'key': 'PLACEHOLDER_KEY',
	 'id': id,
	 'logincount': 0,
	 'version': VERSION,
	 'data': {
	  'creation_date': today,
	  'creation_time': rn,
	  'last_login': today,
	  'items': item_data,
	 }
	}
	write_user(id, temp)
	write_user_data()
	return 'success'


def migrate(id):
	id = str(id)
	user = read_data('user.json')
	items = {}
	items = read_data('data.json')
	for i in range(0, len(user[id]['data']['items'])):
		i = str(i)
		items[i] = user[id]['data']['items'][i]
	update_version(id, items)


def login(user, password):
	rn = str(int(time.time()))
	user = str(user)
	read_data()
	id = int(len(user)) + int(len(password))
	if check(id):
		id = id + 15
	else:
		id = id - 15
	id = str(id)
	print(db)
	temp = db[id]
	if temp['username'] == user and temp['password'] == password:
		if str(temp['version']) != str(VERSION):
			print('Account made in old version create new account')
			exit()
		global dev
		dev = int(temp['data']['dev'])
		item_data = temp['data']['items']
		temp['logincount'] = int(temp['logincount']) + 1
		temp['data']['last_login'] = rn
		write_user(id, temp)
		return True
	elif temp['username'] == user and temp['password'] != password:
		return False
	else:
		return False


def update(user, password):
	id = len(user) + len(password)
	if check(id):
		id = id + 15
	else:
		id = id - 15
	temp = db[str(id)]
	temp['data']['items'] = item_data
	write_user(id, temp)