import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)

while True:
    ret, Frame = video_capture.read()
    # Frame = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)
    # Frame = cv2.resize(Frame, (0,0), fx=0.5 , fy=0.5)
    cv2.line(Frame,(0,0),(511,511),(255,0,0),5)
    cv2.imshow("frame",Frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
