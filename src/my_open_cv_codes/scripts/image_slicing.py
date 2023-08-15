import numpy as np
import cv2

img = cv2.imread("human.jpg")

copy = img.copy()
# rmo = 0
# for i in range(copy.shape[0]):
#     for j in range(copy.shape[1]):
#         copy[i][j][rmo] = 0

print("creating a window holder for image")
cv2.namedWindow("image",cv2.WINDOW_NORMAL)

print("Displaying the image")
cv2.imshow("image",copy)

print("Press a key inside a image to make a copy")
# while(True):
#     ch = input()
#     if ch:
#         break
cv2.waitKey(0)