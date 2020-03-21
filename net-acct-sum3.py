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

import sys
import csv
import importlib.util
import logging
import os

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

# def _test(name):
#     _lst = ["logging", "os", "datetime", "subprocess", "termcolor", "pprint"]
#     for i in _lst:
#         importlib.import_module(i)
#         print("Module " + i + " imported")

# # class _sum(__init__,src_ip,bytes)
# _lst = ["logging", "os", "datetime", "subprocess", "termcolor", "pprint"]
# for i in _lst:
#     _testmodules(i)
    
def select_by_src(utime, src_ip):
    if data["src_ip"] == src_ip:
        return data["src_p"]
    return 0

def bkmg(b):
    ci = input("Print summary in (k)illobytes, (m)egabytes or (g)igabytes?")
    if ci == "k":
        b = print(f"{(b / 1024)} Kb\'s")
    if ci == "m":
        b = print(f"{(b / 2048)} Mb\'s")
    if ci == "g":
        b = print(f"{(b / 4096)} Gb\'s")
    return b

    #num = int(input())
    #m_num = b * dct[ci]
    #ret = [m_num / x[1] for x in dct.items() if x[0] != ci]
    #print(ret)

def _logs():
    logging.basicConfig(filename="./net-acct.log.log", level=logging.DEBUG)
    
def main(filename):
    ip = input("Enter IP to count (default 192.168.0.1): ")
    #if ip != "192.168.0.1":
    #    ip = "192.168.0.1"
    ipbc_in = 0
    ipbc_out = 0
    print("You enter ", ip)
    with open(filename) as f:
        input_line = csv.DictReader(f, fieldnames=["utime", "proto", "src_ip", "src_p", "dst_ip", "dst_p",
                                                   "packets", "_bytes", "dev", "uname"], delimiter="\t")
        for row in input_line:
            if row['src_ip'] == ip:
                #print("Got bytes out: ", row["_bytes"])
                ipbc_out += int(row['_bytes'])
            if row['dst_ip'] == ip:
                #print("Got bytes in: ", row["_bytes"])
                ipbc_in += int(row['_bytes'])

        print(f"{ip}: out -> {ipbc_out} bytes / {ipbc_out / 1024} Kb\'s")
        print(f"{ip}: in -> {ipbc_in} bytes / {ipbc_in / 1024} Kb\'s")

        print("out: ", bkmg(ipbc_out))
        print("in: ", bkmg(ipbc_in))

        # data = []
        # data = set(map(lambda x: x["src_ip"], input_line))
        # #data = set(map(lambda x: x["_bytes"], input_line))
        # f.seek(0)
        # print(data)
        # dict = input_line

        # utime, proto, src_ip, src_p, dst_ip, dst_p, packets, bytes, dev, uname = input_line.split()
        # _dict = input_line(utime, proto, src_ip, src_p, dst_ip, dst_p, packets, _bytes, dev, uname)
        # print(dict())


if __name__ == "__main__":
    # _test()
    try:
        main("./net-acct.log")
    except KeyboardInterrupt:
        print("\nGot KeyboardInterrupt! Exiting...")
        sys.exit()

# with open("./net-acct.log") as file:
#     _main_array = [row.strip() for row in file]
#
#
# _a0 =  (_main_array[0:1])
# _a1 =  (_main_array[1:2])
# _a2 =  (_main_array[2:3])
#
# print (_a0,_a1,_a2, sep='\n')
#
# print("---------2-----------")
#
# _a0array = {}
#
# for i in _a0:
#     _a0array = [i.split("\t") for i in _a0]
#     print("array now: ", _a0array[0:1])
#
# #_aa0.
# #_ts = int("1284101485")
# #print(datetime.utcfromtimestamp(_ts).strftime('%Y-%m-%d %H:%M:%S'))
#
# print("---------3-----------")
#
# """        _dict[0] = _utime, _proto, _srcip, _srcp, _dstip, _dstp, _pcnt, _bcnt, _devname, _username """

_dict = {}
_mydict = []
#print(type(_dict))
#print(type(_mydict))

with open("./net-acct.log") as file:
    for line in file:
        _utime, _proto, _srcip, _srcp, _dstip, _dstp, _pcnt, _bcnt, _devname, _username = line.split()
        _dict = _utime, _proto, _srcip, _srcp, _dstip, _dstp, _pcnt, _bcnt, _devname, _username
        #_mydict = dict{'utime1':'_dict[0]', 'proto':'_dict[1]', 'srcip':'_dict[2]'}
        _mydict = dict(_srcip=_dict[2], _dstip=_dict[4], _bcnt=_dict[7])

#print("Unix time: ", _dict)
print()
#print(_mydict[1], _mydict[2])
print(_mydict)
# print("---------4-----------")
