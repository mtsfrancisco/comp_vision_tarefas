import cv2 
import matplotlib.pyplot as plt

image = cv2.imread("images/image1.webp")
image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
height, width = image.shape[:2]
nRows = height//4
mCols = width//4
gradients = []

for i in range(4):
    for j in range(4):
        y_start = i*nRows
        y_end = (i+1)*nRows
        x_start = j*mCols
        x_end = (j+1)*mCols

        block = image[y_start:y_end, x_start:x_end]
        sobel_x = cv2.Sobel(block, cv2.CV_64F, 1, 0, ksize=3)
        sobel_y = cv2.Sobel(block, cv2.CV_64F, 0, 1, ksize=3)
        gradient_magnitude = cv2.magnitude(sobel_x, sobel_y)
        gradients.append(gradient_magnitude)

fig, axs = plt.subplots(4, 4)
fig.suptitle('Divisão da Imagem em Blocos 4x4')
for i in range(4):
    for j in range(4):
        axs[i, j].imshow(gradients[i*4+j], cmap='gray')
        axs[i, j].axis('off')
plt.show()



