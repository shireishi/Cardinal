#! GENERAL IMPORTS !#
import socket
import threading
import sys

#! LOCAL IMPORTS !#
from notifications import *
from tools import *
from security import *

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

#! CONNECT TO SERVER !#
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

"""
Server Architecture Notes:
    The server architecture will be primarily composed of a defined header that will contain the information
    about the length of the incoming information, which can range a very large data set.

    Custom communication protocols will be made, as well as repeating data with the header toggle of a resend
    to denote whether or not all of the original information was recieved. 

    There should also be a hash check system where a hash is sent along with the information, the information
    is hashed by the same algorithm and then compared to make sure the correct data was recieved.

Header Format:
    [key(32int)][len of message[1byte binary]][len 24 hash of data]
    Example:
    10000000000000000000000000000000 00001010 1232106153434310227543472
    Obiviously remove the spaces but you get the idea
    The total length of the above string is 64 and would be transmitted before the actual data. The binary value providing the length of the message is read second
    After the type of communication is read from the key, and then the hash is read after the recieving to confirm that the data recieved and the data sent is the same.

    The sha256 hashing algorithm will be used simply because of its modern-esque usage.

Cardinal Naming System CNS:
    This will be a localized database which will manage the pseudonyms of different keys for the server-side architecture. For example, the client does not need the exact
    key for a transmission, but could instead can send "transmission" as a string and the CNS will return to the server the key for a transmission key.
"""

def handle_client(connection, address):
    connection.send(buff(CONNECTION_ESTABLISHED))

    

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
