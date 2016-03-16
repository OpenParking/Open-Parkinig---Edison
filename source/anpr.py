import cv2
import cv
import sys
import os
import requests
import json
from pytesseract import image_to_string
from pytesseract import pytesseract as ocr

vidCap = cv2.VideoCapture(0)

while True:
    small = cv2.imread("plate.jpg")  # vidCap.read()
    small = cv2.resize(small, (0, 0), fx=0.5, fy=0.5)
    small = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
    small = cv2.medianBlur(small, 5)

    # Otsu's thresholding after Gaussian filtering
    retOtsu, thOtsu = cv2.threshold(small, 128, 255, cv2.THRESH_OTSU)
    
    # temporately write images to storage
    tempOtsu = 'plateTgOtsu.jpeg'
    cv2.imwrite(tempOtsu, thOtsu)
    tempOtsuTiff = 'plateTgOtsu.tiff'
    img = ocr.Image.open(tempOtsu)
    text = ocr.image_to_string(img)

    # delete temp files
    os.remove(tempOtsu)
    # os.remove(tempOtsuTiff)

    print text

    # img = Image.open(original)
    # img.save('plate.tiff')
    # im = Image.open(img)
    # text = image_to_string(im)
    # text = image_file_to_string(image_file)
    break
