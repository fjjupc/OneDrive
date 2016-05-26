#!/usr/bin/env python
#-*- coding:GBK -*-
# Author:   Carl Fan
# Mail:     fjjupc@gmail.com
# Describe: functions for for Onedrive test

from auth import client

def list_id_path(id):
	items = navigate(id)
	for count,item in enumerate(items):
		print(count+1, item.name)
	pass

def navigate(item_id):
    items = client.item(id=item_id).children.get()
    return items

list_id_path("root")