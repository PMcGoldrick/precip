import struct


def byteArrayToInt4(val):
    return struct.unpack("!I", ''.join([chr(i) for i in val]))[0]

def int4ToByteArray(val):
    return struct.pack("!I", val)
