#!/usr/bin/env python

import time
import csv
from beebotte import *

### Replace CHANNEL_TOKEN with that of your channel
bbt = BBT(token = 'CHANNEL_TOKEN')

### Define the wait period between readings (default is 10 minutes in seconds)
period = 600

### Change channel name as suits - in this instance, it is called BME280
temp_resource = Resource(bbt, 'BME280', 'temperature')
pressure_resource = Resource(bbt, 'BME280', 'pressure')
humidity_resource = Resource(bbt, 'BME280', 'humidity')

while True:
    with open("/home/pi/bme280-pi/my-data.csv", "r") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            temp = float(row[1])
            press = float(row[2])
            hum = float(row[3])
            temp_resource.write(temp)
            pressure_resource.write(press)
            humidity_resource.write(hum)
        time.sleep(period)