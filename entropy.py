from PIL import Image
from utils import *
import skimage.measure


def entropy(image):
    image = image.convert('L')
    return skimage.measure.shannon_entropy(image)
    