# bme280-pi
Use the BME280 temperature, pressure and humidity sensor on the Raspberry Pi and display the output in the terminal.

Inspiration taken from [this guide on Raspberry Pi Spy](https://www.raspberrypi-spy.co.uk/2016/07/using-bme280-i2c-temperature-pressure-sensor-in-python/), but adapted to display only the temperature, pressure and humidity readings in the terminal.

## Installation

Clone this repository:
````
git clone https://github.com/raspberrycoulis/bme280-pi.git
````

Then ensure the BME280 is connected up correctly:
* 3.3V to VIN
* GND to GND
* SDA to SDA
* SCL to SCL

Also need to ensure that I2C and SPI are enabled via `sudo raspi-config` and enabling I2C and SPI via the `Interface` menu. For good measure, it is also worth installing `i2c-tools` via `sudo apt-get update && sudo apt-get install i2c-tools. Verify that your Raspberry Pi can see the BME280 by running `sudo i2cdetect -y 1` at the command prompt.

---

## Running

Assuming you are in the `bme280-pi` directory, simply run:
````
./bme280-pi.py
````

This will display the current temperature, pressure and humidity in the terminal, updating every 0.5 seconds. Exit via `CTRL+C`.
