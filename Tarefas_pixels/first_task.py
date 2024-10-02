import cv2
import matplotlib.pyplot as plt
import numpy as np

def calc_hist(img):
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    plt.plot(hist, color='gray')
    plt.show()


def change_intensity(img):
    height, width = img.shape
    intensity = input("Value: ")

    for i in range(height):
        for j in range(width):
            new_intensity = int(img[i, j]) + int(intensity)
            if (new_intensity > 255):
                new_intensity = 255
            elif (new_intensity < 0):
                new_intensity = 0
            img[i, j] = new_intensity

    cv2.imshow("Image", img)
    cv2.waitKey(0)


def invert_intensity(img):
    height, width = img.shape

    for i in range(height):
        for j in range(width):
            img[i, j] = 255 - int(img[i, j])

    cv2.imshow("Imagem", img)
    cv2.waitKey(0)



img = cv2.imread("image\image1.webp")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(gray_img.shape)

cv2.imshow("Image", gray_img)
cv2.waitKey(0)

calc_hist(gray_img)

change_intensity(gray_img)
invert_intensity(gray_img)



