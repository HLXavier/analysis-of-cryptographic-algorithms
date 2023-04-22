from Crypto.Cipher import AES
from utils import *
from stats import *


def encrypt(plain_text, key):
    aes = AES.new(key, AES.MODE_ECB)
    cipher = aes.encrypt(plain_text)
    return cipher


def decrypt(cipher_text, key):
    aes = AES.new(key, AES.MODE_ECB)
    plain_text = aes.decrypt(cipher_text)
    return plain_text


scales = [(128, 128), (256, 256), (512, 512)]
names = ['lenna', 'panda', 'fruit']


# key = random_bytes(16)
# print(f'key: {hex_to_str(key)}')
# for name in names:
#     print('-'*20)
#     print(name)
#     print('-'*20)
#     for scale in scales:
#         print(f'{scale[0]}x{scale[1]}')
#         generate_images(name, key, encrypt, decrypt, AES.block_size, scale)
#         print()

hist_names = []
hist_names = hist_names + names

for name in names:
    for scale in scales:
        hist_names.append(f'output/encrypted_{name}_{scale[0]}x{scale[1]}')
        hist_names.append(f'output/decrypted_{name}_{scale[0]}x{scale[1]}')

# for name in hist_names:
#     print(name)

# for name in hist_names:
#     histogram(name)
        
for name in hist_names:
    print(f'name: {name}')
    entropy(name)
    print()

# avalanche(encrypt, decrypt)