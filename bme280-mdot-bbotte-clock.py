#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bme280
import time
import datetime
import sys
import threading
import httplib, urllib
from microdotphat import write_string, set_decimal, clear, show
from beebotte import *

### Replace CHANNEL_TOKEN with that of your Beebotte channel
### and YOUR_CHANNEL_NAME_HERE with the channel you create
bbt = BBT(token = 'CHANNEL_TOKEN')
chanName = "YOUR_CHANNEL_NAME_HERE"

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

# Experimental! Clock - may not work yet!
# Display time on Micro Dot pHAT for set time
showClock = 5 # Seconds

# Function for the clock
def clock():
    while True:
        clockEndTime = time.time() + showClock
        while time.time() < clockEndTime:
            clear()
            t = datetime.datetime.now()
            if t.second % 2 == 0:
                set_decimal(2, 1)
                set_decimal(4, 1)
            else:
                set_decimal(2, 0)
                set_decimal(4, 0)
            write_string(t.strftime('%H%M%S'), kerning=False)
            show()
            time.sleep(0.05)

# Experimental! Pushover notifications - should work
def pushover():
    conn = httplib.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
      urllib.urlencode({
        "token": "APP_TOKEN",                       # Insert app token here
        "user": "USER_TOKEN",                       # Insert user token here
        "html": "1",
        "title": "High temperature!",
        "message": "It is "+str(temperature)+ "°C in the nursery!",
        "url": "https://beebotte.com/dash/RANDOM_ID_HERE",
        "url_title": "View Beebotte dashboard",
        "sound": "siren",
      }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()

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
    clock()

try:
    # Get the first reading from the BME280 sensor
    temperature,pressure,humidity = bme280.readBME280All()
    # Start the Beebotte function as a thread so it works in the background
    beebotte_thread = threading.Thread(target=beebotte)
    beebotte_thread.start()
    # Run a loop to collect data and display it on the Micro Dot pHAT
    # and send notifications via Pushover if it is too hot
    while True:
        temperature,pressure,humidity = bme280.readBME280All()
        if temperature >= 26:
            pushover()
        else:
            continue
        microdot()

# Attempt to exit cleanly - not quite there, needs work!
except (KeyboardInterrupt, SystemExit):
    beebotte_thread.stop()  # Experimental, needs testing
    sys.exit()
    pass
