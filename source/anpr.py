import cv2
import cv
import sys
import os
import requests
import json
from PIL import Image
from pytesseract import *

vidCap = cv2.VideoCapture(0)

while True:
    ret, frame = vidCap.read()
    resize = cv.CreateMat(original.rows/ 10, original.cols / 10, original.type)

original = cv.LoadImageM("plate.jpg")
resize = cv.CreateMat(original.rows / 10, original.cols / 10, original.type)
cv.Resize(original, resize)
CvtColor(original, gray, CV_RGB2GRAY)
cvThreshold(image, binary_image, 128, 255, CV_THRESH_OTSU)
