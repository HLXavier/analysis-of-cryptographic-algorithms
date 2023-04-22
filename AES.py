from Crypto.Cipher import AES
from utils import *
from image import *


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


scale = (512, 512)
name = 'lenna'
generate_images(name, key, encrypt, decrypt, AES.block_size, scale)

# histogram(f'decrypted_{name}_{scale[0]}x{scale[1]}')
# histogram(f'encrypted_{name}_{scale[0]}x{scale[1]}')

print(f'Decrypted correlation: {correlation(get_decrypted_path(name, 512))}')
print(f'Encrypted correlation: {correlation(get_encrypted_path(name, 512))}')