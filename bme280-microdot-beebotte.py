#!/usr/bin/env python

import bme280
import time
import sys
import threading
from microdotphat import write_string, set_decimal, clear, show
from beebotte import *

### Replace CHANNEL_TOKEN with that of your Beebotte channel and
### YOUR_CHANNEL_NAME with the name you give your Beebotte channel
bbt = BBT(token = 'CHANNEL_TOKEN')
chanName = "YOUR_CHANNEL_NAME"

### Change Beebotte channel name as suits you - in this instance, it is called BME280.
temp_resource   = Resource(bbt, chanName, 'temperature')
pressure_resource  = Resource(bbt, chanName, 'pressure')
humidity_resource = Resource(bbt, chanName, 'humidity')

# Sends data to your Beebotte channel
def beebotte():
    while True:
        temp_resource.write(round(temperature,1))
        pressure_resource.write(round(pressure,0))
        humidity_resource.write(round(humidity,0))
        time.sleep(900)    # 15 mins to prevent maxing API limit

# Display stats on the Micro Dot pHAT
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
    clear()
    write_string( "%.0f" % humidity + "% RH", kerning=False)
    show()
    time.sleep(5)

try:
    # Get the first reading from the BME280 sensor
    temperature,pressure,humidity = bme280.readBME280All()
    # Start the Beebotte function as a thread so it works in the background
    beebotte_thread = threading.Thread(target=beebotte)
    beebotte_thread.daemon = True
    beebotte_thread.start()
    # Run a loop to collect data and display it on the Micro Dot pHAT
    while True:
        temperature,pressure,humidity = bme280.readBME280All()
        microdot()

# Attempt to exit cleanly - not quite there, needs work!
except (KeyboardInterrupt, SystemExit):
    sys.exit()
    pass
