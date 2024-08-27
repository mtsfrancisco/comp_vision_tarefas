import cv2
import numpy as np
import matplotlib.pyplot as plt


 
img = cv2.imread('images/image1.webp')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
gradient_magnitude = np.sqrt(sobelx**2.0 + sobely**2.0)

cv2.imshow('Gradient', sobelx)
cv2.waitKey(0)

gray_values = gray.ravel()
gradient_values = gradient_magnitude.ravel()


plt.hist2d(gray_values, gradient_values, bins=20, cmap="viridis")
plt.colorbar()
plt.xlabel('Intensidade (Gray Scale)')
plt.ylabel('Magnitude do Gradiente')
plt.title('Histograma 2D: Intensidade vs Gradiente')
plt.show()

