def hash(data):
    if isinstance(data, str) != True:data = str(data)
    data = [x for x in data]
    for loc, value in enumerate(data):
        try: # this will parse through the data stream and convert all values, even letters, into numbers
            data[loc] = int(value)
        except:
            data[loc] = ord(value)
        else:
            return 1
    for loc, num in enumerate(data):
        data[loc] = num%len(data)*(loc+1)
    return data

