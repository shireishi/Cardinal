## Should the header be in json format?
As I continue to think about how the header should be formatted, I run into the problem of further complexity. For example, say I wanted to add future protocols, then I would almost be required to increase the required space proportional to the ammount of information I wish to transfer in the headers. However, if I made this system generally more modular and with a nicer format than hardcoded positions for information, it could easily solve complexity problems.
-- Current Method --
```
protocol key - length of message in binary - data hash confirming information
```
-- Planned Method --
The initial header will simply be a header of 64 bit length that contains the length of the following message. The json header will then tell the server how long the actual message is.
```json
{
    "protocol": "transfer",
    "length": 72,
    "hash": "asdkfhalsehrnjkb123iukh12kj3b1273yuioghsa7yid8fyuiausdgf"
}
```

## Server Architecture Notes
    The server architecture will be primarily composed of a defined header that will contain the information
    about the length of the incoming information, which can range a very large data set.

    Custom communication protocols will be made, as well as repeating data with the header toggle of a resend
    to denote whether or not all of the original information was recieved. 

    There should also be a hash check system where a hash is sent along with the information, the information
    is hashed by the same algorithm and then compared to make sure the correct data was recieved.

    TODO
    - [ ] Set up the client-side recieving after a command is sent to the server, if the command does not have a set reply, then just send an empty buffer that is disregarded from the client.

## Header Format
    [key(32int)][len of message[1byte binary]][len 24 hash of data]
    Example:
    10000000000000000000000000000000 00001010 1232106153434310227543472
    Obiviously remove the spaces but you get the idea
    The total length of the above string is 64 and would be transmitted before the actual data. The binary value providing the length of the message is read second
    After the type of communication is read from the key, and then the hash is read after the recieving to confirm that the data recieved and the data sent is the same.

    The sha256 hashing algorithm will be used simply because of its modern-esque usage.

## Cardinal Naming System CNS
    This will be a localized database which will manage the pseudonyms of different keys for the server-side architecture. For example, the client does not need the exact
    key for a transmission, but could instead can send "transmission" as a string and the CNS will return to the server the key for a transmission key.

## Random Notes
Today I learned that you can use some variable one-liner assignments that use wildcards.
For example, if you use the one-liner; `a, b, *c = [1, 2, 3, 4, 5]` then you will get the output of
`print(a, b, c) # 1 2 [3, 4, 5]` and that can be really useful, perhaps there is a way to integrate this into semi-list combinations. In theory, something like:
```python
l = [1, 2, 3, 4, 5, 6]
*a, *b = l
print(a, b)
# [1, 2, 3] [4, 5, 6]
```
I think that having this as an actual modular half list assignment system could be really nice, but I don't know if the python compiler would like that since 

## Bitwise Operations
### & Operator
the & bitwise operator checks if the bit in a certain position exists as a value or if two ints or uints are equal by checking all of their bits and their correspondence in certain locations.