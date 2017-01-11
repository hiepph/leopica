import time
import logging
import picamera
from upload import Upload
from redis import Redis
from rq import Queue

logging.basicConfig(format='[%(asctime)s] %(levelname)s ($%(name)s) - %(message)s',
                    level=logging.DEBUG)

def shoot_and_upload_images(uploader, delay=5):
    with picamera.PiCamera() as camera:
        logging.info("Setting up camera.")

        # veritcal flip
        camera.vflip = True

        # 1s shutter speed
        camera.shutter_speed = 1000000

        # camera.start_preview()

        # Wait for the automatic gain control to settle
        time.sleep(5)
        
        logging.info("Start photographing!")
        # Start capturing continuosly
        for image in camera.capture_continuous('images/img-{timestamp:%Y-%m-%d-%H:%M:%S}.jpg'):
            logging.info("Captured %s" % image)
            q.enqueue(upload.upload_to_drive, image)
            time.sleep(delay)

if __name__ == "__main__":
    q = Queue(connection=Redis())
    
    logging.info("Login to Drive Account")
    upload = Upload()

    shoot_and_upload_images(upload)
