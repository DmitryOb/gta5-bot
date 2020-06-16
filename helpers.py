import cv2
from PIL import ImageGrab
import winsound
from api import ocr_space_file
from cutter import full_cut, parse_tesseract

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

# def task_processing(filename):
#     full_cut(filename)
#
#     task = ocr_space_file(filename='cutted/0.png')
#     print("Original parse: ", task)
#     task = task.split("=", maxsplit=1)
#     task = task[0].replace(' ', '')
#     true_answer = eval(task)
#     print("True answer:", true_answer)
#
#     orig_first_variant = parse_tesseract('cutted/1.png')
#     print("1 (original):", orig_first_variant)
#     first_variant = int(orig_first_variant)
#     print("1:", first_variant)
#
#     orig_second_variant = parse_tesseract('cutted/2.png')
#     print("2 (original):", orig_second_variant)
#     second_variant = int(orig_second_variant)
#     print("2:", second_variant)
#
#     orig_third_variant = parse_tesseract('cutted/3.png')
#     print("3 (original):", orig_third_variant)
#     third_variant = int(orig_third_variant)
#     print("3:", third_variant)
#
#     winsound.PlaySound('calculated.wav', winsound.SND_FILENAME)
