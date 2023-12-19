from picamera import PiCamera
import time

def pic():
    camera = PiCamera()
    camera.resolution = (2048, 1536)
    camera.sharpness = 90
    camera.image_denoise = True
    camera.start_preview()
    time.sleep(3)
    camera.capture('capture_test.jpg')


