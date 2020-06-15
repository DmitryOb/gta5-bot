import cv2
from PIL import ImageGrab
from PIL import Image
from helpers import viewcv
import numpy as np

def matched_cut(x, y, w, h):
    print(x, y)
    img = Image.open('tasks_png/2+4.png')
    img_right = img.crop((x, y, x+w, y+h))
    img_right.save('matched_cut.png')


template = cv2.imread('single_char/ravno.png', 0)
w, h = template.shape[::-1]  # применимо только к темплейту который считам с флагом 0
img_rgb = cv2.imread('tasks_png/2+4.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
result = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
loc = np.where(result >= 0.9)

if list(zip(*loc)):
    print(loc)
    for pt in zip(*loc[::1]):
        x = int(pt[0])
        y = int(pt[1])
    matched_cut(y, x, w, h)
else:
    print("we have not loc")
