#! GENERAL IMPORTS !#
import socket

#! LOCAL IMPORTS !#
from notifications import *
from tools import *
from security import *
from cns import *

#! GLOBAL VARIABLES !#
HEADER = 64
PORT = 8080
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
welcome_message = """
Welcome to the Cardinal server architecture client interface
CSACI

This server-client communication program is designed to display all of
the possible server-client communication protocols and possibilities with
multiple messaging changes.
"""

#! FUNCTIONS !#
def create_header(message, protocol, message_length):
    header = {
        "protocol": protocol,
        "length": message_length,
        "message": message,
        "hash": hash(message)
    }
    return str(header)

def start_client():
    try:
        server.bind(ADDR)
    except Exception as e:System.error(e)
    try:
        message = server.recv(HEADER)
    except Exception as e:System.error(e)
    System.notify(message.decode(FORMAT))

def send(message):
    protocol = "transfer"
    
    
    message_length = len(message)
    header = create_header(message, protocol, message_length).encode(FORMAT)
    header_length = len(header)

    server.send(buff(header_length)) # send the size of the header as a json string
    server.send(header) # send the actual header as a json string

#! EXECUTIVE CALLS !#
start_client()
while True:
    send(input(":"))