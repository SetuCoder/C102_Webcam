#!/usr/bin/env python
import cv2

def take_snapshot():
    # Initializing cv2
    videocaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        # Read the frames while the camera is on
        ret, frame = videocaptureObject.read()
        # imwrite method is used to save an image to any device
        cv2.imwrite("Picture.jpg", frame)
        result = False
        # This is to turn off the camera 
    videocaptureObject.release()
    # It closes all the windows that might be open during this process
    cv2.destroyAllWindows()

take_snapshot()