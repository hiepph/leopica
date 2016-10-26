from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

"""
Google Drive authentication

Create a '.credential' authen file for automatically authen next time
"""
gauth = GoogleAuth()
gauth.LoadCredentialsFile(".credential")
if gauth.credentials is None:
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()
gauth.SaveCredentialsFile(".credential")

"""
Have fun with files and images
"""
drive = GoogleDrive(gauth)

test_image = 'images/test.jpg'
test_image_name = os.path.basename(test_image)
staged_image = drive.CreateFile({'title': test_image_name})
staged_image.SetContentFile('images/test.jpg')
staged_image.Upload()
print('Uploaded image: \n\ttitle: %s,\n\tmimeType: %s' %
      (staged_image['title'], staged_image['mimeType']))
