from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO

# Setup the camera
camera = PiCamera()
camera.resolution = (1200, 1200)

# GPIO setup
button_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def take_picture():
    camera.start_preview()
    sleep(2)  # Warm-up time for the camera
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()
    print("Picture taken!")

# Function to handle button event
def button_callback(channel):
    print("Button pressed!")
    take_picture()

# Add event detection to the GPIO pin
GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=button_callback, bouncetime=300)

try:
    # Keep the program running
    message = input("Press enter to quit\n\n")
finally:
    GPIO.cleanup()  # Clean up GPIO on normal exit
    camera.close()

