import cv2

img = cv2.imread('jelly_beans.tiff', 0)
negative = abs(255 - img)
cv2.imshow('Grayscale', img)
cv2.imshow('Negative', negative)
cv2.waitKey(0)
cv2.destroyAllWindows()