#!/usr/bin/env python

import os
import datetime
import subprocess


def take_single_photo():
    # Create unique filename based on time and date
    utc_datetime = datetime.datetime.utcnow()
    filename = utc_datetime.strftime("%Y-%m-%d-%H%M")

    #define the command
    cmd = 'raspistill -o ' + filename + '.jpg'
    print cmd

    #how the hell does this run it!!?? you need to learn this!!!!!
    pid = subprocess.call(cmd, shell=True)

take_single_photo()


