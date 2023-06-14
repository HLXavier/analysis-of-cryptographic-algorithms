import matplotlib.pyplot as plt
from PIL import Image
import scipy.stats as stats

def correlation(file_path, output_path):
    image = Image.open(file_path)
    image = image.convert('L')  

    pairs = get_neighboring_pixel_pairs(image)
    x, y = zip(*pairs)

    plt.scatter(x, y, s=1)
    plt.title('correlation')

    plt.savefig(output_path)
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