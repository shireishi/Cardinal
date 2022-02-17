from globvals import *
from notifications import *

def buff(data):return str(data).encode(FORMAT) + b' '*(HEADER-len(str(data)))

def colored(r, g, b, text): return "\033[38;2;{};{};{}m{}\033[m".format(r, g, b, text)

def compress(data):
    data_length = len(data)
    compressed = ""
    count = 1

    for index, letter in enumerate(data):
        try:
            if data[index+1] == letter:count+=1
            elif data[index+1] != letter:
                compressed += letter+str(count)
                count = 1
        except Exception as e:
            System.notify(e)
            continue

    return compressed