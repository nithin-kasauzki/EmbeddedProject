# This is the main file without pi camera

# import RPi.GPIO as GPIO
# from picamera import PiCamera
from io import BytesIO
from time import sleep
import pytesseract
from PIL import Image
from gtts import gTTS
import cv2
import os
import sys
import logging

# Initialize the camera
# camera = PiCamera()
# camera.resolution = (1024, 768)
# button_pin = 5
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


# Path for saving the captured image
image_path = 'images/captured_image.jpg'

# def capture_image():
#     camera.start_preview()
#     sleep(2)  # Camera warm-up time
#     camera.capture(image_path)
#     camera.stop_preview()
#     print("Image Captured.")

def capture_image():
    cap = cv2.VideoCapture(0) # 0 for primary camera, 1 for secondary/external camera
    if not cap.isOpened():
        print("Error: Unable to open camera.")
    else:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(image_path, frame)
            print("Image captured and saved")
        else:
            print("Error: Failed to capture frame.")
    cap.release()

def extract_text(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

def speak_text(text):
    tts = gTTS(text=text, lang='en')
    tts.save("temp.mp3")
    os.system("vlc temp.mp3")

# Main Function
def main():
    capture_image()
    text = extract_text(image_path)
    print("Extracted Text: ", text)
    if text and text.isalnum():
        speak_text(text)

    # try:
    #     while True:
    #         GPIO.wait_for_edge(button_pin,GPIO.RISING)
    #         capture_image()
    #         text = extract_text(image_path)
    #         if text:
    #             speak_text(text)
    #         else:
    #             print("No text found.")
    #         sleep(1)
    # except KeyboardInterrupt:
    #     pass
    

if __name__ == "__main__":
    main()
