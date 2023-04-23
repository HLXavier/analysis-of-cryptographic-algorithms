from Crypto.Cipher import AES
from utils import *
from stats import *
from image import *


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

# histogram(f'decrypted_{name}_{scale[0]}x{scale[1]}')
# histogram(f'encrypted_{name}_{scale[0]}x{scale[1]}')

original_entropy = entropy(f'{names[0]}.png')
print(f'Entropy for original {names[0]}: {original_entropy}')
encrypted_entropy = entropy(f'output/encrypted_{names[0]}_256x256.png')
print(f'Entropy for encrypted {names[0]}: {encrypted_entropy}')

print(f'Decrypted correlation: {correlation(get_decrypted_path(names[0], 512))}')
print(f'Encrypted correlation: {correlation(get_encrypted_path(names[0], 512))}')
