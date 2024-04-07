import cv2
import pymeanshift as pms

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

    (segmented_image, labels_image, number_regions) = pms.segment(
        frame, spatial_radius=2, range_radius=2, min_density=50)

    cv2.imshow('Segmented', segmented_image)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
cap.release()