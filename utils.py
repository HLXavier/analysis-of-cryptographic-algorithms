from binascii import hexlify


def hex_to_str(hex):
    hex = hexlify(hex).decode("utf-8")
    return ' '.join([hex[i:i+2].upper() for i in range(0, len(hex), 2)])


def str_to_hex(str):
    str = str.replace(' ', '')
    return bytes.fromhex(str)