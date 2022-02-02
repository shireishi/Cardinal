import socket
import threading
import Notifications

#! GLOBAL VARIABLES !#
HEADER, PORT = 64, 8080
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

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
"""

def handle_client(connection):
    connection.send("test".encode(FORMAT))

def start_server(): # starts the threading that will manage the new server connections
    server.listen() # start the server listening on port 8080
    Notifications.System.notify(f'Server is listening on port {PORT}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.active_count() - 1}')

server_start()
