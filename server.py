from concurrent.futures import thread
from gettext import install
from http import client, server
from operator import truediv
from pydoc import cli
from telnetlib import IP
from threading import Thread
import socket
from tkinter import SE, Listbox
from xmlrpc.client import ProtocolError

SERVER= None
IP_ADDRESS= '127.0.0.1'
PORT= 8050
clients={}
BUFFER_SIZE= 4096


def acceptConnections():
    global clients
    global SERVER

    while True:
        client, addr= SERVER.accept()
        client_name= client.recv(4096).decode().lower()
        clients[client_name]={
            'client': client,
            'address': addr,
            'connected_with': '',
            'file_name':'',
            'file_size': 4096
        }
        print(f"Connection successfullt established with {client_name} : {addr}")

        # thread= Thread(target=handleClient, args= (client, client_name))
        # thread.start()

def setup():
    print('\n\t\t\t\t\t\t\tMUSIC SHARING APP \n')

    global IP_ADDRESS
    global SERVER
    global PORT

    SERVER= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(100)

    print('\n\t\t\t\tSERVER IS WAITING FOR INCoMING CONNECTIONS...')
    print('\n')

    acceptConnections()


setup_thread= Thread(target=setup)
setup_thread.start()


