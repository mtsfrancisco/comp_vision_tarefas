import cv2
import numpy as np
import matplotlib.pyplot as plt


def adaptive_threshold_mean_c(image, tamanho_bloco=11, c=2):

    altura, largura = image.shape
    thresholded = np.zeros_like(image)
    meio_bloco = tamanho_bloco // 2
    
    for i in range(altura):
        for j in range(largura):
            
            top = max(0, i - meio_bloco)
            bottom = min(altura - 1, i + meio_bloco)
            left = max(0, j - meio_bloco)
            right = min(largura - 1, j + meio_bloco)
            media_bloco = np.mean(image[top:bottom+1, left:right+1])

            if image[i, j] > media_bloco - c:
                thresholded[i, j] = 255
            else:
                thresholded[i, j] = 0
        
    return thresholded

def threshold(img, thresh):

    altura, largura = img.shape

    for i in range(altura):
        for j in range(largura):
            if img[i, j] > thresh:
                img[i, j] = 255
            else:
                img[i, j] = 0

    return img

img = cv2.imread("imagens/image1.webp")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_copy = gray_img.copy()
thresh_img = threshold(gray_img, 127)
mean_thresh = adaptive_threshold_mean_c(gray_copy)
cv2.imshow("Mean Thresh", mean_thresh)
cv2.imshow("Thresh", thresh_img)

cv2.waitKey(0)