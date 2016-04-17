#!/usr/bin/env python
# Author:   Carl Fan
# Mail:     fjjupc@gmail.com
# Describe: Get client id & client secret from secrets.config file if it exists. 
#           Otherwise, get from the user-input.

fileSecrets = open('secrets.config', 'r+')

client_id = ""
client_secret = ""
	
while True:
	line = fileSecrets.readline()
	if not line:
		break;
	try:
		line.index('client_id=')
		client_id = line.lstrip('client_id=').rstrip('\n')
	except:
		pass
	try:
		line.index('client_secret')
		client_secret = line.lstrip('client_secret=').rstrip('\n')
	except:
		pass

if not client_id:
	print("Please input your client_id:")
	client_id = input();
	strWrite = 'client_id='+client_id+'\n'
	fileSecrets.write(strWrite)
if not client_secret:
	print("Please input your client_secret")
	client_secret = input();
	strWrite = 'client_secret='+client_secret+'\n'
	fileSecrets.write(strWrite)
