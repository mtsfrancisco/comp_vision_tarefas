import cv2
import numpy as np


def gray_to_rgb(gray):
    height, width = gray.shape[:2]
    img_copy = np.zeros((height, width, 3))

    for i in range(height):
        for j in range(width):
                color = gray[i, j]
                img_copy[i, j] = [color, color, color]

    return img_copy.astype(np.uint8)

def grayScale(img):
    height, width = img.shape[:2]
    img_copy = np.zeros((height, width))

    for i in range(height):
        for j in range(width):
            color = img[i, j]
            img_copy[i, j] = 0.2989 * color[2] + 0.5870 * color[1] + 0.1140 * color[0]

    return img_copy.astype(np.uint8)

img = cv2.imread("images/image1.webp")
img_copy = img.copy()
gray_copy = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)

gray = grayScale(img)
rgb_gray = gray_to_rgb(gray_copy)

rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

cv2.imshow("RGB Gray", rgb_gray)
cv2.imshow("RGB", rgb)
cv2.imshow("Gray", gray)
cv2.waitKey(0)