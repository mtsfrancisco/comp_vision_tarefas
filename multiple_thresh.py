import cv2
import numpy as np
import matplotlib.pyplot as plt
import random

def generate_random_rgb_values(size):
    rgb_values = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(size)]
    return rgb_values

def multi_threshold(img, thresholds):
    img_copy = img.copy()
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width = gray_img.shape
    colors = generate_random_rgb_values(len(thresholds) + 1)


    for i in range(height):
        for j in range(width):
            
            if gray_img[i, j] < thresholds[0]:
                img_copy[i, j] = colors[0]

            elif gray_img[i, j] >= thresholds[-1]:
                img_copy[i, j] = colors[-1]

            for k in range(1, len(thresholds)):
                if gray_img[i, j] >= thresholds[k-1] and gray_img[i, j] < thresholds[k]:
                    img_copy[i, j] = colors[k]

    return img_copy   


img = cv2.imread("imagens/image1.webp")
thresh_img = multi_threshold(img, [100,150,200])


cv2.imshow("Thresh", thresh_img)
cv2.waitKey(0)