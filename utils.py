import numpy as np

def to_uint8(arr):
    return np.clip(arr, 0, 255).astype(np.uint8)

def inspect_image(img_arr):
    return {
        "Shape": img_arr.shape,
        "Dimensions": img_arr.ndim,
        "Data type": img_arr.dtype,
        "Min pixel value": img_arr.min(),
        "Max pixel value": img_arr.max()
    }
