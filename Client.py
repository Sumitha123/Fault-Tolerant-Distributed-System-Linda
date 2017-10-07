
#!usr/bin/env python3

import socket
import sys
from threading import Thread
import os
import hashlib
import errno
from time import sleep
from Server import selfHost


n = 0
#Initializing the number of hosts added
hostNum = 0
netsFile = '/tmp/92065/linda/nets'

# Create directory with chmod 777 if it does not exist
# Create netsFile with chmod 666 if it does not exist
if not os.path.exists(netsFile):
    try:
        os.makedirs('/tmp/92065')
        os.chmod('/tmp/92065',0o777)
        os.makedirs('/tmp/92065/linda')
        os.chmod('/tmp/92065/linda',0o777)
        with open('/tmp/92065/linda/nets','wt') as netsFile:
            os.chmod('/tmp/92065/linda/nets',0o666)
            netsFile.close()
    except OSError as e:
        if e.errno != 17:
            pass

file = open('/tmp/92065/linda/nets','a')


#Initializing hash tables for Host id and socket descriptors
HOST_LIST = {}
CLIENT_SOCK_DES = {}

#Class for each host added
class hostList:
    def __init__(self):
        print("HOST ID" )
    #def __del__(self):
        #print("Host is removed")
    def hostAddr(self,addr,clientSock):
        self.addr = addr
        self.clientSock = clientSock
        global n,HOST_LIST
        for i in range(n+1):
            HOST_LIST.update({n:addr})
            CLIENT_SOCK_DES.update({n:clientSock})
            file = open('/tmp/92065/linda/nets','w')
            file.write(str(n) + ' : ' + str(addr) + '\n')
            file.close()
        n = n+1
        print(HOST_LIST)


Last login: Mon Dec 19 10:39:08 on ttys002
Sumithas-MacBook-Air:~ sumitha$ ssh -l 92065 23.253.20.67
92065@23.253.20.67's password: 
Welcome to Ubuntu 14.04.2 LTS (GNU/Linux 3.13.0-58-generic x86_64)

 * Documentation:  https://help.ubuntu.com/
New release '16.04.1 LTS' available.
Run 'do-release-upgrade' to upgrade to it.

Last login: Thu Dec 22 18:07:37 2016 from c-50-156-90-56.hsd1.ca.comcast.net
$ cd P1
$ ls
Linda.py  readme.txt  Server.py
$ vim Linda.py
$ vim Server.py
$ vim readme.txt
$ cd ..
$ cd P2
$ ls
Client.py  P2.py  __pycache__  readme.txt  Server.py
$ vim Client.py




#md5hash function to hash the output to a host
def md5hashFumction(q,*a):
    b = (str)(a)
    hash_object = hashlib.md5(b.encode())
    i = hash_object.hexdigest()
    x = (int(i,16))%q
    return x


#Function to find Local IP address
def getLocalIp():
    sock_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_fd.connect(("google.com",80))
    local_ip = sock_fd.getsockname()[0]
    port = sock_fd.getsockname()[1]
    sock_fd.close()
    return local_ip,port


#Define a function for the client thread
def clientProg(ip_,port_):
    global hostNum
    #Create a client socket
    global client_sock
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hostNum = hostNum + 1
    server_address = (ip_,port_)
    client_sock.connect(server_address)
    print("Host added : " + (str)(server_address))

    hostAdded = hostList()
    hostAdded.hostAddr((server_address),client_sock)


ip,port = selfHost()
port1 = int(port)
Thread(target = clientProg, args = (ip,port1)).start()


#Defining outHandler function to perform out operation
def outHandler(p,*a):
    global CLIENT_SOCK_DES
    CLIENT_SOCK_DES[p].send(b"out")
    clientBuff = str(a)
    sleep(0.5)
    CLIENT_SOCK_DES[p].send(clientBuff.encode())
    try:
        sleep(0.5)
        data = CLIENT_SOCK_DES[p].recv(2048)
        if p!=0:
            print(data.decode('utf-8'))
    except socket.error as e:
        err = e.args[0]
        if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
                    sleep(1)


#Defining out function
def out(*a):
    global hostNum
    q = md5hashFumction(hostNum,*a)
                                                                                                                                                                                          101,1         69%

                                                                                                                                                                                          1,1           Top
