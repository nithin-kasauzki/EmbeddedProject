"""
sudo apt update
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
pip3 install pytesseract
pip3 install gtts
"""

from picamera import PiCamera
from time import sleep
import pytesseract
from PIL import Image
from gtts import gTTS
import os

# Initialize the camera
camera = PiCamera()
camera.resolution = (1024, 768)

# Path for saving the captured image
image_path = '/home/pi/Desktop/captured_image.jpg'

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
    tts.save("/home/pi/Desktop/temp.mp3")
    os.system("mpg321 /home/pi/Desktop/temp.mp3")

# Main Function
def main():
    capture_image()
    text = extract_text(image_path)
    if text:
        speak_text(text)
    else:
        print("No text found.")

if __name__ == "__main__":
    main()
