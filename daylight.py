#! /usr/bin/env python

import time
import datetime
import requests
import xml.etree.ElementTree as ET
from dateutil.parser import *


def get_daylight_hours():
    """using openweathermap, get sunrise and sunset times"""
    f = open('/home/andy/repos/daylight/weather.xml', 'r')
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
    # current_time = datetime.datetime.now()
    current_time = time.time()
    sunrise = get_daylight_hours()['sunrise']
    sunset = get_daylight_hours()['sunset']

    if (current_time > sunrise) and (current_time < sunset):
        return True
    else:
        return False

print is_daylight()
