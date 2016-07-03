# raspberrypi

Basic stuff to help with hacking the Raspberry Pi

## gpiotest.py

You can use this to test all the general-purpose IO pins - useful with 
Raspberry Zero where you have to solder a 40-pin socket by yourself. 
Connect each pin in turn to a 220 ohm resistor, followed by a led and 
then to a ground pin. The program will flash the led a few times, then 
asks you to rewire and press enter to continue.
