#!/usr/bin/env python
import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    # Initializing cv2
    videocaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        # Read the frames while the camera is on
        ret, frame = videocaptureObject.read()
        # imwrite method is used to save an image to any device
        image_name = "img " + str(number) + ".jpg"
        cv2.imwrite(image_name, frame)
        start_time = time.time
        result = False
    return image_name
        # This is to turn off the camera 
    videocaptureObject.release()
    # It closes all the windows that might be open during this process
    cv2.destroyAllWindows()

def upload_file(image_name):
    access_token = "sl.A9mU27Gurt2pVnBTsDGRxH6Am2Omnvn21yotFLQ5iOD6cLZOIc_Fi0yPhSSuPgFuSlxnf53XU847uIW3VMziVxI_uYUveiwTfVQjSJVxE6orMN8I_pgWef26nLx_2tNVU4k1n9Lxw9tx"
    file = image_name
    file_from = file
    file_to = "/Test/" + (image_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("Files Uploaded!")

def main():
    while(True):
        if((time.time() - start_time)>=10):
            name = take_snapshot()
            upload_file(name)

main()