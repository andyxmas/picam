#!/usr/bin/env python

import os
import datetime
import subprocess
import upload
import time


def take_single_photo():
    # Create unique filename based on time and date
    utc_datetime = datetime.datetime.utcnow()
    nicetime = utc_datetime.strftime("%Y-%m-%d-%H%M")

    # define the command
    filename = nicetime + '.jpg'
    cmd = 'raspistill -o ' + filename
    print cmd

    # how the hell does this run it!!?? you need to learn this!!!!!
    pid = subprocess.call(cmd, shell=True)

    time.sleep(10)
    try:
        upload.upload_image(filename)
    except IOError:
        print 'Oh dear.'

take_single_photo()
