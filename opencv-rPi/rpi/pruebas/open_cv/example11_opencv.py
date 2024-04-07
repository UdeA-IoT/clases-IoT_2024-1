import cv2

img1 = cv2.imread('mandrill.tiff', 1)
img2 = cv2.imread('airplane_f16.tiff', 1)
cv2.imshow('Blended Image',
           cv2.addWeighted(img1, 0.5, img2, 0.5, 0))
cv2.waitKey(0)
cv2.destroyAllWindows()