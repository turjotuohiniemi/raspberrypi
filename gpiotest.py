#!/usr/bin/python
import RPi.GPIO as GPIO
import time

def lower_pin(pin):
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, False)

def flash_pin(pin):
	for i in range(8, 0, -1):
		GPIO.output(pin, True)
		time.sleep(0.15)
		GPIO.output(pin, False)
		if i > 1:
			time.sleep(0.15)

pins = [3,5,7,8,10,11,12,13,15,16,18,19,21,22,23,24,26,29, \
	31,32,33,35,36,37,38,40]
GPIO.setmode(GPIO.BOARD)

for i in pins:
	lower_pin(i)

for i in pins:
	print "Next pin #", i
	raw_input()
	flash_pin(i)

GPIO.cleanup()
