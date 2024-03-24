import cv2
from time import sleep

W = 320
H = 240

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error opening video capture")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH,W)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,H)

ret, frame = cap.read()
rows, cols, channels = frame.shape
angle = 0
while(1):
    ret, frame = cap.read()
    if angle == 360:
        angle = 0
    M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
    rotated = cv2.warpAffine(frame, M, (cols, rows))
    cv2.imshow('Rotating Image', rotated)
    angle = angle +1
    sleep(0.2)
    if cv2.waitKey(1) == 27 :
        break
cv2.destroyAllWindows()