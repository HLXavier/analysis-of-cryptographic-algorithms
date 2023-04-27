from PIL import Image
from utils import *
from time import time
import matplotlib.pyplot as plt
import numpy as np
import skimage.measure


def avalanche(encrypt, encryption_rounds, key_size):
    executions = 100
    tot = 0

    for _ in range(executions):
        plain_text = random_bytes(32)

        key = random_bytes(key_size)
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

    image = image.resize((512, 512))

    rgb_bytes = b''.join([bytes(pixel) for pixel in image.getdata()])

    encrypted_bytes = encrypt(rgb_bytes, key)
    decrypted_bytes = decrypt(encrypted_bytes, key)

    image = Image.frombytes('RGB', (width, height), encrypted_bytes)
    image.save(f'output/encrypted_{name}.png')

    image = Image.frombytes('RGB', (width, height), decrypted_bytes)
    image.save(f'output/decrypted_{name}.png')


def histogram(image_path, output_path):
    image = Image.open(image_path) 
    image = image.convert('L')
    intensities = list(image.getdata())

    plt.hist(intensities, 256, [0,255], edgecolor='none')

    plt.xlabel('Intensidade')
    plt.ylabel('Quantidade de pixels')

    if ('lenna' in image_path): plt.title('Lenna')
    if ('panda' in image_path): plt.title('Panda')
    if ('fruit' in image_path): plt.title('Frutas')

    plt.savefig(output_path)
    plt.close()


def entropy(path):
    image = Image.open(path) 
    image = image.convert('L')

    return skimage.measure.shannon_entropy(image)

def npcr(path, encrypt, key, rounds):
    image1 = Image.open(path)
    image2 = image1.copy()
    
    width, height = image1.size

    x = randint(0, width - 1)
    y = randint(0, height - 1)

    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    image2.putpixel((x, y), (r, g, b))

    image1bytes = b''.join([bytes(pixel) for pixel in image1.getdata()])
    image2bytes = b''.join([bytes(pixel) for pixel in image2.getdata()])

    image1 = encrypt(image1bytes, key, rounds)
    image2 = encrypt(image2bytes, key, rounds)

    image1 = Image.frombytes('RGB', (width, height), image1)
    image2 = Image.frombytes('RGB', (width, height), image2)

    image1 = image1.convert('L')
    image2 = image2.convert('L')

    intensities1 = list(image1.getdata())
    intensities2 = list(image2.getdata())

    sum = 0
    for i in range(width * height):
        sum += int(intensities1[i] == intensities2[i])

    print(f'npcr: {100 * (sum / (width*height))}')

def uaci(path, encrypt, key, rounds):
    image1 = Image.open(path)
    image2 = image1.copy()
    
    width, height = image1.size

    x = randint(0, width - 1)
    y = randint(0, height - 1)

    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    image2.putpixel((x, y), (r, g, b))

    image1bytes = b''.join([bytes(pixel) for pixel in image1.getdata()])
    image2bytes = b''.join([bytes(pixel) for pixel in image2.getdata()])

    image1 = encrypt(image1bytes, key, rounds)
    image2 = encrypt(image2bytes, key, rounds)

    image1 = Image.frombytes('RGB', (width, height), image1)
    image2 = Image.frombytes('RGB', (width, height), image2)

    image1 = image1.convert('L')
    image2 = image2.convert('L')

    intensities1 = list(image1.getdata())
    intensities2 = list(image2.getdata())

    total = 0
    for i in range(width * height):
        total += abs(intensities1[i] - intensities2[i])

    print(f'uaci: {100 * (total / (width * height * 255))}')
    