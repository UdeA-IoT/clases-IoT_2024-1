import cv2
import numpy as np

W = 320
H = 240

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,2*W)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,2*H)
fgbg = cv2.createBackgroundSubtractorKNN()

if not cap.isOpened():
    print("Error opening video capture")
    exit()

while(True):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    cv2.imshow('frame', fgmask)
    if cv2.waitKey(30) == 27:
        break
cap.release()
cv2.destroyAllWindows()