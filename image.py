from Crypto.Util.Padding import pad
from PIL import Image
from utils import *
import matplotlib.pyplot as plt
import cv2


def generate_images(name, key, encrypt, decrypt, block_size, scale):
    image = Image.open(f'{name}.png') 

    if scale != (512, 512):
        image = image.resize(scale)

    width, height = image.size

    rgb_bytes = b''.join([bytes(pixel) for pixel in image.getdata()])

    no_pad_size = len(rgb_bytes)

    rgb_bytes = pad(rgb_bytes, block_size)
    encrypted_bytes = encrypt(rgb_bytes, key)
    decrypted_bytes = decrypt(encrypted_bytes, key)

    image = Image.frombytes('RGB', (width, height), encrypted_bytes[:no_pad_size])
    image.save(f'output/encrypted_{name}_{width}x{height}.png')

    image = Image.frombytes('RGB', (width, height), decrypted_bytes[:no_pad_size])
    image.save(f'output/decrypted_{name}_{width}x{height}.png')


def histogram(name):
    path = f'output/{name}.png'
    image = cv2.imread(path, 0)

    plt.hist(image.ravel(), 256, [0,255], edgecolor='none')
    plt.title('histogram')

    plt.savefig(f'output/{name}_hist.png')
    plt.close()
