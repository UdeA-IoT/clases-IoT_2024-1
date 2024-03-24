import cv2
import numpy as np

def maxRGB(img):
    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]

    M = np.maximum(np.maximum(b, g), r)

    b[b < M] = 0
    g[g < M] = 0
    r[r < M] = 0

    return(cv2.merge((b, g, r)))

W = 320
H = 240

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error opening video capture")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH,W)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,H)

while True:
    ret, frame = cap.read()
    cv2.imshow('Max RGB Filter', maxRGB(frame))
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
cap.release()