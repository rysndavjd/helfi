#!/usr/bin/env python

import subprocess
import time
import re


def exists(iface):
    iwconfig = subprocess.run(["iwconfig"], stdout = subprocess.PIPE, stderr=subprocess.DEVNULL, text = True)
    check = re.compile(iface)
    result = str(check.search(str(iwconfig.stdout)))

    if result == "None":
        return "None"
    else:
        return iface
    

def mode(iface):
    pass

def setup_auto():
    subprocess.run("clear")

    #if exists("wlan0") == "None":
    #    print("WLAN0 does not exist")
    #    if exists("wlan1") == "None":
    #        pass
    #else:
    #    print("Works")
    #    time.sleep(2) 
    
    subprocess.run("clear")


def setup_man():
    #subprocess.run("clear")
    #print("Choose a WLAN to use. ")
    #subprocess.run("iwconfig", shell=True)
    #time.sleep(1)
    #option = input("Enter your choice: ")
#
    #while option not in ["wlan0", "wlan1", "wlan2", "wlan3"]:
    #    print("Not a valid input, please try again.")
    #    time.sleep(1)
    #    subprocess.run("clear")
    #    print("Choose a WLAN")
    #    subprocess.run("iwconfig", shell=True)
    #    option = input("Enter your choice: ")
    print("net")
    time.sleep(2)
    pass
