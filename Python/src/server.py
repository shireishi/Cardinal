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
command_prefix = "!"

#! CONNECT TO SERVER !#
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

#! FUNCTIONS !#
def decode_header(header_information):return ast.literal_eval(header_information)

def verify_message(message, message_hash):
    if hash(message) == message_hash:return True
    else:return False

def process_commands(message):
    """
    return True if command is executed completely and correctly
    return False if command failed to execute or if it failed to complete
    return null if there is no command to execute
    """
    success = True
    failed = False
    nothing = None

    if message.starts_with() == command_prefix:continue
    else:return nothing

    command = message[1:]
    
    if command == "shutdown":
        try:
            for user in ACTIVE_CONNECTIONS.keys():
                ACTIVE_CONNECTIONS[user].close()
                System.notify(f'Disconnected {user}')
        except Exception as e:
            System.error(e)
            return failed
        return success
    
    if command == "connections":
        try:
            for user in ACTIVE_CONNECTIONS:
                System.notify(user)
        except Exception as e:
            System.error(e)
            return failed
        return success

def handle_client(connection, address):
    global ACTIVE_CONNECTIONS
    connection.send(buff(CONNECTION_ESTABLISHED).encode(FORMAT))
    ACTIVE_CONNECTIONS[address] = connection

    try:
        # recieve all required data
        header_length = connection.recv(HEADER).decode(FORMAT)
        message_header = decode_header(connection.recv(header_length).decode(FORMAT))
        message = connection.recv(message_header["length"]).decode(FORMAT)
    except Exception as e:
        connection.close()
        System.error(e)
        return

    # verify the message using the provided and generated hash
    if verify_message(message, message_header["hash"]) == True:
        pass
    else:
        System.error("Did not recieve full and or correct message.")

    # if the protocol sent in the message exists within known protocols then fulfill request
    if message_header["protocol"] in protocols:
        System.show_message(message, address)

    # parse through message for commands
    execution_status = process_commands(message)

def start_server(): # starts the threading that will manage the new server connections
    server.listen() # start the server listening on port 8080
    System.notify(f'Server is listening on port {PORT}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        System.notify(f'Active connections : {threading.active_count() - 1}')

#! EXECUTIVE CALLS !#
print(WELCOME_MESSAGE)
start_server()