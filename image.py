from PIL import Image
from utils import *
from Crypto.Util.Padding import pad


def generate_images(name, key, encrypt, decrypt, block_size, resize=None):
    image = Image.open(f'{name}.png') 

    if resize:
        image = image.resize(resize)

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
