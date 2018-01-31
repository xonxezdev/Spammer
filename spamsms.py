import requests
import sys,os,time
import random

no = raw_input('number phone > ')

url='http://www.sendanonymoussms.com/'
try:
	while True:
		http = requests.post(url, data={'name':no, 'country':'INDONESIA', 'ReceiverNumber':'6285655943464', 'message':'warning this is a spammer by xonxez team :) ', 'Submit':'submit'})
		content = http.content
		if 'Your message has been sent! ' in content:
			print "[+] Message has been sended "
			time.sleep(10)
		else:
			print "[-] Failed to send a message"
			time.sleep(10)
except IOError:
	print "exiting from program"
except KeyboardInterrupt:
	print "exiting from program"
	
