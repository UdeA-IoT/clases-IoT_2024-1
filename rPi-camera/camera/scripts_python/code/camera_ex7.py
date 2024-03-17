import time
import picamera

with picamera.PiCamera() as camera:
  camera.start_preview()
  camera.image_effect = 'colorswap'
  time.sleep(5)
  camera.capture('/home/tigarto/Desktop/colorswap.jpg', use_video_port=True)
  camera.stop_preview()
