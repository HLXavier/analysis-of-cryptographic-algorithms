from PIL import Image
from utils import *
import matplotlib.pyplot as plt


def histogram(image, title):
    image = image.convert('L')
    intensities = list(image.getdata())

    plt.hist(intensities, 256, [0,255], edgecolor='none')

    plt.xlabel('Intensidade')
    plt.ylabel('Quantidade de pixels')

    plt.title(title)

    plt.savefig(f'plots/{title}_histogram.png')
    plt.close()
    