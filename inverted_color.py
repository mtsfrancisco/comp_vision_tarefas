import cv2
import numpy as np


def invert_colors(img):
    height, width = img.shape[:2]
    img_copy = img.copy()

    for i in range(height):
        for j in range(width):
            color = img[i, j]
            for k in range(3):
                color[k] = 255 - color[k]
            img_copy[i, j] = color

    return img_copy

image = cv2.imread('images/image1.webp')
image2 = image.copy()
inverted_image = invert_colors(image)

image2 = cv2.bitwise_not(image2)
cv2.imshow('Function bitwise_not', image2)

cv2.imshow('Function inverter_cor', inverted_image)
cv2.waitKey(0)