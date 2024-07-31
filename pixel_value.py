import cv2
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
print(blank[10, 10])


def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Left button clicked at ({x}, {y})")
        print(f"Pixel value at ({x}, {y}): {image[y, x]}")
        r,g,b = image[y, x]
        blank[:] = image[y, x]
        altura, largura = blank.shape[:2]

        cv2.putText(blank, f"R: {r}, G: {g}, B: {b}", (0, altura//2), cv2.FONT_HERSHEY_COMPLEX, 1, (255-int(r),255-int(g),255-int(b)), 1)
        cv2.imshow('Cor', blank)
        #cv2.waitKey(0)


cv2.namedWindow('Image')


cv2.setMouseCallback('Image', mouse_callback)


image = cv2.imread('imagens/image1.webp')

while True:
    cv2.imshow('Image', image)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  #ESC
        break

cv2.destroyAllWindows()