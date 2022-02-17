from tools import colored

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
        raise Exception(message)

    def debug(*message):
        debug = colored(255, 255, 0, "DEBUG")
        print('[{}] {}'.format(debug, ' '.join(x for x in message)))

    def show_message(message, address):
        user = colored(0, 128, 0, f'{address[0]}:{address[1]}')
        print(f'[{user}]: {message}')

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
        raise Exception(message)
        
