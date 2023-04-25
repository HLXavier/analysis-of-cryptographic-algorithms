from utils import *
from stats import *
from AES import AES

def aesEncrypt(plain_text, key, rounds=10):
    aes = AES(key)
    aes.nr = rounds
    return aes.encrypt(plain_text)


def aesDecrypt(cipher_text, key, rounds=10):
    aes = AES(key)
    aes.nr = rounds
    return aes.decrypt(cipher_text)
    

names = ['lenna', 'panda', 'fruit']

key = random_bytes(16)
# for name in names:
#     generate_images(name, key, aesEncrypt, aesDecrypt)

for name in names:
    histogram(f'decrypted_{name}')
    histogram(f'encrypted_{name}')

# print(f'Decrypted correlation: {correlation(get_decrypted_path(name, 512))}')
# print(f'Encrypted correlation: {correlation(get_encrypted_path(name, 512))}')

# key = random_bytes(16)
# shifted_key = shift_bit(key)
# word = random_bytes(16)

# print('plain text: ' + hex_to_str(word))
# cipher = aesEncrypt(word, key)
# shifted_cipher = aesEncrypt(word, shifted_key)
# print('ciphered 1: ' + hex_to_str(cipher))
# print('ciphered 2: ' + hex_to_str(shifted_cipher))

# for i in range(5):
#     print(f'{i+1} rodadas de criptografia: ', end='')
#     avalanche(aesEncrypt, i+1)

# key = random_bytes(16)
# word = random_bytes(5)

# print(hex_to_str(word))
# word, pad = aesPad(word)

# encrypted = aesEncrypt(word, key)

# print(hex_to_str(encrypted))

# decrypted = aesDecrypt(encrypted, key)

# decrypted = aesUnpad(decrypted, pad)

# print(hex_to_str(decrypted))
