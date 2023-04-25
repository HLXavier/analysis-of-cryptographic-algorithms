from PIL import Image
from utils import *
import matplotlib.pyplot as plt
import numpy as np
import skimage.measure


def avalanche(encrypt, encryption_rounds):
    executions = 100
    tot = 0

    for _ in range(executions):
        plain_text = random_bytes(32)

        key = random_bytes(32)
        shifted_key = shift_bit(key)

        cipher = encrypt(plain_text, key, encryption_rounds)
        shifted_cipher = encrypt(plain_text, shifted_key, encryption_rounds)

        str_cipher = hex_to_str(cipher).split()
        str_shifted_cipher = hex_to_str(shifted_cipher).split()

        similar_bytes = 0
        for i in range(len(str_cipher)):
            if str_cipher[i] == str_shifted_cipher[i]:
                similar_bytes += 1

        tot += similar_bytes / len(str_cipher)


    print(f'{tot * 100 / executions}% de similaridade entre os bytes.')


def generate_images(name, key, encrypt, decrypt):
    image = Image.open(f'{name}.png')
    width, height = image.size 

    rgb_bytes = b''.join([bytes(pixel) for pixel in image.getdata()])

    encrypted_bytes = encrypt(rgb_bytes, key, 1)
    decrypted_bytes = decrypt(encrypted_bytes, key, 1)

    image = Image.frombytes('RGB', (width, height), encrypted_bytes)
    image.save(f'output/encrypted_{name}.png')

    image = Image.frombytes('RGB', (width, height), decrypted_bytes)
    image.save(f'output/decrypted_{name}.png')


def histogram(name):
    image = Image.open(f'output/{name}.png') 
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


# PRECISA SER ATUALIZADO
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
    