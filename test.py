#!usr/bin/python

import togdrive

print("hello")
print

togdrive.upload_to_gdrive(
	'test3.txt', 
	'my 3rd text doc', 
	'uploaded via the demo.py file', 
	'text/plain'
	)

