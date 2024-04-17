from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO

# Setup the camera
camera = PiCamera()
camera.resolution = (1200, 1200)
GPIO.setwarnings(False) 
# GPIO setup
button_pin = 5
GPIO.setmode(GPIO.BOARD)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def take_picture():
    camera.start_preview()
    sleep(2)  # Warm-up time for the camera
    camera.capture('/home/raspberry/Desktop/30_86_134/img.jpg')
    camera.stop_preview()
    print("Picture taken!")


try:
    while True:
        GPIO.wait_for_edge(button_pin,GPIO.RISING)
        take_picture()
        sleep(1)
except KeyboardInterrupt:
    pass


