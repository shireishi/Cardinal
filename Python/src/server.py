#! GENERAL IMPORTS !#
import socket
import threading
import sys
import ast

#! LOCAL IMPORTS !#
from notifications import *
from tools import *
from security import *
from cns import protocols

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

def decode_header(header_information):return ast.literal_eval(header_information)

def verify_message(message, message_hash):
    if hash(message) == message_hash:return True
    else:return False

def handle_client(connection, address):
    global ACTIVE_CONNECTIONS
    connection.send(buff(CONNECTION_ESTABLISHED).encode(FORMAT))
    ACTIVE_CONNECTIONS[address] = connection

    try:
        header_length = connection.recv(HEADER).decode(FORMAT)
        message_header = decode_header(connection.recv(header_length).decode(FORMAT))
        message = connection.recv(message_header["length"]).decode(FORMAT)
    except Exception as e:
        connection.close()
        System.error(e)
        return

    if verify_message(message, message_header["hash"]) == True:
        pass
    else:
        System.error("Did not recieve full and or correct message.")

    if protocol in cns.protocols:
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
