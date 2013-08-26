#! /usr/bin/env python

import requests
import xml.etree.ElementTree as ET


def save_daylight_xml():
    """save the xml file returned from the api request to
    http://api.openweathermap.org/data/2.5/weather locally
    for use by funcitons, so they dont have to ping the api
    every time."""
    baseurl = "http://api.openweathermap.org/data/2.5/weather"
    query = "?q=salhouse&mode=xml"
    url = baseurl + query
    r = requests.get(url)

    f = open('/home/andy/repos/daylight/weather.xml', 'w')
    f.write(r.text)
    f.close()

save_daylight_xml()
