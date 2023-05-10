from PIL import Image
from image import *
from utils import *


def uaci(image, encrypt, key):
    width, height = image.size

    image1 = transform_image(image, encrypt, key)
    image2 = transform_image(transform_image(image), encrypt, key)

    image1 = image1.convert('L')
    image2 = image2.convert('L')

    intensities1 = list(image1.getdata())
    intensities2 = list(image2.getdata())

    sum = 0
    for i in range(width * height):
        sum += abs(intensities1[i] - intensities2[i])

    print(f'uaci: {100 * sum / (width*height * 255)}')