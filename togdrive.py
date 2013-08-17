#!/usr/bin/python

import httplib2
import pprint

from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow

def upload_to_gdrive(filename, title, description, mimetype):
    # Copy your credentials from the APIs Console
    CLIENT_ID = '212389205932-vvu68uk99iqi08ohq23ml078291df44k.apps.googleusercontent.com'
    CLIENT_SECRET = 'QJ83TKO_ctEZuQB_1W7uuwO5'

    # Check https://developers.google.com/drive/scopes for all available scopes
    OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'

    # Redirect URI for installed apps
    REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

    # Path to the file to upload
    # FILENAME = 'document.txt'

    # Run through the OAuth flow and retrieve credentials
    flow = OAuth2WebServerFlow(
        CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)
    authorize_url = flow.step1_get_authorize_url()
    print 'Go to the following link in your browser: ' + authorize_url
    code = raw_input('Enter verification code: ').strip()
    credentials = flow.step2_exchange(code)

    # Create an httplib2.Http object and authorize it with our credentials
    http = httplib2.Http()
    http = credentials.authorize(http)

    drive_service = build('drive', 'v2', http=http)

    # Insert a file
    media_body = MediaFileUpload(filename, mimetype=mimetype, resumable=True)
    body = {
        'title': title,
        'description': description,
        'mimeType': mimetype
    }

    file = drive_service.files().insert(
        body=body, media_body=media_body).execute()
    pprint.pprint(file)