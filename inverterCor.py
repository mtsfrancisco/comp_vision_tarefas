import cv2
import numpy as np


def inverter_cor(img):
    altura, largura = img.shape[:2]
    img_copy = img.copy()

    for i in range(altura):
        for j in range(largura):
            cor = img[i, j]
            for k in range(3):
                cor[k] = 255 - cor[k]
            img_copy[i, j] = cor

    return img_copy

image = cv2.imread('imagens/image1.webp')
image2 = image.copy()
image_invertida = inverter_cor(image)

image2 = cv2.bitwise_not(image2)
cv2.imshow('Funcao bitwise_not', image2)

cv2.imshow('Funcao inverter_cor', image_invertida)
cv2.waitKey(0)