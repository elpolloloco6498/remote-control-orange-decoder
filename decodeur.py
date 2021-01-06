#!/usr/bin/python3

import requests
import time
import random

ascii_title = """

______ ________  ________ _____ _____  
| ___ \  ___|  \/  |  _  |_   _|  ___| 
| |_/ / |__ | .  . | | | | | | | |__   
|    /|  __|| |\/| | | | | | | |  __|  
| |\ \| |___| |  | \ \_/ / | | | |___  
\_| \_\____/\_|  |_/\___/  \_/ \____/  
                                       
                                       
 ___________  ___   _   _ _____  _____ 
|  _  | ___ \/ _ \ | \ | |  __ \|  ___|
| | | | |_/ / /_\ \|  \| | |  \/| |__  
| | | |    /|  _  || . ` | | __ |  __| 
\ \_/ / |\ \| | | || |\  | |_\ \| |___ 
 \___/\_| \_\_| |_/\_| \_/\____/\____/ 
                                       
                                       
by ElPolloLoco6498"""

keys = ['114', '115']
ip_decodeur = "192.168.1.10"

def modulate_volume(nb_of_requests):
	for i in range(1, nb_of_requests):
		ind = random.randint(0, len(keys)-1)
		key = keys[ind]
		url = "http://"+ip_decodeur+":8080/remoteControl/cmd?operation=01&key="+key+"&mode=0"
		print("Sending http request to decoder \n")
		print(url)
		receive = requests.get(url)
		time.sleep(1)
		
def switch_on_off(time):
	url = "http://"+ip_decodeur+":8080/remoteControl/cmd?operation=01&key=116&mode=0"
	print("Sending http request to decoder \n")
	print(url)
	time.sleep(time)
	receive = requests.get(url)

def switch_channels(nb_iterations):
	for i in range(1, nb_iterations):
		channel = random.randint(513, 521)
		url = "http://"+ip_decodeur+":8080/remoteControl/cmd?operation=01&key="+str(channel)+"&mode=0"
		print("Switching channel to : " + str(channel))
		print(url)
		time.sleep(1)
		#receive = requests.get(url)
	print("\nSwitch back to main channel \n")
	url = "http://"+ip_decodeur+":8080/remoteControl/cmd?operation=01&key=519&mode=0"
	#receive = requests.get(url)

print(ascii_title)
print("========== MENU =========")
print("1. Modulate the volume of the TV")
print("2. Switch channels randomly")
print("3. Switch On / Off")
print("4. Lower volume")
print("5. Increase volume")
print("6. Change channel to selection")
		

