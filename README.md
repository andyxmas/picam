picam
=====

#how it works:
 - function to take a photo using the raspicam
 - function to upload photo to google drive
 - call this function with a cron job

#inspiration
 - raspberrypi-spy.co.uk/2013/06/testing-multiple-pi-camera-options-with-python
 - https://developers.google.com/drive/quickstart-python

#requirements:
gdata-python-client

https://developers.google.com/gdata/articles/python_client_lib?csw=1

google-api-python-client
 - first install python-setuptools via apt-get
 - then install pip http://www.pip-installer.org/en/latest/installing.html
 - then `pip install --upgrade google-api-python-client`





Daylight
========

Simple function to return true if the current time is between sunrise and sunset.

Current intened use if to stop the raspberry pi cam taking photos when its dark.

Requirements
------------
 * python dateutils to parse date string to timedate
   sudo apt-get install python-dateutil


Plan
----

* Get sunrise/sunset times from openweathermap.org
* Parse xml to time or datetime
* compare time now with these times to return true/false

Further...
----------
To avoid having to call the weather web service every time:
 * function, called daily by cron to save the xml file locally
 * adjust is_daylight to read local file instead of api call 
   if its present, but fall back to the api call if file is missing. 
