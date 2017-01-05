import time
import os
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

def init_camera():
    logging.info("Init camera")
    global camera
    camera = picamera.PiCamera()

def shoot_picture(image_name):
    camera.start_preview()
    time.sleep(1) # @todo: Change to 5s in production

    image = 'images/%s.jpg' % image_name
    camera.capture(image)

    camera.stop_preview()
    return image

def upload_to_drive(image):
    image_title = os.path.basename(image)

    staged_image = drive.CreateFile({'title': image_title})
    staged_image.SetContentFile(image)
    staged_image.Upload()
    logging.info("Uploaded image: { title: %s, mimeType: %s }",
                 staged_image['title'], staged_image['mimeType'])

def shoot_and_upload_images():
    i = 1
    while True:
        image_name = 'leopica-%d' % i
        image = shoot_picture(image_name)
        upload_to_drive(image)

        i += 1

if __name__ == "__main__":
    login()
    init_camera()
    shoot_and_upload_images()
