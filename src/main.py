#!/usr/bin/env python

#python libs
import time
import os

#local libs
import helpers.setup_wlan as setup_wlan
import helpers.net_iface as net_iface

run = True

def menu():
    os.system("clear")
    print("")
    print("[h] Help menu")
    print("[1] Setup WLAN manual")
    print("[2] Setup WLAN auto")
    print("[0] Exit")
    print("")

def start():
    menu()
    option = input("Enter your choice: ")
    
    while option not in ["h", "H", "0", "1", "2"]:
        print("Not a valid input, please try again.")
        time.sleep(1)
        menu()
        option = input("Enter your choice: ")


    while option != "999":
            if option == "h" or option == "H":
                break
            elif option == "0":
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


