import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.decomposition import PCA

image = Image.open('papa.JPG')
width, height = image.size
image2 = Image.new("RGB", (width, height))

img_pixels = []
for y in range(height):
        for x in range(width):
        	img_pixels.append(image.getpixel((x,y)))
        	image2.putpixel((x,y),image.getpixel((x,y)))
img_pixels = np.array(img_pixels)
print img_pixels

