#! /usr/bin/python
# Originally Written by Peter Nichols 
# planzero.org/blog/2012/04/13/uploading_any_file_to_google_docs_with_python
#
# Adapted by Andy Christmas to be used for uploading images from the
# raspberry pi camera module to gdrive.

import sys
import time
import os.path
import atom.data
import gdata.client
import gdata.docs.client
import gdata.docs.data
import logging

# configure where log file should be recorded
# logging.basicConfig(filename='picam_upload.log',level=logging.DEBUG)

def upload_image(filename):
    '''uploads an image to google drive'''
    #google account login details
    username = 'andy.christmas'
    password = 'gdomiaveobimsfsm'

    #settings
    file_type = 'image/jpeg'
    collection = 'picam'

    # Start the Google Drive Login
    docsclient = gdata.docs.client.DocsClient(source='RPi Python-GData 2.0.17')

    # Get a list of all available resources (GetAllResources() requires >=
    # gdata-2.0.15)
    # nb, this isnt required, but good login check and worth keeping?
    logging.info('Logging in to google drive...')
    try:
        docsclient.ClientLogin(username, password, docsclient.source)
    except (gdata.client.BadAuthentication, gdata.client.Error), e:
        logging.debug('Unknow Error: ' + str(e))
        sys.exit('Unknown Error: ' + str(e))
    except:
        sys.exit('Login Error, perhaps incorrect username/password')
        logging.debug('Login Error, perhaps incorrect username/password')
    
    logging.info('Login succesful.')

    # The default root collection URI
    uri = 'https://docs.google.com/feeds/upload/create-session/default/private/full'
    # Get a list of all available resources (GetAllResources() requires >=
    # gdata-2.0.15)
    logging.info('Fetching Collection/Directory ID...')
    try:
        resources = docsclient.GetAllResources(
            uri='https://docs.google.com/feeds/default/private/full/-/folder?title=' + collection + '&title-exact=true')
    except:
        sys.exit('ERROR: Unable to retrieve resources')
        logging.warning('ERROR: Unable to retrieve resources')
    # If no matching resources were found
    if not resources:
        sys.exit('Error: The collection "' + collection + '" was not found.')
        logging.warning('Error: The collection "' + collection + '" was not found.')
    # Set the collection URI
    uri = resources[0].get_resumable_create_media_link().href
    
    # Make sure Google doesn't try to do any conversion on the upload (e.g.
    # convert images to documents)
    uri += '?convert=false'

    fhandle = open(filename)
    file_size = os.path.getsize(fhandle.name)
    
    # Create an uploader and upload the file
    uploader = gdata.client.ResumableUploader(
        docsclient, fhandle, file_type, file_size, chunk_size=1048576, desired_class=gdata.data.GDEntry)
    try:
        new_entry = uploader.UploadFile(uri, entry=gdata.data.GDEntry(
            title=atom.data.Title(text=os.path.basename(fhandle.name))))
        logging.info('uploaded successfully to gdrive.')
    except:
        logging.debug('upload to gdrive appears to have failed at the last :-(')
