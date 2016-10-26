from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

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

test_image = drive.CreateFile()
test_image.SetContentFile('images/test.jpg')
test_image.Upload()
print('Uploaded image: \n\ttitle: %s,\n\tmimeType: %s' %
      (test_image['title'], test_image['mimeType']))
