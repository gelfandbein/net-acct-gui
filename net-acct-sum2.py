#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 13:25:31 2020

@author: boris
"""


import csv


def select_by_src(data, src_ip):
    if data["src_ip"] == src_ip:
        return data["src_port"]
    return 0

def main(filename):
    with open(filename) as f:
        data_reader = csv.DictReader(f, fieldnames=["date","proto","src_ip","src_port","dst_ip","dst_port","packets","bytes","dev", "name"],delimiter="\t")
        data = []
        data = set(map(lambda x:x["src_ip"], data_reader))
        f.seek(0)
        
        #print(data_reader(src_ip))
        #print(data(src_ip))
        #for line in data_reader:
        #    data.append(line)
        
    #print(select_by_src(data, src_ip))
    #data = list(set(map(lambda x:x["src_ip"], data)))
    
    print(data)
            
if __name__ == "__main__":
    main("./net-acct.log")