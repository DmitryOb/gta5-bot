import time
from PIL import Image
from api import ocr_space_file
import pytesseract
import cv2
import os

def full_cut(filename):
    single_cut(0, filename)
    single_cut(1, filename)
    single_cut(2, filename)
    single_cut(3, filename)

def single_cut(number, filename):
    img = Image.open(filename)
    x1 = 1219
    x2 = 1335
    Rows = [
        (x1, 340, x2, 396),  # task
        (x1, 413, x2, 454),  # answer1
        (x1, 475, x2, 499),  # answer2
        (x1, 527, x2, 553),  # answer3
    ]
    img_right = img.crop(Rows[number])
    img_right.save('cutted/' + str(number) + '.png')

def parse_tesseract(filename):
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    image = Image.open(filename)
    parsed_text = pytesseract.image_to_string(
        image,
        config='--psm 6',
    )
    if parsed_text == 'Q':
        parsed_text = 9
    return parsed_text

def multiple_cut_task():
    i = 0
    arr = os.listdir('screen_tasks')
    for val in arr:
        print(val)
        img = Image.open('screen_tasks/' + val)
        x1 = 1219
        x2 = 1335
        Rows = [
            (x1, 340, x2, 396),  # task
            (x1, 413, x2, 454),  # answer1
            (x1, 475, x2, 499),  # answer2
            (x1, 527, x2, 553),  # answer3
        ]
        img_right = img.crop(Rows[0])
        # val = val.split(".", maxsplit=1)
        # val = val[0] + '.tiff'
        img_right.save('tasks/' + 'pol.ocrb.exp' + str(i) + '.tif')
        i += 1

multiple_cut_task()