"""
sudo apt update
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
pip3 install pytesseract
pip3 install gtts
"""


from time import sleep
import pytesseract
from PIL import Image
from gtts import gTTS
import os

# Initialize the camera
#
# Path for saving the captured image
#image_path = '/captured_image.jpg'
image_path = 'img2.png'
#
def extract_text(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    print("Extracted Text: ", text)
    return text

def speak_text(text):
    tts = gTTS(text=text, lang='en')
    tts.save("temp.mp3")
    #os.system("mpg321 temp.mp3")

# Main Function
def main():
    #capture_image()
    text = extract_text(image_path)
    
    if text:
        speak_text(text)
    else:
        print("No text found.")

if __name__ == "__main__":
    main()
