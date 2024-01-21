#!/usr/bin/env python

import time
import subprocess
import re 
import helpers.net_iface as net_iface


#def menu():
#    os.system("clear")
#    print("")
#    print("[1] Choose WLAN")
#    print("[2] Check WLAN mode")
#    print("[0] Return")
#    print("")


def wlan_man():
    #menu()
    subprocess.run("ifconfig")
    print("Choose a interface to setup. (0 to exit menu)")
    option = input("Enter your choice: ")

    while option not in ["0", "wlan0", "wlan1"]:
        print("Not a valid input, please try again.")
        #menu()
        option = input("Enter your choice: ")

    if option == "0":
        print("Exiting")
    elif option == "wlan0":
        net_iface.setup_man()

        time.sleep(2)
    elif option == "2":
        print("option 2")
        time.sleep(2)

def wlan_auto():
    pass

    
