import time
import os
import picamera

camera = picamera.PiCamera()
camera.start_preview()
# camera warm-up time
time.sleep(3)
camera.capture(os.path.join(os.getcwd(), 'images', 'test.jpg'))
