from pynput.mouse import Button, Controller
import time

mouse = Controller()
def click():
    mouse.press(Button.left)
    time.sleep(0.0720)
    mouse.release(Button.left)

time.sleep(4)
mouse.position = (1150, 425)
time.sleep(0.0720)
click()
mouse.position = (1200, 700)
time.sleep(0.0720)
click()