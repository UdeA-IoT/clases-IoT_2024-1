import cv2
import matplotlib.pyplot as plt

img = cv2.imread('female1.tiff', 1)
print(img[10, 10])
print(img[10, 10, 0])

cv2.waitKey(0)
b, g, r = cv2.split(img)
b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]

cv2.waitKey(0)
img1 = cv2.merge((b, g, r))


