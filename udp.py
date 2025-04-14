import socket
import tkinter as tk

import asyncio

import globe.essentials
import globe.debug as debug
from globe.debug import printDebug

BUFFER_SIZE = 1024
CLIENT_PORT = 7500
SERVER_PORT = 7501

UDPClient = None

def udp_send(message:str, addr:tuple=None) -> None:
    global UDPClient
    srvrAddrPort = (globe.essentials.ip_addr, CLIENT_PORT) if (addr == None) else addr
    UDPClient.sendto(str.encode(str(message)), srvrAddrPort)
    printDebug("Sent message {} to server with address {}:{}".format(str(message), globe.essentials.ip_addr, SERVER_PORT), debug.UDP)

def udp_receive() -> str:
    global UDPClient
    UDPClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDPClient.setblocking(False)
    loop = asyncio.get_event_loop()
    try:
        data, addr = UDPClient.recvfrom(BUFFER_SIZE)
        message = data.decode('utf-8')
        printDebug("Received {} from {}".format(message, addr), debug.UDP)
        return message
    except Exception as e:
        printDebug("Error receiving UDP message: {}".format(e), debug.UDP)
        return ""

def establish_client() -> None:
    global UDPClient
    if (not globe.essentials.ip_addr):
        globe.essentials.ip_addr = globe.essentials.DEFAULT_IP
    printDebug("Establishing Client", debug.UDP)
    UDPClient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    return







## cy - local test app
if __name__ == "__main__":
    ## Setup
    import sys
    from tkinter import *

    import view

    debug.flag = debug.flag | (debug.DEBUG if "debug" in sys.argv else 0)
    debug.flag = debug.flag | (debug.UDP if "udp" in sys.argv else 0)
    printDebug("Debug mode activated")


    ## tkinter code to create Settings panel
    root = Tk()
    view.add_settings(root)

    

    establish_client()

    ## cy - test client/server case
    if ("server" in sys.argv):
        print("UDP test server")

        UDPServer = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

        UDPServer.bind((globe.essentials.ip_addr, SERVER_PORT))

        print("UDP server up and listening")
        while(True):

            bytesAddressPair = UDPServer.recvfrom(BUFFER_SIZE)
            message = bytesAddressPair[0]
            address = bytesAddressPair[1]
            clientMsg = "Message from Client:{}".format(message)
            clientIP  = "Client IP Address:{}".format(address)
            print(clientMsg)
            printDebug(clientIP)

            # Sending a reply to client
            udp_send(str(message), address)
            root.update()
    else:
        print("UDP test client\n - Add \"server\" to argv to enable server mode.\n - input \'quit\' to exit.")
        while(True):
            message = input("Enter Message >> ")
            if (message == "quit"):
                print("Exiting")
                break
            else:
                udp_send(message)
                ##print(udp_receive())
                
            root.update()