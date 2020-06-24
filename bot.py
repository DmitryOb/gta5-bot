import subprocess
import time
import winsound
from cutter import full_cut, parse_tesseract
from matcher import task_render_calc
from PIL import ImageGrab
import cv2
import numpy as np
import pathlib

path_to_clicker = str(pathlib.Path(__file__).parent.absolute()) + '/clickermann/Clickermann.exe'
script_dir = str(pathlib.Path(__file__).parent.absolute()) + '/clicker_scripts/'

init = script_dir + 'init.cms'
first_variant = script_dir + 'first_variant.cms'
second_variant = script_dir + 'second_variant.cms'
third_variant = script_dir + 'third_variant.cms'
oil = script_dir + 'oil.cms'
miner_auto = script_dir + 'miner_auto.cms'
miner_collect = script_dir + 'miner_collect.cms'

def clicker_script_run(script_path):
    subprocess.run(
        f'{path_to_clicker} {script_path}',
        check=True,
        shell=True
    )

def try_match_true_answer(true_answer_result):
    first_variant_answer = tesseract_to_int('cutted/1.png')
    second_variant_answer = tesseract_to_int('cutted/2.png')
    third_variant_answer = tesseract_to_int('cutted/3.png')

    if first_variant_answer == true_answer_result:
        print('true variant is 1')
        clicker_script_run(first_variant)
        return True
    elif second_variant_answer == true_answer_result:
        print('true variant is 2')
        clicker_script_run(second_variant)
        return True
    elif third_variant_answer == true_answer_result:
        print('true variant is 3')
        clicker_script_run(third_variant)
        return True
    else:
        print('we cant find true variant so we click on first')
        clicker_script_run(first_variant)
        print('list of parsed variants:', first_variant_answer, second_variant_answer, third_variant_answer)
        return False

def tesseract_to_int(file_path):
    parse_result = parse_tesseract(file_path)
    try:
        return int(parse_result)
    except:
        print('we find case which we cant covert to number:', parse_result)

def clicker_script_run_with_init(script_path):
    subprocess.run(
        f'{path_to_clicker} {init}',
        check=True,
        shell=True
    )
    subprocess.run(
        f'{path_to_clicker} {script_path}',
        check=True,
        shell=True
    )

def task_is_open():
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
        print("we have a loc")
        return True
    else:
        print("we have not loc")
        return False

def human_is_open():
    base_screen = ImageGrab.grab(bbox=(0, 0, 2560, 1080))
    base_screen.save("base_screen.png")

    template = cv2.imread('human_tpl.png', 0)
    img_rgb = cv2.imread('base_screen.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= 0.926)

    if list(zip(*loc)):
        return True
    else:
        return False

def miner_bot(collect_minute):
    subprocess.run(
        f'{path_to_clicker} {init}',
        check=True,
        shell=True
    )

    i = 0
    while True:
        i += 1
        if i % (4*collect_minute) == 0:
            clicker_script_run(miner_collect)

        clicker_script_run(miner_auto)
        if task_is_open():
            full_cut("base_screen.png")
            true_answer = task_render_calc('cutted/0.png')
            isWork = try_match_true_answer(true_answer)
            time.sleep(1)

def alarm_when_human():
    subprocess.run(
        f'{path_to_clicker} {init}',
        check=True,
        shell=True
    )

    i = 0
    while True:
        i += 1
        if human_is_open():
            winsound.PlaySound('signal.wav', winsound.SND_FILENAME)
            time.sleep(15)
        clicker_script_run(miner_auto)

miner_bot(15)
