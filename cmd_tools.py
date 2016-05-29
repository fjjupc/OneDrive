#!/usr/bin/env python
#-*- coding:GBK -*-
# Author:   Carl Fan
# Mail:     fjjupc@gmail.com
# Describe: functions for for Onedrive test

from auth import client

N_LIST_DEPTH = 0

def list_id_path(id):
	items = navigate(id)
	for count,item in enumerate(items):
		print(count+1, item.name)
	pass

def navigate(item_id):
    items = client.item(id=item_id).children.get()
    return items

def list_all(id):
	global N_LIST_DEPTH
	items = navigate(id)
	N_LIST_DEPTH += 1
	for count,item in enumerate(items):
		print("|-"+(N_LIST_DEPTH-1)*"--"+item.name)
		list_all(item.id)
	N_LIST_DEPTH -= 1

N_LIST_DEPTH = 0
list_all("root")

