#! /usr/bin/python3

import time
import os
import picamera
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

import telegram
import logging

bot = telegram.Bot(token=open('telegram.token').read().rstrip())
logging.basicConfig(format='%(asctime)s - %(name)s \
                    - %(levelname)s - %(message)s', level=logging.INFO)

RECIPIENT_ID = 226142487


def telegram_notify(bot, log):
    bot.sendMessage(chat_id=RECIPIENT_ID, text=log)


def telegram_send_photo(bot, image):
    bot.sendPhoto(chat_id=RECIPIENT_ID, photo=open(image, 'rb'))


def login():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(".credential")
    if gauth.credentials is None:
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        os.system("rm .credential")
        login()
    else:
        gauth.Authorize()
    gauth.SaveCredentialsFile(".credential")

    global drive
    drive = GoogleDrive(gauth)


def init_camera():
    global camera
    camera = picamera.PiCamera()


def shoot_picture(image_name):
    camera.start_preview()
    time.sleep(5)

    image = 'images/%s.jpg' % image_name
    camera.capture(image)

    camera.stop_preview()
    telegram_send_photo(bot, image)
    return image


def upload_to_drive(image):
    image_title = os.path.basename(image)
    log = "INFO Uploading %s..." % image_title
    print(log)
    telegram_notify(bot, log)

    staged_image = drive.CreateFile({'title': image_title})
    staged_image.SetContentFile(image)
    staged_image.Upload()
    log = "INFO Uploaded image: { title: %s, mimeType: %s }" % \
           (staged_image['title'], staged_image['mimeType'])
    print(log)
    telegram_notify(bot, log)


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
