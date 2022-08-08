import numpy as np
import random
import Xlib.display

display = Xlib.display.Display()
screen = display.screen()

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


array = get_gradient_3d(screen.width_in_pixels, screen.height_in_pixels, (random_color()), (random_color()), (True, True, True))
Image.fromarray(np.uint8(array)).save('/home/snorre/Documents/gradientwall/data/gray_gradient_h.jpg', quality=5000)

# ![](data/dst/gray_gradient_h.jpg)

array = get_gradient_3d(screen.width_in_pixels, screen.height_in_pixels, (random_color()), (random_color()), (False, False, False))
Image.fromarray(np.uint8(array)).save('/home/snorre/Documents/gradientwall/data/gray_gradient_v.jpg', quality=5000)

# ![](data/dst/gray_gradient_v.jpg)

array = get_gradient_3d(screen.width_in_pixels, screen.height_in_pixels, (random_color()), (random_color()), (True, False, False))
Image.fromarray(np.uint8(array)).save('/home/snorre/Documents/gradientwall/data/color_gradient.jpg', quality=5000)

# ![](data/dst/color_gradient.jpg)