#!/usr/bin/python3

import requests
import time
import random
from pynput import keyboard

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
fuse = 0

def modulate_volume(nb_of_requests):
	time.sleep(fuse)
	for i in range(1, nb_of_requests):
		ind = random.randint(0, len(keys)-1)
		key = keys[ind]
		url = "http://"+ip_decodeur+":8080/remoteControl/cmd?operation=01&key="+key+"&mode=0"
		print("Sending http request to decoder \n")
		print(url)
		time.sleep(2)
		receive = requests.get(url)
		print("SUCCESS !\n\n")
		
def switch_on_off():
	time.sleep(fuse)
	url = "http://"+ip_decodeur+":8080/remoteControl/cmd?operation=01&key=116&mode=0"
	print("Sending http request to decoder \n")
	print(url)
	receive = requests.get(url)
	print("SUCCESS !\n\n")

def switch_channels(nb_iterations):
	time.sleep(fuse)
	for i in range(1, nb_iterations):
		channel = random.randint(513, 521)
		url = "http://"+ip_decodeur+":8080/remoteControl/cmd?operation=01&key="+str(channel)+"&mode=0"
		print("Switching channel to : " + str(channel))
		print(url)
		time.sleep(5)
		receive = requests.get(url)
	print("\nSwitch back to main channel \n")
	url = "http://"+ip_decodeur+":8080/remoteControl/cmd?operation=01&key=515&mode=0"
	receive = requests.get(url)
	print("SUCCESS !\n\n")
	
#menu
def print_menu(with_logo=True):
	if with_logo:
		print(ascii_title)
	print("\n========== MENU =========")
	print("1. Modulate the volume of the TV")
	print("2. Switch channels randomly")
	print("3. Switch On / Off")
	print("To quit the program press the escape (ESC) key")
	print("=========================\n")
	print(">> Waiting for input : ")
	
#event managment
def on_press(key):
	if key == keyboard.KeyCode(char = '1'):
		print("Modulating the volume of the TV\n")
		modulate_volume(10)
		print_menu(False)
	elif key == keyboard.KeyCode(char = '2'):
		print("Switching channels randomly")
		switch_channels(10)
		print_menu(False)
	elif key == keyboard.KeyCode(char = '3'):
		print("Playing with the power button !")
		switch_on_off()
	elif key == keyboard.Key.esc:
		print("Quiting the program...")
		return False
	else:
		print("[!] Wrong command, please chose one of the followings options")

#main
fuse = int(input("Execute command in x seconds : "))
print("Your commands will be executed in " + str(fuse) + " seconds")
print_menu()

with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()

		

