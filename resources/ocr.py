from flask_restful import Resource
from flask import request
import pytesseract
import io
import traceback
import cv2
import numpy as np


class OCR(Resource):
    @staticmethod
    def post():
        try:
            files = request.files

            # Mention the installed location of Tesseract-OCR in your system
            pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract.exe'

            out_below = ''
            for name, image in files.items():
                in_memory_file = io.BytesIO()
                image.save(in_memory_file)

                image = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)
                color_image_flag = 1
                image = cv2.imdecode(image, color_image_flag)

                gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
                gray, img_bin = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
                gray = cv2.bitwise_not(img_bin)
                kernel = np.ones((2, 1), np.uint8)
                image = cv2.erode(gray, kernel, iterations=1)
                image = cv2.dilate(image, kernel, iterations=1)
                out_below = pytesseract.image_to_string(image)

            return out_below

        except Exception:
            return traceback.format_exc()