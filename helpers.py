# двигать мышкой
# pyautogui.moveTo(100, 100)
# pyautogui.mouseDown()
# time.sleep(0.4)
# pyautogui.mouseUp()
# w, h = template.shape[::-1]


# pip install opencv-python pyautogui

# pip install pywin32

# --------x
# |
# |
# y

# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
# loc = np.where(result >= 0.83)
# if (list(zip(*loc))):
#     print(loc)
#     for pt in zip(*loc[::1]):
#         x = int(pt[0])
#         y = int(pt[1])
#     find_answer_button(x, y, i, result)
# else:
#     print("we have not loc", i)
# time.sleep(0.3)

import cv2

def viewcv(cv2Obj):
    cv2.imshow("viewCv", cv2Obj)
    cv2.waitKey(0)

# def cuting_screen(loc):
#     y_min = np.amin(loc, axis=1)[0]
#     y_max = np.amax(loc, axis=1)[0]
#     button_height = y_max - y_min
#     x_min = np.amin(loc, axis=1)[1]
#     x_max = np.amax(loc, axis=1)[1]
#     button_width = x_max-x_min
#     top_left_point_x = x_min - button_width
#     top_left_point_y = y_max - button_height*12
#     cut_screen = ImageGrab.grab(bbox=(
#         top_left_point_x,
#         top_left_point_y,
#         top_left_point_x + 4*button_width,
#         top_left_point_y + button_height * 13
#     ))
#     cut_screen.save("cut_screen.png")