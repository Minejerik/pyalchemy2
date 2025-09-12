import os
import json
import login

from os import system, name

filename = 'items.json'

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

def read_item_data():
	with open(filename) as json_file:
		data = json.load(json_file)
	return data

rep_data = read_item_data()

def exit_save():
	login.write_user_data()
	exit()

def clear_request():
	temp = input('Do you want to clear your progress?\n')
	if temp == 'y':
		print('clearing!')
		for i in range(1, len(login.item_data) + 1):
			login.item_data[str(i)] = 0
		login.item_data['1'] = 1
		login.item_data['2'] = 1
		login.item_data['3'] = 1
		login.item_data['4'] = 1
		if login.dev == 1:
			login.item_data['0'] = 1
		login.update(user, pas)
	else:
		clear()
		print('stopping!')
		main()


def main():
	data = login.item_data
	for i in range(0, len(data)):
		if data[str(i)] == 1:
			try:
				print('{} {}'.format(rep_data[str(i)]['name'], i))
			except:
				data[str(i)] = 0

	rep = input('\nRecipe 1 2\n')

	if rep == 'reset':
		clear()
		clear_request()

	if rep == "exit":
		exit_save()
	
	if len(rep) < 3:
		clear()
		print('invalid recipe!\n')
		main()
	split_rep = sorted(rep.split(' '))
	split_rep = [int(x) for x in split_rep]

	valid_items = True
	for item in split_rep:
		if data[str(item)] == 0:
			valid_items = False

	valid_recipe = False

	if valid_items:
		# fl = fliprep(rep)
		for i in range(0, len(rep_data)):
			tt = sorted(rep_data[str(i)]['recipe'])
			if split_rep == tt:
				valid_recipe = True
				data[str(i)] = 1
				login.update(user)
				clear()
				print(rep_data[str(i)]['name'] + ' unlocked\n')

	if not valid_recipe:
		clear()
		print('invalid recipe!\n')
	
	main()


def start():
	global user
	user = input('Profile name?\n')
	temp = login.login(user)
	if temp == True:
		clear()
		main()

start()