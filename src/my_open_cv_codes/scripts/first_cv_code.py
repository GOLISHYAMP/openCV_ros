#!/usr/bin/env python3

import numpy as np

import cv2

imagename = 'human'
print("Read image from file")
img = cv2.imread(imagename+".jpg")

print("creating a window holder for image")
cv2.namedWindow("image",cv2.WINDOW_NORMAL)

print("Displaying the image")
cv2.imshow("image",img)

print("Press a key inside a image to make a copy")
cv2.waitKey(0)

print("image copied to folder /copy")
cv2.imwrite("copy/"+imagename+".jpg",img)

