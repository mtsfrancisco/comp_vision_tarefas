import cv2
import numpy as np



def grayScale(img):
    altura, largura = img.shape[:2]
    img_copy = np.zeros((altura, largura))

    for i in range(altura):
        for j in range(largura):
            cor = img[i, j]
            img_copy[i, j] = 0.2989 * cor[2] + 0.5870 * cor[1] + 0.1140 * cor[0]

    return img_copy.astype(np.uint8)

img = cv2.imread("imagens/image1.webp")
gray = grayScale(img)

rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
cv2.imshow("RGB", rgb)
cv2.imshow("Gray", gray)
cv2.waitKey(0)