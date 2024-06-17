from datetime import datetime
import numpy as np
import random

def random_color():
    levels = range(0,150,32)
    return tuple(random.choice(levels) for _ in range(3))

def get_gradient_2d(start, stop, width, height, is_horizontal):
    if is_horizontal:
        return np.tile(np.linspace(start, stop, width), (height, 1))
    else:
        return np.tile(np.linspace(start, stop, height), (width, 1)).T

def get_gradient_3d(width, height, start_list, stop_list, is_horizontal_list):
    result = np.zeros((height, width, len(start_list)), dtype=np.float64)

    for i, (start, stop, is_horizontal) in enumerate(zip(start_list, stop_list, is_horizontal_list)):
        result[:, :, i] = get_gradient_2d(start, stop, width, height, is_horizontal)

    return result

from PIL import Image

def add_random_white_pixels(array, num_pixels):
    height, width, _ = array.shape
    for _ in range(num_pixels):
        x, y = random.randint(0, width-1), random.randint(0, height-1)
        array[y, x] = [255, 255, 255]
    return array

array = get_gradient_3d(1710, 1112, (random_color()), (random_color()), (True, True, True))

Image.fromarray(np.uint8(array)).save("data/gray_gradient_h.png", quality=95)

# ![](data/dst/gray_gradient_h.jpg)

array = get_gradient_3d(1710, 1112, (random_color()), (random_color()), (False, False, False))
Image.fromarray(np.uint8(array)).save("data/gray_gradient_v.png", quality=95)

# ![](data/dst/gray_gradient_v.jpg)

array = get_gradient_3d(1710, 1112, (random_color()), (random_color()), (True, False, False))
array = add_random_white_pixels(array, 1000)  # Add 1000 random white pixels
Image.fromarray(np.uint8(array)).save("data/color_gradient.png", quality=95)

# ![](data/dst/color_gradient.jpg)
