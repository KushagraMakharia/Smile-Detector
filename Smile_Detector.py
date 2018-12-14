#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 16:27:19 2018

@author: kushagra
"""
#Imporing the libraries
import cv2
 
#Creating Cascades
#eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")

#Creating function
def detect(gray,frame):
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        #eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
        smile = smile_cascade.detectMultiScale(gray,1.3,22)
        for(sx, sy, sw, sh) in smile:
            cv2.rectangle(frame, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)
    return frame

#Opening Camera
video = cv2.VideoCapture(-1)

while(True):
    _,frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    canvas = detect(gray, frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
