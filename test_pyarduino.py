from pyarduino import *

# do some tests,
if __name__ == '__main__':
	print "lets start"
	ard = arduino ("COM21")
	ard.pinMode (13, PORT.OUTPUT)
	ard.digitalWrite (13, DIGITAL.LOW)
	time.sleep (2)
	ard.digitalWrite (13, DIGITAL.HIGH)
	ard.digitalWrite (13, DIGITAL.LOW)
	print ard.digitalRead (13)
	print ard.analogWrite (0, 100)
	print ard.analogRead (4)
	print ard.analogReference (ANALOG.DEFAULT)
	print ard.tone (8, 100)
	time.sleep (2)
	#print ard.tone (8, 100, 2000)
	print ard.noTone (8)
