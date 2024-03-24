import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('female1.tiff', 0)
print(type(img1))
print(img1.ndim)
print(img1.shape)
print(img1.size)
print(img1.dtype)
print(img1.nbytes)

cv2.waitKey(0)

img2 = cv2.imread('female1.tiff', 1)
print(type(img2))
print(img2.ndim)
print(img2.shape)
print(img2.size)
print(img2.dtype)
print(img2.nbytes)

