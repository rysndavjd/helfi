#!/usr/bin/env python

import shutil

def check_tool(name):
    return shutil.which(name) is not None