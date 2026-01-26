from image_processor import (
    inversion,
    gray_scale,
    flip_horizontally,
    flip_vertically,
    rotate_clockwise,
    rotate_anti_clockwise,
    adjust_brightness,
    adjust_contrast
)

def run_pipeline(img_arr, operation, value=None):

    if operation == "invert":
        return inversion(img_arr)

    if operation == "grayscale":
        return gray_scale(img_arr)

    if operation == "brightness":
        return adjust_brightness(img_arr, value)

    if operation == "contrast":
        return adjust_contrast(img_arr, value)

    if operation == "flip_h":
        return flip_horizontally(img_arr)

    if operation == "flip_v":
        return flip_vertically(img_arr)

    if operation == "rotate_cw":
        return rotate_clockwise(img_arr)

    if operation == "rotate_ccw":
        return rotate_anti_clockwise(img_arr)

    return img_arr
