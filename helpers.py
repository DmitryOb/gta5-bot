import cv2
from PIL import ImageGrab

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