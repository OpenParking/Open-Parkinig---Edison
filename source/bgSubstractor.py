import numpy as np
import cv2

cap = cv2.VideoCapture(1)
fgbg = cv2.BackgroundSubtractorMOG(history=0, nmixtures=0, backgroundRatio=0, noiseSigma=0.54)

while(1):
    ret, original = cap.read()
    fgmask = fgbg.apply(original)

    # Otsu's thresholding after Gaussian filtering
    # blur = cv2.GaussianBlur(fgmask,(5,5),0)
    # ret3,th3 = cv2.threshold(fgmask,128,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    cv2.imshow('original', fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()
