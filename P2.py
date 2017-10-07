
#!/usr/bin/env python3

import Server
import Client
from Client import clientProg
from threading import Thread
from Client import out
from Server import rd
from Server import in_
from Server import selfHost
from Client import hostList


#Define a function to get user inputs
def getUserInput():
    x = input("Linda> ")
    try:
        y = x.split(' ')
        func = str(y[0])
        if func == 'add':
            ip_ = str(y[1])
            port_ = int(y[2])
            Thread(target = clientProg, args = (ip_,port_)).start()

    except:
        pass
    try:
        eval(x)
    except:
        pass
while 1:
    #Get user input
    getUserInput()

