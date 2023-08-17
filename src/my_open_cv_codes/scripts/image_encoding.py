import numpy as np
import cv2

img = cv2.imread("tree.jpg")

# copy = img.copy()
# rmo = 0
# for i in range(copy.shape[0]):
#     for j in range(copy.shape[1]):
#         copy[i][j][rmo] = 0

print("creating a window holder for image")
cv2.namedWindow("image",cv2.WINDOW_NORMAL)

print("Displaying the image")
# red, blue, green = cv2.split(img)
# cv2.imshow("image",green)
# print(green.shape)

#spliting the image in hsv (hue,saturation and value)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
hsv_image = np.concatenate((h,s,v),axis=1)
cv2.imshow("hsv image",hsv_image)


# print("Press a key inside a image to make a copy")
# while(True):
#     ch = input()
#     if ch:
#         break
cv2.waitKey(0)