# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2
import numpy as np

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_alt_tree.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')

image_name='donald_trump_kim_jong_un.jpg';

img=cv2.imread(image_name,cv2.IMREAD_COLOR)
gray=cv2.imread(image_name,cv2.IMREAD_GRAYSCALE)

faces=face_cascade.detectMultiScale(gray,1.3,5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi=img[y:y+h,x:x+w]
    roi_gray=gray[y:y+h,x:x+w]
    eyes=eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
