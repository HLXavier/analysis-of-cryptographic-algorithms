from Crypto.Util.Padding import pad
from PIL import Image
from utils import *
from time import time
import matplotlib.pyplot as plt
import cv2
import numpy as np

def avalanche(encrypt, decrypt):
    key = random_bytes(16)
    shifted_key = shift_bit(key)
    plain_text = random_bytes(16)

    print(f'key           : {hex_to_str(key)}')
    print(f'plain text    : {hex_to_str(plain_text)}')

    encrypted = encrypt(plain_text, key)

    print(f'encrypted text: {hex_to_str(encrypted)}')

    decrypted = decrypt(encrypted, key)

    print(f'decrypted text: {hex_to_str(decrypted)}')

    print('-' * 10)

    print(f'shifted key   : {hex_to_str(shifted_key)}')
    print(f'plain text    : {hex_to_str(plain_text)}')

    shifted_encrypted = encrypt(plain_text, shifted_key)

    print(f'encrypted text: {hex_to_str(shifted_encrypted)}')

    shifted_decrypted = decrypt(encrypted, shifted_key)

    print(f'decrypted text: {hex_to_str(shifted_decrypted)}')


def generate_images(name, key, encrypt, decrypt, block_size, scale):
    image = Image.open(f'{name}.png') 

    if scale != (512, 512):
        image = image.resize(scale)

    width, height = image.size

    rgb_bytes = b''.join([bytes(pixel) for pixel in image.getdata()])

    no_pad_size = len(rgb_bytes)

    rgb_bytes = pad(rgb_bytes, block_size)

    start = time()
    encrypted_bytes = encrypt(rgb_bytes, key)
    print(f'encryption time: {time() - start}')

    start = time()
    decrypted_bytes = decrypt(encrypted_bytes, key)
    print(f'decryption time: {time() - start}')

    image = Image.frombytes('RGB', (width, height), encrypted_bytes[:no_pad_size])
    image.save(f'output/encrypted_{name}_{width}x{height}.png')

    image = Image.frombytes('RGB', (width, height), decrypted_bytes[:no_pad_size])
    image.save(f'output/decrypted_{name}_{width}x{height}.png')


def histogram(name):
    image = cv2.imread(f'{name}.png', 0)

    plt.hist(image.ravel(), 256, [0,255], edgecolor='none')
    plt.title('histogram')

    name = name.replace('output/', '')
    plt.savefig(f'hist/{name}_hist.png')
    plt.close()


def entropy(name):
    image = cv2.imread(f'{name}.png', 0)

    marg = np.histogramdd(np.ravel(image), bins = 256)[0] / image.size
    marg = list(filter(lambda p: p > 0, np.ravel(marg)))
    entropy = -np.sum(np.multiply(marg, np.log2(marg)))

    print(f'entropy: {entropy}')
