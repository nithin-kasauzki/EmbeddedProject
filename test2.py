from io import BytesIO
import os
import sys
from time import sleep
import logging

import pytesseract
from gtts import gTTS
from PIL import Image
#from picamera import PiCamera

class OCR:
    def extract_text(self, image_path, language="eng"):
        try:
            image = Image.open(image_path)
            return pytesseract.image_to_string(image, lang=language)
        except Exception as e:
            logging.error("Can not extract text from image - {}".format(str(e)))

class TTS:
    def text_to_speech(self, text, save_to, language="en"):
        try:
            tts = gTTS(text=text, lang=language)
            tts.save(save_to)
        except Exception as e:
            logging.error("Can not convert text to speech - {}".format(str(e)))

class DocumentReader:
    mp3_dir = "/tmp/mp3-files"
    mp3_file = "{}/{}".format(mp3_dir, "speech.mp3")

    def __init__(self):
        if not os.path.exists(self.mp3_dir):
            os.mkdir(self.mp3_dir, 0o755)

    def run(self):
        #os.mkdir('s0ma', 0o755)
        image_path = "images/image.png"  
        text = OCR().extract_text(image_path)
        logging.info("Extracted text: {}".format(text))

        TTS().text_to_speech(text, self.mp3_file, "en")
        self.clean()

    def clean(self):
        # Add cleanup code if needed
        pass

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info('Started')
    document_reader = DocumentReader()
    document_reader.run()
    logging.info('Finished')

if __name__ == '__main__':
    main()
