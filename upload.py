from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

class Upload:
    def __init__(self):
        self.drive = self.login_to_drive()

    def login_to_drive(self):
        gauth = GoogleAuth()
        gauth.LoadCredentialsFile(".credential")
        if gauth.credentials is None:
            gauth.LocalWebserverAuth()
        elif gauth.access_token_expired:
            gauth.Refresh()
        else:
            gauth.Authorize()
        gauth.SaveCredentialsFile(".credential")

        return GoogleDrive(gauth)

    def upload_to_drive(self, image):
        image_title = os.path.basename(image)

        staged_image = self.drive.CreateFile({'title': image_title})
        staged_image.SetContentFile(image)
        staged_image.Upload()
