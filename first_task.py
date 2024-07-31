import cv2
import matplotlib.pyplot as plt
import numpy as np

def calc_hist(img):
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    plt.plot(hist, color='gray')
    plt.show()


def mudar_intensidade(img):
    altura, largura = img.shape
    intensidade = input("Digite o valor: ")

    for i in range(altura):
        for j in range(largura):
            nova_intensidade = int(img[i, j]) + int(intensidade)
            if (nova_intensidade > 255):
                nova_intensidade = 255
            elif (nova_intensidade < 0):
                nova_intensidade = 0
            img[i, j] = nova_intensidade

    cv2.imshow("Imagem", img)
    cv2.waitKey(0)


def inverter_intensidade(img):
    altura, largura = img.shape

    for i in range(altura):
        for j in range(largura):
            img[i, j] = 255 - int(img[i, j])

    cv2.imshow("Imagem", img)
    cv2.waitKey(0)



img = cv2.imread(r"imagens\image1.webp")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(gray_img.shape)

cv2.imshow("Imagem", gray_img)
cv2.waitKey(0)

calc_hist(gray_img)

mudar_intensidade(gray_img)
inverter_intensidade(gray_img)



