#! GENERAL IMPORTS !#
import socket

#! LOCAL IMPORTS !#
from notifications import *
from tools import *
from security import *
from cns import *
from globvals import *

#! GLOBAL VARIABLES !#
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
welcome_message = """
Welcome to the Cardinal server architecture client interface
CSACI

This server-client communication program is designed to display all of
the possible server-client communication protocols and possibilities with
multiple messaging changes.
"""

#! FUNCTIONS !#
def test_command(message):
    if message.starts_with(command_prefix):return True
    else:return False

def process_response(response):
    try:
        if int(response) == 1:pass
        if int(response) == 0:System.error("Failed to execute command on the server.")
    except:if isinstance(response, str):System.broadcast(response)

def create_header(message, protocol, message_length):
    header = {
        "protocol": protocol,
        "length": message_length,
        "hash": hash(message)
    }
    return str(header)

def start_client():
    try:server.bind(ADDR)
    except Exception as e:System.error(e)
    try:message = server.recv(HEADER)
    except Exception as e:System.error(e)

    System.notify(message.decode(FORMAT))

def send(message):
    protocol = "transfer"
    
    # Send instructions :
    """
    The first thing that is sent is the length of the length of the header
    The second thing that is sent is the actual header which contains the message content,
    a hash representing the message, and the official length of just the message

    The New Send Instructions:
    Instead the length of the message should be sent first, the message, the header length,
    then the actual header
    And if the message alone is a command then the client is to wait after the sending to recieve a
    response from the server, whether actual data or just a blank stamp.
    """

    is_command = test_command(message)

    message_length = len(message)
    header = create_header(message, protocol, message_length).encode(FORMAT)
    header_length = len(header)
    message = message.encode(FORMAT)

    server.send(buff(header_length)) # send the size of the header as a json string
    server.send(header) # send the actual header as a json string
    server.send(message_length)
    server.send(message)

    if is_command: # if the message sent is a command then wait for a response from the server
        response = server.recv(HEADER).decode(FORMAT)
        if response:process_response(response)

#! EXECUTIVE CALLS !#
start_client()
while True:send(input(":"))