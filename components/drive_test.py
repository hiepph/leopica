from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
gauth.LoadCredentialsFile(".credential")
if gauth.credentials is None:
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()

gauth.SaveCredentialsFile(".credential")
