import os, time
from datetime import datetime

os.system('sudo apt-get update')
os.system('sudo apt-get upgrade -y')

os.system('sudo python3 -m pip install --upgrade pip setuptools wheel')
os.system('sudo pip3 install Adafruit_DHT')

os.system('mv /home/pi/Temperature-Alert/tempalert.service /etc/systemd/system/')
os.system('sudo chmod 644 /etc/systemd/system/tempalert.service')
os.system('chmod +x /home/pi/Temperature-Alert/tempalert.py')
os.system('sudo systemctl daemon-reload')
os.system('sudo systemctl enable tempalert.service')
os.system('sudo systemctl start tempalert.service')

os.system('sudo raspi-config')