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
	write_user_data()


def update_version(id, towrite):
	id = str(id)
	db[id]['data']['version'] = VERSION


def signup(user):
	today = str(date.today())
	rn = str(int(time.time()))
	id = len(user)
	if check(id):
		id = id + 15
	else:
		id = id - 15
	temp = {
	 'username': user,
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


def login(user):
	global item_data
	rn = str(int(time.time()))
	user = str(user)
	read_data()

	id = int(len(user))
	if check(id):
		id = id + 15
	else:
		id = id - 15

	id = str(id)
	if id not in db.keys():
		signup(user)

	temp = db[id]

	if temp['username'] == user:
		item_data = temp['data']['items']
		temp['logincount'] = int(temp['logincount']) + 1
		temp['data']['last_login'] = rn
		write_user(id, temp)
		return True


def update(user):
	id = len(user)
	if check(id):
		id = id + 15
	else:
		id = id - 15
	temp = db[str(id)]
	temp['data']['items'] = item_data
	write_user(id, temp)