import socket
import threading
import 

#! GLOBAL VARIABLES !#
HEADER, PORT = 64, 8080

"""
Server Architecture Notes:
    The server architecture will be primarily composed of a defined header that will contain the information
    about the length of the incoming information, which can range a very large data set.

    Custom communication protocols will be made, as well as repeating data with the header toggle of a resend
    to denote whether or not all of the original information was recieved. 

    There should also be a hash check system where a hash is sent along with the information, the information
    is hashed by the same algorithm and then compared to make sure the correct data was recieved.
"""

def server_start():
    pass



server_start()
