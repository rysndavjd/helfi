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
