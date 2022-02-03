import socket
from notifications import *

#! GLOBAL VARIABLES !#
HEADER = 64
PORT = 8080
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def start_client():
    try:
        server.bind(ADDR)
    except Exception as e:System.error(e)
    message = server.recv(HEADER)
    System.notify(str(message))

start_client()