#! GENERAL IMPORTS !#
import socket
import threading
import sys

#! LOCAL IMPORTS !#
from notifications import *
from tools import *
from security import *
from cns import protocols

#! LOCAL IMPORTS !#
sys.path.append('../')

#! GLOBAL VARIABLES !#
HEADER, PORT = 64, 8080
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
CONNECTION_ESTABLISHED = "Server connection established."
WELCOME_MESSAGE = """
Hello, and welcome to the Cardinal server system.
This server architecture is composed primarily of raw data transfers and is designed for local network communication within a demilitarized zone (DMZ).
There are virtually no security protocols established.

If you wish to add custom security protocols through a fork or use any code listed here, please credit this repository.
Thank you
Keys
"""
ACTIVE_CONNECTIONS = {}

#! CONNECT TO SERVER !#
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(connection, address):
    global ACTIVE_CONNECTIONS
    connection.send(buff(CONNECTION_ESTABLISHED).encode(FORMAT))
    ACTIVE_CONNECTIONS[address] = connection

    message_length = connection.recv(HEADER).decode(FORMAT)
    message = connection.recv(message_length)

    System.show_message(message, address)

def start_server(): # starts the threading that will manage the new server connections
    server.listen() # start the server listening on port 8080
    System.notify(f'Server is listening on port {PORT}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        System.notify(f'Active connections : {threading.active_count() - 1}')

print(WELCOME_MESSAGE)
start_server()
