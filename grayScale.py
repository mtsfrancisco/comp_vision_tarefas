import cv2
import numpy as np


def grayToRgb(gray):
    altura, largura = gray.shape[:2]
    img_copy = np.zeros((altura, largura, 3))
    print(img_copy[0,0])
    for i in range(altura):
        for j in range(largura):
                color = gray[i, j]
                img_copy[i, j] = [color, color, color]

    return img_copy.astype(np.uint8)

def grayScale(img):
    altura, largura = img.shape[:2]
    img_copy = np.zeros((altura, largura))

    for i in range(altura):
        for j in range(largura):
            cor = img[i, j]
            img_copy[i, j] = 0.2989 * cor[2] + 0.5870 * cor[1] + 0.1140 * cor[0]

    return img_copy.astype(np.uint8)

img = cv2.imread("imagens/image1.webp")
img_copy = img.copy()
gray_copy = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)

gray = grayScale(img)
rgb_gray = grayToRgb(gray_copy)

rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

cv2.imshow("RGB Gray", rgb_gray)
cv2.imshow("RGB", rgb)
cv2.imshow("Gray", gray)
cv2.waitKey(0)