#(hMin = 0 , sMin = 0, vMin = 0), (hMax = 179 , sMax = 117, vMax = 255)

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

def process_image(img):
    kernel = np.ones((5,5),np.uint8)
    image = cv.medianBlur(img, 5)
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    binary_image = cv.threshold(image, 40, 255, cv.THRESH_BINARY_INV)[1]

    binary_image = cv.dilate(binary_image, kernel, iterations=2)
    binary_image = cv.medianBlur(binary_image, 5)

    return binary_image

def process_template(img):
    kernel = np.ones((5,5),np.uint8)
    image = cv.medianBlur(img, 5)
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    binary_image = cv.threshold(image, 40, 255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)[1]

    return binary_image


template = cv.imread('tarefa_02.04/images/coin_template.png')
processed_template = process_template(template)
cv.imshow('template', processed_template)
cv.waitKey(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    image = process_image(frame)

    res = cv.matchTemplate(image,processed_template,cv.TM_CCOEFF_NORMED)
    cv.imshow("res", res)
    cv.waitKey(0)

    threshold = 0.7
    loc = np.where( res >= threshold )
    if loc:
        for pt in zip(*loc[::-1]):
            cv.rectangle(frame, pt, (pt[0], pt[1]), (0,0,255), 2)

    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()