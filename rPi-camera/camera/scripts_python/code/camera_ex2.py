from picamera import PiCamera
from time import sleep
   
camera = PiCamera()
try:
    camera.start_preview()
    sleep(10)
    camera.stop_preview()
finally:
    camera.close() # El close se usa para limpiar recursos