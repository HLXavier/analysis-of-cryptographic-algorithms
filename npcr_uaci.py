from PIL import Image
from utils import *

def npcr_uaci(path, encrypt, key, rounds):
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

    npcr_sum = 0
    uaci_diff = 0
    for i in range(width * height):
        npcr_sum += int(intensities1[i] == intensities2[i])
        uaci_diff += abs(intensities1[i] - intensities2[i])

    print(f'npcr: {100 * (npcr_sum / (width*height))}')
    print(f'uaci: {100 * (uaci_diff / (width*height*255))}')

