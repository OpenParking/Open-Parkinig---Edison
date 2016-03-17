"""Detects faces from webcam."""
import cv2
import sys
from collections import Counter
from requests import put
import json

# Get user supplied values
cascPath = sys.argv[1]
numFrames = int(sys.argv[2])
cameraIdx = int(sys.argv[3])

countFrames = 0
numObjsCount = []

cap = cv2.VideoCapture(cameraIdx)
url = "http://198.199.119.166/settransit/Z1/"

# Create the haar cascade
objCascade = cv2.CascadeClassifier(cascPath)

while True:
    countFrames += 1
    ret, frame = cap.read()

    # Read the image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    objects = objCascade.detectMultiScale(frame, 1.1, 2)
    # Draw a rectangle around the objects
    for (x, y, w, h) in objects:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    numObjsCount.append(len(objects))

    cv2.imshow("Frame", frame)

    if countFrames >= 10:
        counter = Counter(numObjsCount)
        numObjs = counter.most_common(1)[0][0]
        print(numObjs)
        countFrames = 0
        numObjsCount = []
        put(url + str(numObjs))
        del counter

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
