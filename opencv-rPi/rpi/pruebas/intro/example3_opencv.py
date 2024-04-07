import cv2
import matplotlib.pyplot as plt

img = cv2.imread('mandrill.tiff', 0)
plt.imshow(img, cmap='gray')
plt.title('Mandrill')
plt.axis('off')
plt.show()