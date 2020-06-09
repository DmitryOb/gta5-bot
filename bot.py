import time
import winsound
import cv2
import os
import sys
import numpy as np
from PIL import ImageGrab, Image
from api import ocr_space_file
from cutter import full_cut, parse_tesseract

def task_processing(filename):
    full_cut(filename)

    task = ocr_space_file(filename='cutted/0.png')
    print("Original parse: ", task)
    task = task.split("=", maxsplit=1)
    task = task[0].replace(' ', '')
    true_answer = eval(task)
    print("True answer:", true_answer)

    orig_first_variant = parse_tesseract('cutted/1.png')
    print("1 (original):", orig_first_variant)
    first_variant = int(orig_first_variant)
    print("1:", first_variant)

    orig_second_variant = parse_tesseract('cutted/2.png')
    print("2 (original):", orig_second_variant)
    second_variant = int(orig_second_variant)
    print("2:", second_variant)

    orig_third_variant = parse_tesseract('cutted/3.png')
    print("3 (original):", orig_third_variant)
    third_variant = int(orig_third_variant)
    print("3:", third_variant)

    winsound.PlaySound('calculated.wav', winsound.SND_FILENAME)

def search_tasks_cycle():
    i = 0
    find = False
    while not find:
        i += 1
        base_screen = ImageGrab.grab(bbox=(0, 0, 2560, 1080))
        base_screen.save("base_screen.png")
        img = cv2.imread("base_screen.png")
        mod = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        hsv_low_yellow = np.array((22.5, 207.06, 255), np.uint8)
        hsv_high_yellow = np.array((26, 255, 255), np.uint8)
        mask_yellow = cv2.inRange(mod, hsv_low_yellow, hsv_high_yellow)
        result = cv2.bitwise_and(mod, mod, mask=mask_yellow)
        result = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)
        loc = np.where(result >= 0.99)
        if (list(zip(*loc))):
            for pt in zip(*loc[::1]):
                x = int(pt[0])
                y = int(pt[1])
            print("we have a loc", i)
            find = True
            winsound.PlaySound('find_task.wav', winsound.SND_FILENAME)
            task_processing('base_screen.png')
        else:
            print("we have not loc", i)
        time.sleep(0.3)

def alaram_when_task():
    i = 0
    while True:
        i += 1
        base_screen = ImageGrab.grab(bbox=(0, 0, 2560, 1080))
        base_screen.save("base_screen.png")
        img = cv2.imread("base_screen.png")
        mod = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        hsv_low_yellow = np.array((22.5, 207.06, 255), np.uint8)
        hsv_high_yellow = np.array((26, 255, 255), np.uint8)
        mask_yellow = cv2.inRange(mod, hsv_low_yellow, hsv_high_yellow)
        result = cv2.bitwise_and(mod, mod, mask=mask_yellow)
        result = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)
        loc = np.where(result >= 0.99)
        if (list(zip(*loc))):
            for pt in zip(*loc[::1]):
                x = int(pt[0])
                y = int(pt[1])
            print("we have a loc", i)
            winsound.PlaySound('find_task.wav', winsound.SND_FILENAME)
        else:
            print("we have not loc", i)
        time.sleep(0.3)

alaram_when_task()
