import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from random import choice
import imageio
from PIL import Image

def create_fractal(xmin, xmax, ymin, ymax, xpoints, ypoints, h):
    x = np.linspace(xmin, xmax, xpoints)
    y = np.linspace(ymin, ymax, ypoints)
    c = x + y * 1j
    fractal = np.array([h(c) for c in c.flat]).reshape(xpoints, ypoints)
    return fractal

def create_mist():
    fractal = create_fractal(-2, 2, -2, 2, 800, 800, lambda c: (np.abs(np.sin(c))+np.abs(np.cos(c)))/2)
    fractal = np.asarray(fractal)
    fractal = np.interp(fractal, (fractal.min(), fractal.max()), (0, 255))
    fractal = fractal.astype(np.uint8)
    image = Image.fromarray(fractal)
    image = image.resize((500,500))
    image.show()

if __name__ == '__main__':
    create_mist()
