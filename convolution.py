import cv2
import numpy as np
import matplotlib.pyplot as plt

kernel = np.array([[1, 0, -1],
                     [1, 0, -1],
                     [1, 0, -1]])


def convoluton(img, kernel):
    height, width = img.shape[:2]
    k_height, k_width = kernel.shape[:2]
    pad = k_width // 2
    img_copy = np.zeros((height + 2 * pad, width + 2 * pad))
    kernel = cv2.flip(kernel, -1)

    for i in range(pad, height - pad):
        for j in range(pad, width - pad):
            sum = 0
            for m in range(k_height):
                for n in range(k_width):
                    sum += int(img[i - pad + m, j - pad + n]) * int(kernel[m, n])
            if sum > 255:
                img_copy[i, j] = 255
            elif sum < 0:
                img_copy[i, j] = 0
            else:
                img_copy[i, j] = sum

    return img_copy.astype(np.uint8)

img = cv2.imread("images/image1.webp")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_copy = gray_img.copy()

conv_img = convoluton(gray_img, kernel)
opencv_conv = cv2.filter2D(gray_copy, -1, kernel)

#histo = cv2.calcHist([conv_img], [0], None, [256], [0, 256])

cv2.imshow("OpenCV", opencv_conv)
cv2.imshow("Imagem", conv_img)

#plt.plot(histo, color='gray')
#plt.show()
cv2.waitKey(0)

