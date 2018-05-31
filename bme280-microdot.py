#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bme280
import time
import sys
from microdotphat import write_string, set_decimal, clear, show

try:
    while True:
	     clear()
        temperature,pressure,humidity = bme280.readBME280All()
        write_string( "%.2f" % temperature + "°C", kerning=False)
        show()
        time.sleep(5)
        clear()
        temperature,pressure,humidity = bme280.readBME280All()
        write_string( "%.2f" % pressure + "hPa", kerning=False)
        show()
        time.sleep(5)
        temperature,pressure,humidity = bme280.readBME280All()
        write_string( "%.2f" % humidity + "%", kerning=False)
        show()
        time.sleep(5)

except KeyboardInterrupt:
    print "\n"
    pass
