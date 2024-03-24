import cv2

W = 320
H = 240

# Assuming video capture from a webcam (replace with your video source)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,2*W)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,2*H)

# Handle potential errors (e.g., invalid camera index)
if not cap.isOpened():
    print("Error opening video capture")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Process the frame here (may not need position information)

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()