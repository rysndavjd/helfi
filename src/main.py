#!/usr/bin/env python

#python libs
import time
import os

#local libs
import helpers.setup.setup_wlan as setup_wlan
import helpers.net_iface as net_iface

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


    while option != "999":
            if option == "h" or option == "H":
                break
            elif option == "0" or option == "q" or option == "Q":
                exit(0)
            elif option == "1":
                if net_iface.exists("wlan") == "None":
                    print("There seems to be no WLAN interfaces available.")
                    print("Exiting")
                    time.sleep(1)
                else:
                    setup_wlan.wlan_man()
                break
            elif option == "2":
                pass
            else:
                print("Error #1")
                break


while run == True:
    start()


