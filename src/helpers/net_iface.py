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
    
def lists():
    wlan = []
    for i in range(10):
        if exists("wlan"+str(i)) == "wlan"+str(i):
            wlan.append(exists("wlan"+str(i)))

    for n in wlan:
        print(n + " Found")
    print("")

def set_mode(mode, iface):
    if mode == "monitor":
        #subprocess.run(["airmon-ng", "check", "kill"])
        #subprocess.run(["airmon-ng", "start", iface])
        subprocess.run(["ifconfig", "-s", iface, "down"])
        subprocess.run(["iwconfig", iface, "mode", "monitor"])
        subprocess.run(["ifconfig", "-s", iface, "up"])
    elif mode == "ap":
        pass
    elif mode == "managed":
        subprocess.run(["ifconfig", "-s", iface, "down"])
        subprocess.run(["iwconfig", iface, "mode", "managed"])
        subprocess.run(["ifconfig", "-s", iface, "up"])



def check_mode(iface):
    subprocess.run([])

def setup_auto():

    #if exists("wlan0") == "None":
    #    print("WLAN0 does not exist")
    #    if exists("wlan1") == "None":
    #        pass
    #else:
    #    print("Works")
    #    time.sleep(2) 
    
    subprocess.run("clear")


def setup_man(iface):
    
    print("net")
    time.sleep(2)
    pass
