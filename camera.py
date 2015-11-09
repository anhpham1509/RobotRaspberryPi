import time
import picamera

def camera():
	camera = picamera.PiCamera()
	camera.resolution = (1024, 768)
	camera.start_preview()
	time.sleep(2) #Camera warm-up time
	camera.capture("Triforce.JPG")	

camera()