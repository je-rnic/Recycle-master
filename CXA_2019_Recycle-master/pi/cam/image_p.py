from picamera import PiCamera
import time

def pic():
	camera = PiCamera()
	camera.resolution = (512, 384)
	camera.sharpness = 50
	camera.image_denoise = False
	camera.start_preview()
	time.sleep(3)
	camera.capture('capture.jpg')
	camera.close()

pic()
