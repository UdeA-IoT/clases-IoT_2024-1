from picamera import PiCamera
from time import sleep

with PiCamera() as pycam:
    pycam.start_preview()
    for effect in pycam.IMAGE_EFFECTS:
       pycam.image_effect = effect
       pycam.annotate_text = "Effect: %s" % effect
       sleep(5)
    pycam.stop_preview()
