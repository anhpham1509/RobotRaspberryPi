import RPi.GPIO as GPIO
import metroGPIO as io
import time
import os
import sys
import curses
import picamera

##IgnoreWarnings##
GPIO.setwarnings(False)

##InitPins##
io.initMetroPins()
GPIO.setup(io.IN1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(io.IN8,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

##DefinePins##
RF = GPIO.PWM(io.OUT1, 100)
RB = GPIO.PWM(io.OUT2, 100)
LF = GPIO.PWM(io.OUT3, 100)
LB = GPIO.PWM(io.OUT4, 100)
	
##MovingActions##
def idl(): #Idle
	RF.start(0)
	LB.start(0)
	RB.start(0)
	LF.start(0)

def fwd(dc,t): #Go forward
	RF.start(dc)
	LF.start(dc)
	time.sleep(t)
	
def bwd(dc,t): #Go backward
	RB.start(dc)
	LB.start(dc)
	time.sleep(t)
	
def tlt(dc,t): #Turn left
	RF.start(dc)
	time.sleep(t)
	
def trt(dc,t): #Turn right
	LF.start(dc)
	time.sleep(t)


##Camera##	
def camera():
	camera = picamera.PiCamera()
	camera.resolution = (1024, 768)
	camera.start_preview()
	time.sleep(2) #Camera warm-up time
	camera.capture("Triforce.JPG")	
	
	
##Auto Go##
def go(dir,dist):
	##Distance Calculation##
	steps = dist * 20 / dia
	
	try:
		GPIO.add_event_detect(io.IN1,GPIO.RISING,callback=count)
		while (c <= steps):
			if dir == 1:
				fwd(dc,t)
			elif dir == -1:
				bwd(dc,t)
			time.sleep(0.02)
			idl()
		GPIO.remove_event_detect(io.IN1)
		global c
		c = 0
	except KeyboardInterrupt:
		GPIO.cleanup()

##Auto Turn##
def turn(dir,deg):
	try:
		if dir == 1: #Clockwise
			steps = deg * 5 / 20 #Calculate steps needed to turn
			GPIO.add_event_detect(io.IN8,GPIO.RISING, callback=count)
			while (c <= steps):
				trt(dct,t)
				time.sleep(0.02)
				idl()
			GPIO.remove_event_detect(io.IN8)
			global c
			c = 0
		elif dir == -1: #Counter-clockwise
			steps = deg * 5 / 20 #Calculate steps needed to turn3.9
			GPIO.add_event_detect(io.IN1,GPIO.RISING, callback=count)
			while (c <= steps):
				tlt(dct,t)
				time.sleep(0.02)
				idl()
			GPIO.remove_event_detect(io.IN1)
			global c
			c = 0
	except KeyboardInterrupt:
		GPIO.cleanup()

##InitVars##
	#Calculation Values
dia = 204.2506464

	#InitCount
c = 0

	#PWM values
dc = 30
dcr  = dc*1.2#(26/21)#495#3.785/3
dct = 30

	#Time value
t = 0.01

#Call back functions
def count(channel):
	global c
	c += 1

def count1(channel):
	global c1
	c1 += 1

#Process input#
def go_track(x, y, z):
	if (x == 1):
		go(y,z)
	elif(x == 2):
		turn(y,z)

#Read track from file#
def read_track():
	track = open("track.txt","r")
	content = track.readlines()
	action = []

	for line in content:
		for i in line.split():
			tmp = int(i)
			action.append(tmp)
		go_track(action[0],action[1],action[2])
		time.sleep(0.15)
		action = []
	track.close()

##Main##
##Automatic Mode##
idl()
read_track()
GPIO.cleanup()
