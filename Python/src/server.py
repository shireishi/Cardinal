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
from globvals import *

#! GLOBAL VARIABLES !#
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
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

#! CONNECT TO SERVER !#
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

#! Command Class !#
class Commands:
    def command_test(message):return True if message.startswith(command_prefix) else False

    def process_commands(message, connection):
        """
        return True if command is executed completely and correctly
        return False if command failed to execute or if it failed to complete
        return None if there is no command to execute

        Existing commands:
        shutdown    - disconnects all connected clients and closes the server program
        connections - displays all of the active connections to the server
        broadcast   - sends the following message to all of the connected clients
        """
        success = True
        failed = False
        nothing = None

        if message[0] == (command_prefix):
            if debug==True:System.debug("Message is command")
        else:return nothing

        split_message = message[1:].split()
        command = split_message[0]
        comargs = ' '.join(split_message[1:])

        if command == "shutdown":
            try:
                for user in ACTIVE_CONNECTIONS.keys():
                    ACTIVE_CONNECTIONS[user].close()
                    System.notify(f'Disconnected {user}')
                    System.notify("Shutting down")
                    quit()
            except Exception as e:
                System.error(e)
            return success
        
        if command == "connections":
            try:
                for user in ACTIVE_CONNECTIONS.keys():
                    System.notify(user)
            except Exception as e:
                System.error(e)
            return success

        if command == "broadcast":
            for user in ACTIVE_CONNECTIONS.keys():
                ACTIVE_CONNECTIONS[user].send(buff(str(len(comargs))))
                ACTIVE_CONNECTIONS[user].send(comargs.encode(FORMAT))

        if command == "disconnect":
            connection.close()
            System.notify("User disconnected.")
            return success

        return failed

#! Server Class !#
class Server:
    def decode_header(header_information):return ast.literal_eval(header_information)

    def verify_message(message, message_hash):
        if hash(message) == message_hash:return True
        else:return False

    def handle_client(connection, address):
        global ACTIVE_CONNECTIONS
        ACTIVE_CONNECTIONS[address] = connection

        connected = True
        while connected:
            try:# recieve all required data
                header_length = int(connection.recv(HEADER).decode(FORMAT))
                header = connection.recv(int(header_length)).decode(FORMAT)

                header = ast.literal_eval(header)

                message = connection.recv(int(header["length"])).decode(FORMAT)

                if debug==True:System.debug(header_length, header, message)
            except Exception as e:
                connection.close()
                System.error(e)

            # verify the message using the provided and generated hash
            if Server.verify_message(message, header["hash"]) == True:pass
            else:System.error("Did not recieve full and or correct message.")

            # if the protocol sent in the message exists within known protocols then fulfill request
            if header["protocol"] in protocols:System.show_message(message, address)

            # parse through message for commands
            execution_status = Commands.process_commands(message, connection)
            is_command = Commands.command_test(str(message))
            if debug == True:
                System.debug(execution_status)
                System.debug(is_command)
            # send a true or false value depending on the execution status of the command
            if is_command == True:connection.send(buff(1 if execution_status else 0))

    def start_server(): # starts the threading that will manage the new server connections
        server.listen() # start the server listening on port 8080
        System.notify(f'Server is listening on port {PORT}')
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=Server.handle_client, args=(conn, addr))
            thread.start()
            System.notify(f'Active connections : {threading.active_count() - 1}')
            System.notify(f'{addr[0]} connected to the server')

#! EXECUTIVE CALLS !#
print(WELCOME_MESSAGE)
Server.start_server()