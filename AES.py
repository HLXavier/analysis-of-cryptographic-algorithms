from Crypto.Cipher import AES
from utils import *
from image import generate_images


def encrypt(plain_text, key):
    aes = AES.new(key, AES.MODE_ECB)
    cipher = aes.encrypt(plain_text)
    return cipher


def decrypt(cipher_text, key):
    aes = AES.new(key, AES.MODE_ECB)
    plain_text = aes.decrypt(cipher_text)
    return plain_text


plain_text = str_to_hex('0A 0B 0C 0D 0F 01 02 03 04 05 06 07 08 09 1A 2B')
key = str_to_hex('01 02 04 05 06 AA BB CC 44 DD EE 88 09 04 05 06')


# print(f'plain text      : {hex_to_str(plain_text)}')
# print(f'key             : {hex_to_str(key)}')
# cipher_text = encrypt(plain_text, key)
# plain_text = decrypt(cipher_text, key)
# print(f'encrypted text  : {hex_to_str(cipher_text)}')
# print(f'decrypted cipher: {hex_to_str(plain_text)}')

def avanlanche():
    p1 = '64254F9981329E35A60DA284FD675350'
    p2 = '642587528132D663A60DCF1DFD67E530'

    same = 0
    for i in range(32):
        if p1[i] == p2[i]: same += 1

    print(same)

    avalanche = same / 32
    print(avalanche)


generate_images('fruit', key, encrypt, decrypt, AES.block_size, resize=(220, 220))
