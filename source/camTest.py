import cv2

cap = cv2.VideoCapture(0)

while True:
    if cap.isOpened():
        print True
    else: print False
