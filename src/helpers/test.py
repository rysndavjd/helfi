#!/usr/bin/env python

import time
import net_iface


if net_iface.exists("wlan") == "None":
    print("There seems to be no WLAN interfaces available.")
    print("Exiting")
    time.sleep(1)
