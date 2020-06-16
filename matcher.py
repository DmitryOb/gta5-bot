import sys
import cv2
from PIL import ImageGrab
from PIL import Image
from helpers import viewcv
import numpy as np
import os

def matched_cut(x, y, w, h):
    print(x, y)
    img = Image.open('tasks_png/2+4.png')
    img_right = img.crop((x, y, x+w, y+h))
    img_right.save('matched_cut.png')

def calculate(found_arr):
    answer = 0
    for true_number in found_arr:
        answer += true_number
    return answer

def match_file_with_tmpl(main_template, matched_image):
    template = cv2.imread('single_char_numbers/' + main_template, 0)
    w, h = template.shape[::-1]  # применимо только к темплейту который считам с флагом 0
    img_rgb = cv2.imread(matched_image)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= 0.926)

    if list(zip(*loc)):
        # print(loc)
        # for pt in zip(*loc[::1]):
        #     x = int(pt[0])
        #     y = int(pt[1])
        # matched_cut(y, x, w, h)
        return True
    else:
        return False

def task_render_calc(task):
    single_chars = os.listdir('single_char_numbers')
    number = 0
    found_arr = []
    for number_file_name in single_chars:
        number += 1
        if match_file_with_tmpl(number_file_name, task):
            found_arr.append(number)
    if len(found_arr) == 1:
        found_arr.append(found_arr[0])
    print('=======================================')
    print(task, 'we find numbers:', found_arr)
    answer = calculate(found_arr)
    print('answer is: ', answer)
    return answer
