from picamera import PiCamera
from time import sleep
   
with PiCamera() as camera:
    camera.start_preview()
    sleep(10)
    camera.stop_preview()
