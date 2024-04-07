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

frame_count = 0  # Track frame count manually (if needed)
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Process the frame here
    # You might use timestamps or frame_count for timing-related operations

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

    # Update frame count (if you're manually tracking it)
    frame_count += 1
    print(frame_count)

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()