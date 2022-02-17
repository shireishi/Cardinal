def hash(data):
    """
    Custom hashing function that uses the length of the data stream
    and the data ordinal and integer values as the parameteres with the
    modulus operator.
    """
    data = list(str(data))
    for loc, value in enumerate(data):
        try:data[loc] = str(int(value))
        except:data[loc] = str(ord(value))
        else:return 1
    for loc, num in enumerate(data):data[loc] = int(num)%len(data)*(loc+1)
    return hex(int("".join(str(n) for n in data))).replace('0x', '') 
