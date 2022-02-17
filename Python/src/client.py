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
    if message.startswith(command_prefix):return True
    else:return False

def process_response(response):
    try:
        if int(response) == 1:System.debug(response)
        if int(response) == 0:System.error("Failed to execute command on the server.")
    except:System.broadcast(response) if isinstance(response, str) else System.error("Failed to display response from server")

def create_header(message, protocol, message_length):
    header = {
        "protocol": protocol,
        "length": message_length,
        "hash": hash(message)
    }
    try:return str(header)
    except:return "{}"

def start_client():
    try:
        server.connect(ADDR)
        System.broadcast("Server connection established.")
    except Exception as e:System.error(e)

def send(message):
    if message:pass
    else:return
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

    ## DEFINING DATA INFORMATION ##
    message_length = len(message)
    header = create_header(message, protocol, message_length).encode(FORMAT)
    header_length = len(header)
    message = message.encode(FORMAT)

    if debug == True:print(buff(header_length), header, message)

    ## SEND ALL OF THE NECESSARY DATA ##
    try:
        server.send(buff(header_length)) # send the size of the header as a json string
        server.send(header) # send the actual header as a json string
        server.send(message)
    except Exception as e:
        System.error(e)

    if is_command: # if the message sent is a command then wait for a response from the server
        status = server.recv(HEADER).decode(FORMAT)
        if status:process_response(status)

#! EXECUTIVE CALLS !#
start_client()
try:
    while True:send(input(":"))
except KeyboardInterrupt:System.broadcast("Closing client program.")