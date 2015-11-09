import RPi.GPIO as GPIO
import metroGPIO as io
import time
import os
import sys
import curses

##IgnoreWarnings##
GPIO.setwarnings(False)

##InitPins##
io.initMetroPins()
GPIO.setup(io.IN1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(io.IN8,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

##DefinePins##
o1 = GPIO.PWM(io.OUT1, 100)
o2 = GPIO.PWM(io.OUT2, 100)
o3 = GPIO.PWM(io.OUT3, 100)
o4 = GPIO.PWM(io.OUT4, 100)
	
##MovingActions##
def idl(): #Idle
	o1.start(0)
	o4.start(0)
	o2.start(0)
	o3.start(0)

def fwd(dc,t): #Go forward
	o1.start(dc)
	o3.start(dc)
	time.sleep(t)
	
def bwd(dc,t): #Go backward
	o2.start(dc)
	o4.start(dc)
	time.sleep(t)
	
def tlt(dc,t): #Turn left
	o1.start(dc)
	#o4.start(dc)
	time.sleep(t)
	
def trt(dc,t): #Turn right
	#o2.start(dc)
	o3.start(dc)
	time.sleep(t)

##Camera##	
	
	
	
##AutoGo##
def go(dir,dist):
	##Distance Calculation##
	#real_dist= 1.5 * dist - 0.5  #dc = 30
	steps = int((dist) * 20 / dia)
	
	try:
		GPIO.add_event_detect(io.IN1,GPIO.RISING,callback=count)
		GPIO.add_event_detect(io.IN8,GPIO.RISING,callback=count1)
		while (c <= steps):
			if dir == 1:
				fwd(dc,t)
			elif dir == -1:
				bwd(dc,t)
			time.sleep(0.02)
			idl()
		GPIO.remove_event_detect(io.IN1)
		GPIO.remove_event_detect(io.IN8)
		print("c1 = ",c," c2 = ",c1)
		global c
		c = 0
		global c1
		c1 = 0
	except KeyboardInterrupt:
		GPIO.cleanup()

##AutoTurn##
def turn(dir,deg):
	#Degree calculation
	#real_deg = deg - 0#9.8#0#20
	steps = int(deg * 2.5 / 20) #3.9
	
	try:
		if dir == 1:
			GPIO.add_event_detect(io.IN8,GPIO.RISING, callback=count)
			while (c <= steps):
				trt(dct,t)
				time.sleep(0.02)
				idl()
			GPIO.remove_event_detect(io.IN8)
			print(c)
			global c
			c = 0
		elif dir == -1:
			GPIO.add_event_detect(io.IN1,GPIO.RISING, callback=count1)
			while (c1 <= steps):
				tlt(dct,t)
				time.sleep(0.02)
				idl()
			GPIO.remove_event_detect(io.IN1)
			print(c1)
			global c1
			c1 = 0
	except KeyboardInterrupt:
		GPIO.cleanup()

##InitVars##
	#Calc Values
dia = 204.2506464

	#InitCount
c = 0
c1 = 0
	#User Input
choice = '' 
	#PWM values
dc = 30
dcr  = dc*1.2#(26/21)#495#3.785/3
dct = 30
t = 0.01

#Call back functions
def count(channel):
	global c
	c += 1
	#print (c)

def count1(channel):
	global c1
	c1 += 1


def go_track(x, y, z):
	if (x == 1):
		go(y,z)
	elif(x == 2):
		turn(y,z)

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
		#print(action)
		action = []
	track.close()

##Main##
idl()


##Automatic Mode##
read_track()
'''
#S1#
go(1,0.2)
time.sleep(0.2)
go(1,0.2)
time.sleep(0.2)
go(1,0.2)
time.sleep(0.2)
go(1,0.2)
time.sleep(0.2)
go(1,0.2)
time.sleep(0.2)
go(1,0.2)
time.sleep(0.2)
go(1,0.2)
time.sleep(0.2)
#go(1,0.2)
#time.sleep(0.2)
#go(1,0.2)
#time.sleep(0.2)

#Turn 90#
turn(1,30)
time.sleep(0.5)
turn(1,30)
time.sleep(0.5)
turn(1,30)
time.sleep(0.5)

#GO more#
go(1,0.2)
time.sleep(0.2)
go(1,0.2)
time.sleep(0.2)
go(1,0.2)
time.sleep(0.2)
#go(1,0.2)
#time.sleep(0.2)

#Turn 60#
turn(1,30)
time.sleep(0.5)
turn(1,30)
time.sleep(0.5)
#turn(1,30)
#time.sleep(0.5)

#Go more#
go(1,0.2)
time.sleep(0.2)
go(1,0.2)
time.sleep(0.2)
go(1,0.15)
time.sleep(0.2)


turn(1,30)
time.sleep(0.5)
#turn(1,8)
#time.sleep(0.5)
#turn(1,30)
#time.sleep(0.5)

go(1,0.2)
time.sleep(0.2)
go(1,0.2)
time.sleep(0.2)
go(1,0.15)
time.sleep(0.2)

#turn(1,30)
#time.sleep(0.5)
#turn(1,30)
#time.sleep(0.5)
#turn(1,30)
#time.sleep(0.5)

#go(1,0.1)
#time.sleep(0.2)
#turn(1,90)
#time.sleep(0.05)
#go(1,0.1)
#time.sleep(0.2)
#go(1,0.1)
#times.sleep(0.2)
#go(1,0.1)
#time.sleep(0.2)
#turn(-1,60)
GPIO.cleanup()
'''
'''
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
			tlt(dct,xt)

		elif choice == curses.KEY_RIGHT:
			trt(dct,xt)
			
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
'''

idl()
GPIO.cleanup()
