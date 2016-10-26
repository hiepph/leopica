import time
import os
import picamera
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


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
    global camera
    camera = picamera.PiCamera()
    camera.start_preview()
    time.sleep(3)


def shoot_picture(image_name):
    image = 'images/%s.jpg' % image_name
    camera.capture(image)
    return image


def upload_to_drive(image):
    image_title = os.path.basename(image)
    staged_image = drive.CreateFile({'title': image_title})
    staged_image.SetContentFile(image)
    staged_image.Upload()
    print('INFO Uploaded image: { title: %s, mimeType: %s }' %
          (staged_image['title'], staged_image['mimeType']))


def shoot_and_upload_images():
    i = 1
    while True:
        image_name = 'lepica-%d' % i
        image = shoot_picture(image_name)
        upload_to_drive(image)

        time.sleep(5)
        i += 1

if __name__ == "__main__":
    login()
    init_camera()
    shoot_and_upload_images()
