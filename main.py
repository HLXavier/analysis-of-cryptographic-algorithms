from sys import argv
from utils import *
from ciphers import *
from PIL import Image
from avalanche import avalanche_effect
from entropy import entropy
from image import transform_image
from histogram import histogram


cipher = argv[1] 
op = argv[2]

ciphers = {
        'aes': [aes_encrypt, aes_decrypt, 16],
        '3des': [triple_des_encrypt, triple_des_decrypt, 16]
    }

encrypt = ciphers[cipher][0]
decrypt = ciphers[cipher][1]
key_size = ciphers[cipher][2]


def _avalanche():
    encryption_rounds = int(argv[3])

    key = random_bytes(key_size)

    print(avalanche_effect(encrypt, key, encryption_rounds))


def _entropy():
    path = argv[3]

    image = Image.open(path)

    print(entropy(image)) 


def _enc_image():
    path = argv[3]

    image = Image.open(path)
    key = random_bytes(key_size)
    encrypted_image = transform_image(image, encrypt, key)

    text_key = hex_to_str(key).replace(' ', '')
    print(f'KEY: {text_key}')

    path = path.replace('images/', 'images/encrypted_')
    encrypted_image.save(path)


def _dec_image():
    path = argv[3]
    key = argv[4]

    key = separete_hex(key)
    key = str_to_hex(key)

    image = Image.open(path)
    encrypted_image = transform_image(image, decrypt, key)

    path = path.replace('images/encrypted_', 'images/decrypted_')
    encrypted_image.save(path)
    

def _histogram():
    path = argv[3]

    image = Image.open(path)
    title = path.replace('images/', '')

    histogram(image, title)


ops = {
    'avalanche': _avalanche,
    'entropy': _entropy,
    'enc-image': _enc_image,
    'dec-image': _dec_image,
    'histogram': _histogram
}

op = ops[op]
op()
