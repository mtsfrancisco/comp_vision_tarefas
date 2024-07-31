import cv2
import numpy as np
import matplotlib.pyplot as plt

kernel = np.array([[1, 0, -1],
                     [1, 0, -1],
                     [1, 0, -1]])


def convolucao(img, kernel):
    altura, largura = img.shape[:2]
    k_altura, k_largura = kernel.shape[:2]
    pad = k_largura // 2
    img_copy = np.zeros((altura + 2 * pad, largura + 2 * pad))
    kernel = cv2.flip(kernel, -1)

    for i in range(pad, altura - pad):
        for j in range(pad, largura - pad):
            soma = 0
            for m in range(k_altura):
                for n in range(k_largura):
                    soma += int(img[i - pad + m, j - pad + n]) * int(kernel[m, n])
            if soma > 255:
                img_copy[i, j] = 255
            elif soma < 0:
                img_copy[i, j] = 0
            else:
                img_copy[i, j] = soma

    #return img_copy.astype(np.uint8)
    return img_copy

img = cv2.imread("imagens/image1.webp")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_copy = gray_img.copy()

conv_img = convolucao(gray_img, kernel)
opencv_conv = cv2.filter2D(gray_copy, -1, kernel)

#histo = cv2.calcHist([conv_img], [0], None, [256], [0, 256])

cv2.imshow("OpenCV", opencv_conv)
cv2.imshow("Imagem", conv_img)

#plt.plot(histo, color='gray')
#plt.show()
cv2.waitKey(0)

