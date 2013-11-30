#! /usr/bin/env python

import time
import datetime
import requests
import xml.etree.ElementTree as ET
from dateutil.parser import *
# import logging

def get_daylight_hours():
    """using openweathermap, get sunrise and sunset times"""
    f = open('/home/andy/repos/picam/weather.xml', 'r')
    tree = ET.parse(f)
    root = tree.getroot()
    f.close()

    # if root == "":
    #    baseurl = "http://api.openweathermap.org/data/2.5/weather"
    #    query = "?q=salhouse&mode=xml"
    #    url = baseurl + query
    #    r = requests.get(url)
    #    root = ET.fromstring(r.text)
    #    print "got xml from api"

    sunrise = parse(root[0][2].attrib.get('rise'))
    sunset = parse(root[0][2].attrib.get('set'))
    daylight_hours = {'sunrise': sunrise, 'sunset': sunset}
    return daylight_hours


def is_daylight():
    current = datetime.datetime.now().time()
    sunrise = get_daylight_hours()['sunrise'].time()
    sunset = get_daylight_hours()['sunset'].time()

# convert the xml string into an actual date/time
    rise_datetime = time.strptime(str(sunrise), "%H:%M:%S")
    set_datetime = time.strptime(str(sunset), "%H:%M:%S")

#get just the hours minutes and seconds of the date/times
    current_time = time.strftime("%H:%M:%S")
    rise_time = time.strftime("%H:%M:%S", rise_datetime)
    set_time = time.strftime("%H:%M:%S", set_datetime)

#    logging.info("current_time:", current_time)
#    logging.info("rise_time:", rise_time)
#    logging.info("set_time:", set_time)

    if (current_time > rise_time) and (current_time < set_time):
#        logging.info("currently daylight")
        return True
    else:
#        logging.info("the sun is set")
        return False

