import numpy as np
import cv2

W = 320
H = 240

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error opening video capture")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH,W)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,H)

while ( True ):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    image_mask = cv2.inRange(hsv, np.array([40, 50, 50]),
    np.array([80, 255, 255]))
    output = cv2.bitwise_and(frame, frame,mask=image_mask)
    cv2.imshow('Original', frame)
    cv2.imshow('Output', output)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
cap.release()