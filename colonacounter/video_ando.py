#!/usr/bin/env python
# Python 2/3 compatibility
from __future__ import print_function

import cv2 as cv

MOTION_THRESHOLD = 0.1

cap = cv.VideoCapture(0)
cv.namedWindow("Video")

fgbg = cv.bgsegm.createBackgroundSubtractorMOG()
img_width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
img_height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
img_size = img_width * img_height

while True:
    status, img = cap.read()
    fgmask = fgbg.apply(img)

    whitePixels = cv.countNonZero(fgmask)
    ratio = whitePixels / img_size

    if ratio > MOTION_THRESHOLD:
        print("koronda")

    cv.imshow("Video", fgmask)


    k = cv.waitKey(1)
    if k == 27:
        break
    
