'''
	pyarduino
	Remotely automate arduino boards using python	
	Author : Raja Jamwal <linux1@zoho.com>
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
	
'''

#!/usr/bin/python
import serial
import time
	
class enum (object):
    def __init__(self, names):
        for number, name in enumerate(names.split()):
            setattr(self, name, number)

STATUS 		= enum ("OK FAIL")
DIGITAL 	= enum ("HIGH LOW")
PORT    	= enum ("OUTPUT INPUT")
OPERATION   = enum ("PIN_MODE DIGITAL_WRITE DIGITAL_READ ANALOG_REFERENCE ANALOG_READ ANALOG_WRITE TONE TONE_DURATION NO_TONE SHIFT_OUT SHIFT_IN PULSE_IN")
ANALOG      = enum ("DEFAULT INTERNAL INTERNAL1V1 INTERNAL2V56 EXTERNAL") 

def dprint (string):
	if __name__ == '__main__':
		print (string)
		
class arduino:

	def tone (self, pin, freq, duration=0):
		if (self.com != None):
			if (duration==0):
				self.data = chr(OPERATION.TONE)+chr(2)+chr(pin)+chr(freq)
				self.write (self.data)
				self.read (2) #read status
			else:
				self.data = chr(OPERATION.TONE_DURATION)+chr(2)+chr(pin)+chr(freq)+chr(255 if duration> 255 else duration)
				self.write (self.data)
				self.read (2) #read status

	def noTone (self, pin):
		if (self.com != None):
			self.data = chr(OPERATION.NO_TONE)+chr(1)+chr(pin)
			self.write (self.data)
			self.read (2) #read status
				
	def __init__ (self, port, baud_rate = 9600):
		self.port = port
		self.com  = serial.Serial (port, baud_rate)
		self.data = self.read (3)
		
		if ord(self.data[0]) == STATUS.OK and ord(self.data[1]) == 1:
			dprint ("Arduino connected, supports version "+str(ord(self.data[2]))) 
	
	def pinMode (self, pin, mode):
		if (self.com != None):
			self.data = chr(OPERATION.PIN_MODE)+chr(2)+chr(pin)+chr(mode)
			self.write (self.data)
			self.read (2) #read status
	
	def digitalWrite (self, pin, mode):
		if (self.com != None):
			self.data = chr(OPERATION.DIGITAL_WRITE)+chr(2)+chr(pin)+chr(mode)
			self.write (self.data)
			self.read (2) #read status
			
	def digitalRead (self, pin):
		if (self.com != None):
			self.data = chr(OPERATION.DIGITAL_READ)+chr(1)+chr(pin)
			self.write (self.data)
			self.read (2) #read status
			self.data = self.read (4)
			if ord(self.data[0]) == OPERATION.DIGITAL_READ and ord(self.data[1]) == 2:
				return DIGITAL.HIGH if ord (self.data[3]) == DIGITAL.HIGH else DIGITAL.LOW
	
	def analogReference (self, type):
		if (self.com != None):
			self.data = chr(OPERATION.ANALOG_REFERENCE)+chr(1)+chr(type)
			self.write (self.data)
			self.read (2) #read status
			
	def analogRead (self, pin):
		if (self.com != None):
			self.data = chr(OPERATION.ANALOG_READ)+chr(1)+chr(pin)
			self.write (self.data)
			self.read (2) #read status
			self.data = self.read (4)
			if ord(self.data[0]) == OPERATION.ANALOG_READ and ord(self.data[1]) == 2:
				return ord (self.data[3])
	
	def analogWrite (self, pin, value):
		if (self.com != None):
			self.data = chr(OPERATION.ANALOG_WRITE)+chr(2)+chr(pin)+chr(value)
			self.write (self.data)
			self.read (2) #read status
	
	def read (self, length = 1):
		data = self.com.read (length)
		return data
		
	def write (self, data):
		self.com.write (data)
	