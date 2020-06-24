from PIL import Image
import pytesseract
import os

# нарезаем с полного скрина 4 вида картинки
def full_cut(filename, ultra_wide=True):
    single_cut(0, filename, ultra_wide)
    single_cut(1, filename, ultra_wide)
    single_cut(2, filename, ultra_wide)
    single_cut(3, filename, ultra_wide)

def single_cut(number, filename, ultra_wide=True):
    img = Image.open(filename)

    if ultra_wide:
        x1 = 1219
        x2 = 1335
        task_row = [350, 385]   # task
        first_row = [415, 450]   # answer1
        second_row = [470, 505]   # answer2
        third_row = [522, 560]   # answer3
        Rows = [
            (x1, task_row[0], x2, task_row[1]),
            (x1, first_row[0], x2, first_row[1]),
            (x1, second_row[0], x2, second_row[1]),
            (x1, third_row[0], x2, third_row[1]),
        ]
    else:
        x1 = 1219
        x2 = 1335
        task_row = [350, 385]   # task
        first_row = [415, 450]   # answer1
        second_row = [470, 505]   # answer2
        third_row = [522, 560]   # answer3
        Rows = [
            (x1, task_row[0], x2, task_row[1]),
            (x1, first_row[0], x2, first_row[1]),
            (x1, second_row[0], x2, second_row[1]),
            (x1, third_row[0], x2, third_row[1]),
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
    parsed_text = parsed_text.replace('"', '1')
    parsed_text = parsed_text.replace('Q', '9')
    parsed_text = parsed_text.replace('B', '13')
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
