#!/usr/bin/python
# -*- coding: utf-8 -*-

import bme280
import time
import sys

try:
    while True:
	temperature,pressure,humidity = bme280.readBME280All()
	sys.stdout.write("\rTemperature is %d°C | Pressure is %dhPa | Humidity is %d%% \033[K" % (temperature,pressure,humidity))
	sys.stdout.flush()
	time.sleep(0.5)

except KeyboardInterrupt:
    print "\n"
    pass
