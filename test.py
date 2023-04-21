from PIL import Image
from utils import *
from random import choice


image = Image.open("white.png") 
width, height = image.size

pixel_bytes = b"".join([bytes(pixel) for pixel in image.getdata()])
pixel_bytes_f = hex_to_str(pixel_bytes)
p = pixel_bytes_f.split()

for i in range(len(p)):
    change = choice([True, False])
    if change:
        p[i] = '00'
    
p = ' '.join(p)

print(p)

pixel_bytes = str_to_hex(p)

# Create an Image object from RGB bytes
image = Image.frombytes("RGB", (width, height), pixel_bytes)

# Save the image
image.save("output_white.png") 
