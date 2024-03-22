#!/usr/bin/env python

import os
import time
import helpers.net_iface as net_iface
import helpers.tools as tools

def menuSetup():
    os.system("clear")
    print("")
    print("[h] Help menu")
    print("[1] Check dependencies")
    print("[2] 802.11 auto setup")
    print("[3] 802.11 manual setup")
    print("[4] Bluetooth auto setup")
    print("[5] Bluetooth manual setup")
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
    elif option =="1":
        os.system("clear")
        if tools.check_tool("iwconfig") == False:
            print("iwconfig missing, Install wireless-tools package")
        if tools.check_tool("ifconfig") == False:
            print("ifconfig missing, Install net-tools package")
        if tools.check_tool("aircrack-ng") == False:
            print("aircrack-ng missing, Install aircrack-ng package")
        print("")
        exit(0)
    elif option == "2":
        if net_iface.exists("wlan") == False:
            print("There seems to be no WLAN interfaces available.")
            print("Exiting")
            time.sleep(1)
        else:
            pass
    elif option == "3":
        if net_iface.exists("wlan") == None:
            print(net_iface.exists("wlan"))
            print("There seems to be no WLAN interfaces available.")
            print("Exiting")
            time.sleep(1)
        else:
            os.system("clear")
            net_iface.lists()
            option = input("Enter your choice (q to quit): ")
            while option not in ["wlan0", "wlan1", "wlan2", "wlan3", "wlan4", "wlan5", "wlan6", "wlan7", "wlan8", "wlan9", "q", "0"]:
                print("Not a valid input, please try again.")
                time.sleep(1)
                os.system("clear")
                option = input("Enter your choice (q to quit): ")
            if option == "0" or option == "q":
                pass
            else:
                net_iface.set_mode("monitor", option)


    else:
        print("Error #setup.py")
        exit


