from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
try: 
  for i in range(5):
    sleep(2)
    camera.capture('/home/tigarto/Documents/image%s.jpg' % i,use_video_port=True)
    camera.stop_preview()
finally:
  camera.close() 
