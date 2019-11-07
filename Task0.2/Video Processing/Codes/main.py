import cv2
import numpy as np
import os

def partA():
    vidcap = cv2.VideoCapture("SB-3087_Task0-master/Task0.2/Video Processing/Videos/RoseBloom.mp4")
    vidcap.set(cv2.CAP_PROP_POS_MSEC, 6000)  # just cue to 6 sec. position
    success, image = vidcap.read()

    if success:
        cv2.imwrite("SB-3087_Task0-master/Task0.2/Video Processing/Generated/frame_as_6.jpg",image)
        success = False
    status = cv2.imwrite("SB-3087_Task0-master\Task0.2\Video Processing\Generated/frame_as_6.jpg",image)

def partB():
    vidcap = cv2.VideoCapture("SB-3087_Task0-master/Task0.2/Video Processing/Videos/RoseBloom.mp4")
    vidcap.set(cv2.CAP_PROP_POS_MSEC, 6000)  # just cue to 6 sec. position
    success, image = vidcap.read()
    b,g,r = cv2.split(image)
    b = b*0
    g = g*0
    img2 = cv2.merge((b,g,r))
    cv2.imwrite("SB-3087_Task0-master/Task0.2/Video Processing/Generated/frame_as_6_red.jpg",img2)

partA()
partB()
