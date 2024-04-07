import cv2
img1 = cv2.imread('mandrill.tiff', 1)
img2 = cv2.imread('airplane_f16.tiff', 1)
cv2.imshow('NumPy Subtract', img1 - img2 )
cv2.imshow('OpenCV Subtract', cv2.subtract(img1, img2))
cv2.waitKey(0)
cv2.destroyAllWindows()