from PIL import Image
from utils import *

def change_random_rgb(image):
    new_image = image.copy()
    width, height = new_image.size

    x = randint(0, width - 1)
    y = randint(0, height - 1)

    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    new_image.putpixel((x, y), (r, g, b))
    return new_image


def transform_image(image, function, key, rounds=None):
    rgb_bytes = b''.join([bytes(pixel) for pixel in image.getdata()])
    encrypted_bytes = function(rgb_bytes, key, rounds=rounds)

    return Image.frombytes('RGB', image.size, encrypted_bytes)
