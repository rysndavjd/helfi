#!/usr/bin/env python

import os
import time
import helpers.net_iface as net_iface


def menuSetup():
    os.system("clear")
    print("")
    print("[h] Help menu")
    print("[1] 802.11 auto setup")
    print("[2] 802.11 manual setup")
    print("[3] Bluetooth auto setup")
    print("[4] Bluetooth manual setup")
    print("[0] Exit")
    print("")

def setup():
    menuSetup()
    option = input("Enter your choice: ")
    
    while option not in ["h", "H", "q", "Q", "0", "1", "2", "3", "4"]:
        print("Not a valid input, please try again.")
        time.sleep(1)
        menuSetup()
        option = input("Enter your choice: ")

    if option == "h" or option == "H":
        pass
    elif option == "0" or option == "q" or option == "Q":
        pass
    elif option == "1":
        if net_iface.exists("wlan") == "None":
            print("There seems to be no WLAN interfaces available.")
            print("Exiting")
            time.sleep(1)
        else:
            pass
    elif option == "2":
        if net_iface.exists("wlan") == "None":
            print("There seems to be no WLAN interfaces available.")
            print("Exiting")
            time.sleep(1)
        os.system("clear")
        net_iface.lists()
        option = input("Enter your choice: ")
        while option not in ["wlan0", "wlan1", "wlan2", "wlan3", "wlan4", "wlan5", "wlan6", "wlan7", "wlan8", "wlan9"]:
            print("Not a valid input, please try again.")
            time.sleep(1)
            option = input("Enter your choice: ")

        net_iface.set_mode("monitor", option)


    else:
        print("Error #setup.py")
        exit


