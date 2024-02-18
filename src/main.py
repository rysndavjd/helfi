#!/usr/bin/env python

#python libs
import time
import os
import signal

#local libs
import helpers.setup

run = True

def menu():
    os.system("clear")
    print("")
    print("[h] Help menu")
    print("[1] Setup")
    print("[2] 802.11 (WIFI) attacks")
    print("[3] Bluetooth attacks")
    
    print("[0] Exit")
    print("")

def start():
    menu()
    option = input("Enter your choice: ")
    
    while option not in ["h", "H", "q", "Q", "0", "1", "2", "3", "4"]:
        print("Not a valid input, please try again.")
        time.sleep(1)
        menu()
        option = input("Enter your choice: ")


    while run:
            if option == "h" or option == "H":
                break
            elif option == "0" or option == "q" or option == "Q":
                exit(0)
            elif option == "1":
                helpers.setup.setup()
                start()
            elif option == "2":
                pass
            else:
                print("Error #main.py")
                break

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    exit(0)

if os.geteuid() == 0:
    signal.signal(signal.SIGINT, signal_handler)
    start()
    
else:
    print("Please run as root.")
