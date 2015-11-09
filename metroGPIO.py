# Output pins of Metropolia's GPIO addon board
# O_P* should be used in the code.
# Numbers 3,5,... are Raspberry pi board pin numbers and they should not be changed unless you know the addon board layout

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Output pins
global OUT1
global OUT2
global OUT3
global OUT4
global OUT5
global OUT6
global OUT7
global OUT8
OUT1=9
OUT2=10
OUT3=22
OUT4=27
OUT5=17
OUT6=4
OUT7=3
OUT8=2

#Input pins
global IN1
global IN2
global IN3
global IN4
global IN5
global IN6
global IN7
global IN8
IN1=20
IN2=21
IN3=26
IN4=19
IN5=13
IN6=6
IN7=5
IN8=11

def initMetroPins():
	#Output pins
	GPIO.setup(OUT1,GPIO.OUT)
	GPIO.setup(OUT2,GPIO.OUT)
	GPIO.setup(OUT3,GPIO.OUT)
	GPIO.setup(OUT4,GPIO.OUT)
	GPIO.setup(OUT5,GPIO.OUT)
	GPIO.setup(OUT6,GPIO.OUT)
	GPIO.setup(OUT7,GPIO.OUT)
	GPIO.setup(OUT8,GPIO.OUT)
	
	#Input pins
	GPIO.setup(IN1,GPIO.IN)
	GPIO.setup(IN2,GPIO.IN)
	GPIO.setup(IN3,GPIO.IN)
	GPIO.setup(IN4,GPIO.IN)
	GPIO.setup(IN5,GPIO.IN)
	GPIO.setup(IN6,GPIO.IN)
	GPIO.setup(IN7,GPIO.IN)
	GPIO.setup(IN8,GPIO.IN)



