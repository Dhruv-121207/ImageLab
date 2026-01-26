import numpy as np

def inversion(img_arr):

    arr = img_arr.copy()
    arr = 255 - arr

    return arr

def gray_scale(img_arr):

    gray = 0.299 * img_arr[:,:,0] + 0.587 * img_arr[:,:,1] + 0.114 * img_arr[:,:,2]
    gray = np.clip(gray,0,255).astype(np.uint8)

    grayscale_image = np.stack((gray,gray,gray),axis = 2)

    return grayscale_image

def flip_horizontally(img_arr):

    arr = img_arr.copy()
    flipped = arr[:,::-1,:]

    return flipped

def flip_vertically(img_arr):

    arr = img_arr.copy()
    flipped = arr[::-1,:,:]

    return flipped

def rotate_clockwise(img_arr):

    h,w,c = img_arr.shape
    transpose = np.zeros((w,h,c),dtype=img_arr.dtype)

    for row in range(h):
        for col in range(w):
            transpose[col,row] = img_arr[row,col]

    clockwise_rotated_image = transpose[:,::-1,:]

    return clockwise_rotated_image

def rotate_anti_clockwise(img_arr):

    h,w,c = img_arr.shape
    transpose = np.zeros((w,h,c),dtype=img_arr.dtype)

    for row in range(h):
        for col in range(w):
            transpose[col,row] = img_arr[row,col]

    anti_clockwise_rotated_image = transpose[::-1,:,:]

    return anti_clockwise_rotated_image

def adjust_brightness(img_arr,slider):

    slider = np.clip(slider,-100,100)
    gamma = (2.5) ** (-slider/100)

    arr = img_arr.astype(np.float32) / 255.0
    arr = arr ** gamma
    arr = arr * 255

    arr = np.clip(arr,0,255).astype(np.uint8)

    return arr

def adjust_contrast(img_arr,slider):

    slider = np.clip(slider,-100,100)
    factor = 1 + slider/100

    arr = img_arr.astype(np.float32)
    arr = (arr - 128) * factor + 128

    arr = np.clip(arr,0,255).astype(np.uint8)

    return arr

