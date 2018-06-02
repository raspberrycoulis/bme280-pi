#!/usr/bin/env python

import bme280
import time
import sys
import threading
from microdotphat import write_string, set_decimal, clear, show
from beebotte import *

### Replace CHANNEL_TOKEN with that of your channel
bbt = BBT(token = 'CHANNEL_TOKEN')

### Change channel name as suits you - in this instance, it is called BME280.
temp_resource   = Resource(bbt, 'BME280', 'temperature')
pressure_resource  = Resource(bbt, 'BME280', 'pressure')
humidity_resource = Resource(bbt, 'BME280', 'humidity')

def beebotte():
    temp_resource.write(temperature)
    pressure_resource.write(pressure)
    humidity_resource.write(humidity)
    time.sleep(600)

try:
    while True:
        clear()
        temperature,pressure,humidity = bme280.readBME280All()
        write_string( "%.1f" % temperature + "C", kerning=False)
        show()
        time.sleep(5)
        clear()
        write_string( "%.0f" % pressure + "hPa", kerning=False)
        show()
        time.sleep(5)
        write_string( "%.0f" % humidity + "% RH", kerning=False)
        show()
        time.sleep(5)
        beebotte_thread = threading.Thread(target=beebotte)
        beebotte_thread.start()

except (KeyboardInterrupt, SystemExit):
    print "\n"
    sys.exit()
    pass
