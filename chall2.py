#!/usr/bin/python3
import collections

def decode(key, data):
    newdata = ""
    data = bytearray.fromhex(data)
    #print(data)
    for i in range(len(data)):
        newkey = int(key, 16)
        tempdata = data[i]
        newdata += chr(newkey ^ tempdata)
    cursor = int(newdata[0:4], 10)
    newdata = newdata[4:]
    return newdata,cursor

def suppr_red(data, cursor):
    global tab
    for i in range(len(data)):
        tab[cursor + i] = data[i]
    return tab

with open('capture') as file:
    cpt = 0
    tab = ['*'] * 500
    for line in file.readlines():
        if cpt % 2 == 0:
            line = line[:-11]
            key = line[:2]
            data = line[2:]
            data, cursor = decode(key, data)
            suppr_red(data, cursor)
        cpt += 1
    print("".join(tab))

