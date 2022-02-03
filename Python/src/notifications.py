def colored(r, g, b, text): return "\033[38;2;{};{};{}m{}\033[m".format(r, g, b, text)

class System:
    def broadcast(message):
        broadcast = colored(0, 255, 0, "BROADCAST")
        print(f'[{broadcast}] {message}')

    def notify(message):
        notification = colored(0, 255, 255, "NOTIFICATION")
        print(f'[{notification}] {message}')

    def error(message):
        error = colored(255, 0, 0, "ERROR")
        print(f'[{error}] {message}')

    def show_message(message, address):
        print(f'[{address}] {message}')

class Client:
    def broadcast(message, connection):
        broadcast = colored(0, 255, 0, "BROADCAST")
        connection.send(f'[{broadcast}] {message}')

    def notify(message, connection):
        notification = colored(0, 255, 255, "NOTIFICATION")
        connection.send(f'[{notification}] {message}')

    def error(message, connection):
        error = colored(255, 0, 0, "ERROR")
        connection.send(f'[{error}] {message}')
        
