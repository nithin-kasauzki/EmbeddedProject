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
import re

# Initialize the camera
camera = PiCamera()
camera.resolution = (1024, 768)
button_pin = 5
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


# Path for saving the captured image
image_path = 'images/captured_image.jpg'

def capture_image():
    #camera.start_preview()
    sleep(2)  # Camera warm-up time
    camera.capture(image_path)
    #camera.stop_preview()
    print("Image Captured.")
    return

def extract_text(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

def speak_text(text):
    tts = gTTS(text=text, lang='en')
    tts.save("temp.mp3")
    os.system("vlc temp.mp3")
    return
def remove_non_alphanumeric(text):
    # Define a regular expression to match non-alphanumeric characters
    pattern = re.compile(r'[^a-zA-Z0-9 ]')
    
    # Use the sub() function to replace non-alphanumeric characters with an empty string
    cleaned_text = re.sub(pattern, '', text)
    
    return cleaned_text

def camera_on_off():
    if flag==0:
        camera.start_preview()
        flag=1
    if flag==1:
        camera.stop_preview()
        flag=0
# Main Function
def main():
    try:
        while True:
            camera.start_preview()
            GPIO.wait_for_edge(button_pin,GPIO.RISING)
            capture_image()
            sleep(0.001)
            camera.stop_preview()
            text=extract_text(image_path)
            text = re.sub(r'\s+', ' ', text)
            print("Extracted Text: ", text)
            if text:
                speak_text(text)
            else:
                print("No text found.")
                text="unable to extract text"
                speak_text(text)
            sleep(1)
    except KeyboardInterrupt:
        pass
    

if __name__ == "__main__":
    main()
