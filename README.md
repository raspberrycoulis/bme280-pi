# bme280-pi
Use the BME280 temperature, pressure and humidity sensor on the Raspberry Pi and display the output in the terminal.

Inspiration taken from [this guide on Raspberry Pi Spy](https://www.raspberrypi-spy.co.uk/2016/07/using-bme280-i2c-temperature-pressure-sensor-in-python/), but adapted to display only the temperature, pressure and humidity readings in the terminal.

The script called `bme280-microdot-beebotte.py` also sends sensor readings to [Beebotte](https://beebotte.com) every 15 minutes so you can log the readings over time. 

## Installation

Clone this repository:
````
git clone https://github.com/raspberrycoulis/bme280-pi.git
````

Then ensure the BME280 is connected up correctly:
* 3.3V to VIN
* GND to GND
* SDA to SDA
* SCL to SCL

Also need to ensure that I2C and SPI are enabled via `sudo raspi-config` and enabling I2C and SPI via the `Interface` menu. For good measure, it is also worth installing `i2c-tools` via `sudo apt-get update && sudo apt-get install i2c-tools`. Verify that your Raspberry Pi can see the BME280 by running `sudo i2cdetect -y 1` at the command prompt.

### Install Beebotte
If you plan on using the Beebotte side of things, you’ll need to install the Beebotte client via:
````
pip install beebotte
````

Then you will need to create a channel and use the token in the `bme280-microdot-beebotte.py` code. 

## Running

Assuming you are in the `bme280-pi` directory, simply run:
````
./bme280-pi.py
````

This will display the current temperature, pressure and humidity in the terminal, updating every 0.5 seconds. Exit via `CTRL+C`.

## To do

The process of closing the script on the `bme280-microdot-beebotte.py` side still needs work due to the use of threading. Happy for help if people can assist here! Open an issue / or PR. 
