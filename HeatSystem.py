#!/usr/bin/python

# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import Adafruit_DHT
import time


# Some code by MarcScott.  https://github.com/MarcScott/temperature-log

################################################################
#
# Class:  HeatSystem
#
################################################################

class HeatSystem:
    'HeatSystem documentation'

    # Begin method __init__
    def __init__(self):
        print "HeatSystem constructor"







        # Sensor should be set to Adafruit_DHT.DHT11,
	# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
	self.sensor = Adafruit_DHT.AM2302


	# Example using a Raspberry Pi with DHT sensor
	# connected to GPIO24.
	self.pin = 24







    # End method __init__

    # Begin method Exec
    def Exec(self):
        print "HeatSystem::Exec"

        shouldContinue = True
        while shouldContinue:
            self.GetAirTemp()
            self.GetWaterTemp()
            time.sleep(3)
	    shouldContinue = False
    # End method Exec

    # Begin method GetAirTemp
    def GetAirTemp(self):
        print "HeatSystem::GetAirTemp"

	humidity = 0
	temperature = 0
	temperatureF = 0

  	# Try to grab a sensor reading.  Use the read_retry method which will retry up
	# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
	humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)

	# Note that sometimes you won't get a reading and
	# the results will be null (because Linux can't
	# guarantee the timing of calls to read the sensor).
	# If this happens try again!
	if humidity is not None and temperature is not None:

	    print('Temp={0:0.1f}C  Humidity={1:0.1f}%'.format(temperature, humidity))
	    temperatureF = temperature * 1.8 + 32
	    print ('Temp{0:0.1f}F'.format(temperatureF))
	    writeStats(temperatureF, humidity)
	else:
	    print('Failed to get reading. Try again!')




    # End method GetAirTemp





    # Begin method GetWaterTemp
    def GetWaterTemp(self):
        print "HeatSystem::GetWaterTemp"
    # End method GetWaterTemp

################################################################
#
# End Class:  HeatSystem
#
################################################################



def writeStats(_temp, _humidity):
    with open("stats.csv", "a") as log:
        log.write( "{0}, ".format( time.strftime("%Y-%m-%d %H:%M:%S") ) )
        log.write( "{0}, ".format( str(_temp) ) )
        log.write( "{0} \n".format( str(_humidity) ) )


hs = HeatSystem()

hs.Exec()
