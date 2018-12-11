# tsys01-python

A Python module to interface with the TSYS01 temperature sensor. Tested on Raspberry Pi 3 with Raspbian.

The python SMBus library must be installed.

	sudo apt-get install python-smbus

# Usage

	import tsys01

### TSYS01(bus=1)

	sensor = tsys01.TSYS01() # Use default I2C bus 1
	sensor = tsys01.TSYS01(0) # Specify I2C bus 0

### init()

Initialize the sensor. This needs to be called before using any other methods.

    sensor.init()

Returns true if the sensor was successfully initialized, false otherwise.

### read()

Read the sensor and update the temperature.

    sensor.read()

Returns True if read was successful, False otherwise.

### temperature(conversion=UNITS_Centigrade)

Get the most recent temperature measurement.

	sensor.temperature() # Get temperature in default units (Centigrade)
	sensor.temperature(ms5837.UNITS_Farenheit) # Get temperature in Farenheit

Valid arguments are:

	tsys01.UNITS_Centigrade
	tsys01.UNITS_Farenheit
	tsys01.UNITS_Kelvin

Returns the most recent temperature in the requested units, or temperature in degrees Centigrade if invalid units specified. Call read() to update.
