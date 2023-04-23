from Crypto.Util.Padding import pad
from PIL import Image
from utils import *
from time import time
import matplotlib.pyplot as plt
import numpy as np
import skimage.measure


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


def encrypt_image_bytes(image, key, encrypt, block_size):
    rgb_bytes = b''.join([bytes(pixel) for pixel in image.getdata()])
    no_pad_size = len(rgb_bytes)
    rgb_bytes = pad(rgb_bytes, block_size)
    return encrypt(rgb_bytes, key), no_pad_size


def generate_images(name, key, encrypt, decrypt, block_size, scale):
    image = Image.open(f'{name}.png') 

    if scale != (512, 512):
        image = image.resize(scale)

    encrypted_bytes, no_pad_size = encrypt_image_bytes(image, key, encrypt, block_size)
    decrypted_bytes = decrypt(encrypted_bytes, key)

    image = Image.frombytes('RGB', scale, encrypted_bytes[:no_pad_size])
    image.save(f'output/encrypted_{name}_{scale[0]}x{scale[1]}.png')

    image = Image.frombytes('RGB', scale, decrypted_bytes[:no_pad_size])
    image.save(f'output/decrypted_{name}_{scale[0]}x{scale[1]}.png')


def histogram(name):
    image = Image.open(f'{name}.png') 
    image = image.convert('L')
    intensities = list(image.getdata())

    plt.hist(intensities, 256, [0,255], edgecolor='none')
    plt.title('histogram')

    name = name.replace('output/', '')
    plt.savefig(f'hist/{name}_hist.png')
    plt.close()


def entropy(path):
    image = Image.open(path) 
    image = image.convert('L')

    return skimage.measure.shannon_entropy(image)


def uaci(name, key, encrypt, block_size):
    image1 = Image.open(f'{name}.png')
    image2 = image1.copy()
    
    width, height = image1.size

    x = randint(0, width - 1)
    y = randint(0, height - 1)

    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    image2.putpixel((x, y), (r, g, b))

    image1, no_pad_size = encrypt_image_bytes(image1, key, encrypt, block_size)
    image2, _ = encrypt_image_bytes(image2, key, encrypt, block_size)

    image1 = Image.frombytes('RGB', (width, height), image1[:no_pad_size])
    image2 = Image.frombytes('RGB', (width, height), image2[:no_pad_size])

    image1 = image1.convert('L')
    image2 = image2.convert('L')

    intensities1 = list(image1.getdata())
    intensities2 = list(image2.getdata())

    sum = 0
    for i in range(width*height):
        sum += abs(intensities1[i] - intensities2[i])

    print(f'uaci: {100 * sum / (width*height * 255)}')
    