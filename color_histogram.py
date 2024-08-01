import matplotlib.pyplot as plt
import cv2

img = cv2.imread("images/image1.webp")
chans = cv2.split(img)
colors = ("b", "g", "r")
print(img.shape)
plt.figure()
plt.title("Histograma de Cores")
plt.xlabel("Bins")
plt.ylabel("# de Pixels")

for (chan, color) in zip(chans, colors):
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])

plt.show()