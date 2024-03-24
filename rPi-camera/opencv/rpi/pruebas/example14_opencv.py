import cv2

img1 = cv2.imread('female3.tiff', 1)
img2 = cv2.imread('house.tiff', 1)
cv2.imshow('Image1', img1 * 2)
cv2.waitKey(0)
cv2.destroyAllWindows()