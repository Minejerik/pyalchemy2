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
	temp = read_item_data()
	data = login.item_data
	for i in range(0, len(data)):
		if data[str(i)] == 1 or login.dev == 1:
			print('{} {}'.format(temp[str(i)]['name'], i))

	rep = input('Recipe 1 2\n')

	if rep == 'reset':
		clear()
		clear_request()

	if rep == "exit":
		exit_save()
	
	if len(rep) < 3:
		clear()
		print('Invalid recipe12!\n')
		main()
	split_rep = sorted(rep.split(' '))
	split_rep = [int(x) for x in split_rep]

	valid_items = True
	for item in split_rep:
		if data[str(item)] == 0:
			valid_items = False

	if valid_items:
		# fl = fliprep(rep)
		for i in range(0, len(data)):
			tt = sorted(temp[str(i)]['recipe'])
			if split_rep == tt:
				data[str(i)] = 1
				login.update(user, pas)
				clear()
				print(temp[str(i)]['name'] + ' unlocked\n')
	else:
		clear()
		print('Invalid recipe!\n')
	main()


def start():
	temp = input('[1] Login [2] Sign up\n')
	read_item_data()
	clear()
	if temp == '1':
		global user
		global pas
		user = input('Username?\n')
		pas = input('Password?\n')
		temp = login.login(user, pas)
		if temp == True:
			main()
		elif temp == False:
			print('Wrong Password')
	elif temp == '2':
		login.signup(input('Username?\n'), input('Password?\n'))
		clear()
		start()

start()