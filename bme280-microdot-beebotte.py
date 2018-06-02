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
    while True:
        temp_resource.write(round(temperature,1))
        pressure_resource.write(round(pressure,0))
        humidity_resource.write(round(humidity,0))
        time.sleep(900)

def microdot():
    clear()
    write_string( "%.1f" % temperature + "C", kerning=False)
    show()
    time.sleep(5)
    # Uncomment to display pressure if needed
    #clear()
    #write_string( "%.0f" % pressure + "hPa", kerning=False)
    #show()
    #time.sleep(5)
    write_string( "%.0f" % humidity + "% RH", kerning=False)
    show()
    time.sleep(5)

try:
    temperature,pressure,humidity = bme280.readBME280All()
    beebotte_thread = threading.Thread(target=beebotte)
    beebotte_thread.start()
    while True:
        temperature,pressure,humidity = bme280.readBME280All()
        microdot()

except (KeyboardInterrupt, SystemExit):
    print "\n"
    sys.exit()
    pass
