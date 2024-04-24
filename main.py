"""
sudo apt update
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
pip3 install pytesseract
pip3 install gtts
"""
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
import pytesseract
from PIL import Image
from gtts import gTTS
import os

# Initialize the camera
camera = PiCamera()
camera.resolution = (1024, 768)
button_pin = 5
GPIO.setmode(GPIO.BOARD)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Path for saving the captured image
image_path = 'images/captured_image.jpg'

def capture_image():
    camera.start_preview()
    sleep(2)  # Camera warm-up time
    camera.capture(image_path)
    camera.stop_preview()
    print("Image Captured.")

def extract_text(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    print("Extracted Text: ", text)
    return text

def speak_text(text):
    tts = gTTS(text=text, lang='en')
    tts.save("temp.mp3")
    os.system("mpg321 temp.mp3")

# Main Function
def main():
    try:
        while True:
            GPIO.wait_for_edge(button_pin,GPIO.RISING)
            capture_image()
            text = extract_text(image_path)
            if text:
                speak_text(text)
            else:
                print("No text found.")
            sleep(1)
    except KeyboardInterrupt:
        pass
    

if __name__ == "__main__":
    main()
