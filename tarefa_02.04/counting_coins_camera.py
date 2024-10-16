import cv2 as cv
import numpy as np
from scipy.ndimage import label, find_objects

capture = cv.VideoCapture(0)
kernel = np.ones((5,5),np.uint8)
structure = np.ones((3, 3), dtype=int)

while True:
    ret, frame = capture.read()
    if not ret:
        break

    image = cv.medianBlur(frame, 5)
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    binary_image = cv.threshold(image, 40, 255, cv.THRESH_BINARY_INV)[1]

    binary_image = cv.dilate(binary_image, kernel, iterations=2)
    binary_image = cv.medianBlur(binary_image, 5)

    cv.imshow('binary_image', binary_image)
    cv.waitKey(0)

    rotulos, num_objects = label(binary_image, structure=structure)

    objs = find_objects(rotulos)
    for i, obj in enumerate(objs):
        if obj is not None:
            y, x = obj
            cv.rectangle(frame, (x.start, y.start), (x.stop, y.stop), (0, 255, 0), 2)


    cv.putText(frame, f'Number of coins: {num_objects}', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv.imshow('frame', frame)
    #print(f'Number of coins: {num_objects}')
    #cv.imshow('Rotulos', rotulos)
    #rotulos = rotulos.astype(np.uint8)
    #im_color = cv.applyColorMap(rotulos, cv.COLORMAP_JET)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break