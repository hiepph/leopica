import picamera

with picamera.PiCamera() as camera:
    camera.start_recording('test.h264')
    camera.wait_recording(60)
    camera.stop_recording()
