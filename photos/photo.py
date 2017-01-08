import time
import logging
import picamera
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

logging.basicConfig(format='[%(asctime)s] %(levelname)s ($%(name)s) - %(message)s',
                    level=logging.DEBUG)

def login():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(".credential")
    if gauth.credentials is None:
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
    gauth.SaveCredentialsFile(".credential")

    global drive
    drive = GoogleDrive(gauth)

def upload_to_drive(image):
    image_title = os.path.basename(image)

    staged_image = drive.CreateFile({'title': image_title})
    staged_image.SetContentFile(image)
    staged_image.Upload()
    logging.info("Uploaded image: { title: %s, mimeType: %s }",
                 staged_image['title'], staged_image['mimeType'])

def shoot_and_upload_images(delay=5):
    with picamera.PiCamera() as camera:
        # 1s shutter speed
        camera.shutter_speed = 1000000
        camera.start_preview()

        # Wait for the automatic gain control to settle
        time.sleep(5)
        
        # Start capturing continuosly
        for image in camera.capture_continuous('images/img-{timestamp:%Y-%m-%d-%H-%M-%S}.jpg'):
            logging.info("Captured %s" % image)
            time.sleep(delay)

if __name__ == "__main__":
    login()
    shoot_and_upload_images(1)
