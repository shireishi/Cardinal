import sys

prompt = """
Hello! Welcome to the Cardinal Server Architecture.
If you wish to use the server-client communication as a chat application then input `client` and `server`
respectively within seperate terminals.

If you would rather learn about the server architecture before use; whether for file transfer, chat application, and or underlying network communication, then please
input `help` below.

- keys
"""

help_menu = """
Help menu
The Carinal Server Architecture (CSA) is a system designed to transfer data with as little traffic as possible while keeping security standards
and data integrity. There are multiple architectures written in the languages Rust, C, C++, and Python. All of which can be manipulated using any of the clients.

The portability of the server architecture is a goal of mine and will hopefully be shared by any and all future collaborators.
The server architecture will also soon be extended to a dynamically linked library to allow multiple applications to call it without the worry about multi-threading code acting faulty.
Instead, the managing of ownership and library calls will be your own operating system.
"""

print(prompt)
choice = input("> ").lower()

sys.path.append("./Python/src/")

if choice == "server":import server
if choice == "client":import client
if choice == "help":print(help_menu)