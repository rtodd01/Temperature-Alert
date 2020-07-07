import os, sys, Adafruit_DHT, time, smtplib

#users user1, user2, user3, user4, user5

users = "10digitnumber@mms.att.net", "10digitnumber@mms.att.net", "10digitnumber@mms.att.net", "10digitnumber@vtext.com", "10digitnumber@vtext.com"

sender_account = 'username@gmail.com', 'password'

sensor = Adafruit_DHT.AM2302 #DHT11/DHT22/AM2302
pin = 4
sensor_name = "example name"

low_temp = 55.0
high_temp = 80.0
