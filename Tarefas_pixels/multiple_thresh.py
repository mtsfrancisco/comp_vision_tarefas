import cv2
import numpy as np
import matplotlib.pyplot as plt
import random
import time

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
            pixel_value = gray_img[i, j]
            for k, threshold in enumerate(thresholds):
                if pixel_value < threshold:
                    img_copy[i, j] = colors[k]
                    break
            else:
                img_copy[i, j] = colors[-1]

    return img_copy


img = cv2.imread("images/image1.webp")

start_time = time.time()
thresh_img = multi_threshold(img, [100,150,200])
end_time = time.time()

print(end_time - start_time)
cv2.imshow("Thresh", thresh_img)
cv2.waitKey(0)