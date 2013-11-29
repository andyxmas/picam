#! /usr/bin/env python

import time
import datetime
import requests
import xml.etree.ElementTree as ET
from dateutil.parser import *


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
    current_time = time.time()
    sunrise = get_daylight_hours()['sunrise'].time()
    sunset = get_daylight_hours()['sunset'].time()

    # print "sunrise:", sunrise
    # print "sunset:", sunset
    # print "current time:", current_time

    rise_time = time.strptime(str(sunrise), "%H:%M:%S")
    set_time = time.strptime(str(sunset), "%H:%M:%S")

    # print "rise_time:", rise_time
    # print "set_time:", set_time

    if (current_time > rise_time) and (current_time < set_time):
        return True
    else:
        return False
