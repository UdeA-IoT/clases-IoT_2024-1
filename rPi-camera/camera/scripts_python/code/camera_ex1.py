from picamera import PiCamera
from time import sleep
cam = PiCamera()
try:
    cam.start_recording('vid.h264')
    sleep(5)
    cam.stop_recording()
finally:
    cam.close()