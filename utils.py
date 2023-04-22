from binascii import hexlify
from os import urandom
from random import randint


def hex_to_str(hex):
    hex = hexlify(hex).decode("utf-8")
    return ' '.join([hex[i:i+2].upper() for i in range(0, len(hex), 2)])


def str_to_hex(str):
    if len(str) > 2:
        str = str.replace(' ', '')
    return bytes.fromhex(str)


def random_bytes(size):
    return urandom(size)


def shift_bit(bytes):
    str_bytes = hex_to_str(bytes).split()
    byte_pos = randint(0, len(str_bytes)-1)
    str_byte = str_bytes[byte_pos]

    int_byte = int(str_byte, 16)
    bin_byte = bin(int_byte).replace('0b', '').zfill(8)
    bit_pos = randint(0, 7)

    bit = bin_byte[bit_pos]
    if bit == '0':
        bin_byte = bin_byte[:bit_pos] + '1' + bin_byte[bit_pos + 1:]
    else:
        bin_byte = bin_byte[:bit_pos] + '0' + bin_byte[bit_pos + 1:]

    bin_byte = '0b' + bin_byte

    int_byte = int(bin_byte, 2)

    str_byte = hex(int_byte)[2:]
    str_byte = str_byte.upper().zfill(2)

    str_bytes[byte_pos] = str_byte

    return str_to_hex(' '.join(str_bytes))

shift_bit(random_bytes(16))
