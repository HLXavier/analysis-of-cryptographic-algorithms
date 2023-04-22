from Crypto.Util.Padding import pad
from PIL import Image
from utils import *
import matplotlib.pyplot as plt
import cv2
import scipy.stats as stats


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

def correlation(path):
    image = Image.open(path)
    image = image.convert('L')  

    pairs = get_neighboring_pixel_pairs(image)
    x, y = zip(*pairs)

    plt.scatter(x, y, s=1)
    plt.title('correlation')

    plt.savefig(f'{path[:-4]}_correlation.png')
    plt.close()

    r, p = stats.pearsonr(x, y)
    return r

def get_neighboring_pixel_pairs(image):
    width, height = image.size

    pairs = []
    for i in range(width - 1):
        for j in range(height - 1):
            pixel = image.getpixel((i, j))
            right_pixel = image.getpixel((i, j+1))
            bottom_pixel = image.getpixel((i+1, j))
            bottom_right_pixel = image.getpixel((i+1, j+1))
            
            pairs.append((pixel, right_pixel))
            pairs.append((pixel, bottom_pixel))
            pairs.append((pixel, bottom_right_pixel))
    
    return pairs

def get_encrypted_path(name, size):
    return f'output/encrypted_{name}_{size}x{size}.png'

def get_decrypted_path(name, size):
    return f'output/decrypted_{name}_{size}x{size}.png'