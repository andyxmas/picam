#!/usr/bin/env python

import os
import datetime
import subprocess
import upload
import daylight
import time


def take_single_photo():
    # Create unique filename based on time and date
    utc_datetime = datetime.datetime.now()
    nicetime = utc_datetime.strftime("%Y-%m-%d-%H%M")

    # define the command
    filename = nicetime + '.jpg'

    # set the options to use
    options = ['-w 500',  # width 500px
               '-h 500',  # height 500px
               '-q 80',  # jpg quality to 80
               '-rot 180']  # rotate image 180 degrees

    cmd = 'raspistill -o ' + filename + ' ' + ' '.join(options)
    print "Executing: ", cmd

    # how the hell does this run it!!?? you need to learn this!!!!!
    pid = subprocess.call(cmd, shell=True)

    time.sleep(10)
    try:
        upload.upload_image(filename)
        print("upload successful.")
    except IOError:
        print 'Oh dear.'

if daylight.is_daylight():
    take_single_photo()

else:
    print "It's too dark to take a photo..."
