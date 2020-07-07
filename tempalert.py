import os, sys, Adafruit_DHT, time, smtplib
from sensorconfig import users, sensor, pin, sensor_name, low_temp, high_temp
# edit sensorconfig.py for changes to the users, the sensor location, or the sensor

time.sleep(60)

# function that handles sending a text when the temperature is too high or too low
def send_alert(temp):
 	# Establish a secure session with gmail's outgoing SMTP server using your gmail account
 server = smtplib.SMTP( "smtp.gmail.com", 587 )
 server.starttls()
 server.login( 'username@gmail.com', 'password' )
  # Send text message through SMS gateway of destination number
 msg = ("{0} temperature is {1:0.1f} F".format(sensor_name, temp))
 toaddr = users
 server.sendmail( sensor_name, toaddr , msg )
 time.sleep(1800) # Sleep for 30 minutes

# read temperature from sensor, convert to Farenheit, and send alert if temp is too high or low
while True:
  hum, temp = Adafruit_DHT.read_retry(sensor, pin)
  temp= (temp * 9/5 +32)
  if temp < low_temp or temp > high_temp:
   send_alert(temp)