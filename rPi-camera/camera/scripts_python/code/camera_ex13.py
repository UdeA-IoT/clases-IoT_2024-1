import time
import picamera

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    camera.capture_sequence([
        'sec_image1.jpg',
        'sec_image2.jpg',
        'sec_image3.jpg',
        'sec_image4.jpg'
        ], use_video_port=True)
    camera.stop_preview()
