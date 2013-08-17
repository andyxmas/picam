#!/usr/bin/env python

import os
import datetime
import subprocess
import togdrive
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
        with open(filename):
            togdrive.upload_to_gdrive(
                filename,
                filename,
                'photo taken using the raspberry pi camera module',
                'image/jpeg'
            )
    except IOError:
        print 'Oh dear.'

take_single_photo()
