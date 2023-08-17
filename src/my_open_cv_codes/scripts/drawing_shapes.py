import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)

cv2.line(img,(0,0),(511,511),(255,255,255),5)
#cv2.line(img,(0,511),(511,0),(255,255,255),5)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Learning ROS OpenCV',(10,250),font, 1, (255,255,255),2, cv2.LINE_AA)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
