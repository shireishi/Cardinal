import socket
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

def create_header(message, protocol):
    pass

def start_client():
    try:
        server.bind(ADDR)
    except Exception as e:System.error(e)
    try:
        message = server.recv(HEADER)
    except Exception as e:System.error(e)
    System.notify(message.decode(FORMAT)))

def send(message):
    message_length = len(message)
    server.send(buff(message_length).encode(FORMAT))
    server.send(message.encode(FORMAT))

start_client()
while True:
    send(input(":"))