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
	
	
##InitVars##
	#Calculation Values
dia = 204.2506464

	#InitCount
c = 0

	#PWM values
dc = 30
dct = 30

	#Time value
t = 0.01

##Main##
##Manual Mode##
	
	##InitScreen##
stdscr = curses.initscr()

	##InitCurses##
curses.noecho() #Turn off echo
curses.cbreak #React keys instantly
stdscr.keypad(True) #Enable keypad mode

try:
	while True:
		curses.flushinp()
		stdscr.clear()
		choice = stdscr.getch()
		stdscr.refresh()

		yt=0.2
		xt=0.1
			
		if choice == curses.KEY_UP:
			fwd(dc,yt)
			
		elif choice == curses.KEY_DOWN:
			bwd(dc,yt)

		elif choice == curses.KEY_LEFT:
			tlt(dc,xt)

		elif choice == curses.KEY_RIGHT:
			trt(dc,xt)
			
		else:
			print("Invalid!!")
			
		idl()

except KeyboardInterrupt:
	stdscr.refresh()
	stdscr.clear()
	print ("Bye")
	
	#######EndCurses######
stdscr.keypad(False)
curses.nocbreak()
curses.echo()
curses.endwin()
idl()
GPIO.cleanup()
