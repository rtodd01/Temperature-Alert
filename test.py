#!/usr/bin/python
import sys
import Adafruit_DHT

while True:

	humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
	temperature= (temperature * 9/5 +32)

	print ("Temp: {0:0.1f} F Humidity: {1:0.1f} %".format(temperature, humidity))
