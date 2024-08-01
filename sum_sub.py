import cv2

def sum(img, img2):

    height, width = img.shape

    for i in range(height):
        for j in range(width):
            sum = int(img[i,j]) + int(img2[i,j])
            if sum > 255:
                img[i, j] = 255
            elif sum < 0:
                img[i, j] = 0
            else:
                img[i, j] = sum

    return img

def sub(img, img2):
    height, width = img.shape

    for i in range(height):
        for j in range(width):
            sub = int(img[i,j]) - int(img2[i,j])
            if sub > 255:
                img[i, j] = 255
            elif sub < 0:
                img[i, j] = 0
            else:
                img[i, j] = sub
    return img

img = cv2.imread("images\image1.webp")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray_copy = gray_img.copy()
gray_img = cv2.resize(gray_img, (500, 500))
gray_copy = cv2.resize(gray_copy, (500, 500))

img2 = cv2.imread("images\image2.webp")
gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

gray_copy2 = gray_img2.copy()
gray_img2 = cv2.resize(gray_img2, (500, 500))
gray_copy2 = cv2.resize(gray_copy2, (500, 500))

soma_img = sum(gray_img, gray_img2)
sub_img = sub(gray_copy, gray_copy2)

cv2.imshow("Sum", soma_img)
cv2.imshow("Sub", sub_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
