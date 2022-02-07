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
    # protonum = get_name(protocol)
    # bindata = bin(len(message)).replace('0b', '')
    # mlbin = '0'*(8-len(bindata))+bindata
    # message_hash = hash(message)[:31]
    # return str(protonum)+mlbin+message_hash
    header = {
        "protocol": protocol,
        "length": message_length,
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
    server.send(buff(message_length))
    server.send(buff(create_header(message, protocol, message_length)).encode(FORMAT))
    server.send(message.encode(FORMAT))

#! EXECUTIVE CALLS !#
start_client()
while True:
    send(input(":"))