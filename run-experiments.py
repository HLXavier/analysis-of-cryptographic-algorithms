from typing import Callable, Tuple
from PIL import Image
from main import *
import stats
import image

# Use this to encrypt or decrypt an image, depending on which method you
# pass to the crypt parameter
def crypt_image(crypt, key, rounds, original_image_path, output_path):
    image = Image.open(original_image_path)
    width, height = image.size 

    rgb_bytes = b''.join([bytes(pixel) for pixel in image.getdata()])

    encrypted_bytes = crypt(rgb_bytes, key, rounds)

    image = Image.frombytes('RGB', (width, height), encrypted_bytes)
    image.save(output_path)

def avalanche(encrypt):
    for i in range(5):
        stats.avalanche(encrypt, i + 1, 24)

key = random_bytes(16)

def experiments(name, encrypt, decrypt):
    # # encrypt
    # crypt_image(encrypt, key, 16, f'lenna.png', f'output/{name}_encrypted_lenna.png')

    # # decrypt
    # crypt_image(decrypt, key, 16, f'output/{name}_encrypted_lenna.png', f'output/{name}_decrypted_lenna.png')

    # avalanche(encrypt)

    # # correlation
    # image.correlation(f'output/{name}_encrypted_lenna.png', f'output/{name}_correlation_encrypted_lenna.png')

    # entropy = stats.entropy(f'output/{name}_encrypted_lenna.png')
    # print(f'entropy: {entropy}')

    # stats.histogram(f'output/{name}_encrypted_lenna.png', f'output/{name}_histogram_encrypted_lenna.png')

    stats.npcr(f'lenna.png', encrypt, key, 10)
    stats.uaci(f'lenna.png', encrypt, key, 10)




# setup
image.correlation(f'lenna.png', f'output/correlation_lenna.png')
stats.histogram(f'lenna.png', f'output/histogram_lenna.png')

# run experiments
# experiments('3des', tripleDesEncrypt, tripleDesDecrypt)
experiments('aes', aesEncrypt, aesDecrypt)