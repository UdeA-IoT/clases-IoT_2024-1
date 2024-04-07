import cv2
import time
import numpy as np

img1 = cv2.imread('mandrill.tiff', 1)
img2 = cv2.imread('airplane_f16.tiff', 1)

for i in np.linspace(0, 1, 100):
    alpha = i
    beta = 1-alpha
    print('ALPHA =' + str(alpha) + ' BETA =' + str(beta))
    cv2.imshow('Image Transition',
               cv2.addWeighted(img1, alpha, img2, beta, 0))
    time.sleep(0.05)
    if cv2.waitKey(1) == 27 :
        break
cv2.destroyAllWindows()