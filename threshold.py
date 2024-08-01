import cv2
import numpy as np
import matplotlib.pyplot as plt


def adaptive_threshold_mean_c(image, block_size=11, c=2):

    height, width = image.shape
    thresholded = np.zeros_like(image)
    half_block_size = block_size // 2
    
    for i in range(height):
        for j in range(width):
            
            top = max(0, i - half_block_size)
            bottom = min(height - 1, i + half_block_size)
            left = max(0, j - half_block_size)
            right = min(width - 1, j + half_block_size)
            block_mean = np.mean(image[top:bottom+1, left:right+1])

            if image[i, j] > block_mean - c:
                thresholded[i, j] = 255
            else:
                thresholded[i, j] = 0
        
    return thresholded

def threshold(img, thresh):

    height, width = img.shape

    for i in range(height):
        for j in range(width):
            if img[i, j] > thresh:
                img[i, j] = 255
            else:
                img[i, j] = 0

    return img

img = cv2.imread("images/image1.webp")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_copy = gray_img.copy()
thresh_img = threshold(gray_img, 127)
mean_thresh = adaptive_threshold_mean_c(gray_copy)
cv2.imshow("Mean Thresh", mean_thresh)
cv2.imshow("Thresh", thresh_img)

cv2.waitKey(0)