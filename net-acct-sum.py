#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 12:40:59 2020
@author: boris.gelfandbein

0 - unix time, utime
1 - protocol, proto
2 - source address, src_ip
3 - source port, src_p
4 - destination address, dst_ip
5 - destination port, dst_p
6 - packets count, packets
7 - bytes count, _bytes
8 - device name, dev
9 - user name - on eth always unknown, uname
"""

from config import *

import csv
import datetime
import importlib.util
import logging
import sys
from datetime import datetime

def _modules(name):
    if name in sys.modules:
        print(f"{name!r} already in sys.modules")
    # elif (spec := importlib.util.find_spec(name)) is not None:
    elif importlib.util.find_spec(name) is not None:
        spec = importlib.util.find_spec(name)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        print(f"{name!r} has been imported")
    else:
        print(f"can't find the {name!r} module")

def _testmodules(_module):
    try:
        importlib.import_module(_module)
    except ImportError as err:
        # subprocess.call([sys.executable, "-m", "pip", "install", 'termcolor'])
        print(f"Importing '{_module}' error.", err)
    else:
        print(f"Module '{_module}' testing well done.")

def select_by_src(utime, src_ip):
    if data["src_ip"] == src_ip:
        return data["src_p"]
    return 0

l = ['0000000001','1260633600', '1256993100', '1273255200', '1253450700']
def humanize(unix_time):
    time = datetime.fromtimestamp(int(unix_time)).strftime('%Y-%m-%d %H:%M')
    return time

lsorted = sorted(l, reverse=False)
print(lsorted)
print([humanize(i) for i in lsorted])

def bkmg(bytes):
    if bytes < 1000 * 1024:
        bytes = ("%.2f" % (bytes / 1024) + " Kb's")
        return bytes
    if bytes < 1000 * 1048576:
        bytes = ("%.2f" % (bytes / 1048576) + " Mb's")
        return bytes
    if bytes < 1000 * 1073741824:
        bytes = ("%.2f" % (bytes / 1073741824) + " Gb's")
        return bytes
    else:
        bytes = ("%.2f" % (bytes / 1099511627776) + " Tb's")
        return bytes

def _logs():
    logging.basicConfig(filename="./net-acct-log.log", level=logging.DEBUG)
    
def main(filename):
    ip = str(input("Enter IP to count (default 192.168.0.3): "))
    if ip == "":
        ip = "192.168.0.3"
    ipbc_in = 0
    ipbc_out = 0

    with open(filename) as f:
        input_line = csv.DictReader(f, fieldnames=["utime", "proto", "src_ip", "src_p", "dst_ip", "dst_p",
                                                   "packets", "_bytes", "dev", "uname"], delimiter="\t")
        for row in input_line:
            if row['dst_ip'] == ip:
                ipbc_in += int(row['_bytes'])
            if row['src_ip'] == ip:
                ipbc_out += int(row['_bytes'])
        _in = bkmg(ipbc_in)
        _out = bkmg(ipbc_out)

        print(f"{ip} downloaded {_in} uploaded {_out}")


if __name__ == "__main__":
    try:
        main(logfile)
    except KeyboardInterrupt:
        print("\nGot KeyboardInterrupt! Exiting...")
        sys.exit()
