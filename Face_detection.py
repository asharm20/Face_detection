#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import cv2


# Using Haarcascade to Implement Face detection 

face_cascade = cv2.CascadeClassifier('/Users/ayushsharma/repos/Harcascade/frontalFace10/haarcascade_frontalface_default.xml')

# Using Haarcascade to detect facial features\

eye_cascade = cv2.CascadeClassifier('/Users/ayushsharma/repos/Harcascade/frontalFace10/parojos.xml')

# Reading Image

img = cv2.imread('/Users/ayushsharma/repos/Harcascade/frontalFace10/black-and-white-boy-casual-555790.jpg')

#Converting Image to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Using the Haarcascader

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Fetching the coordinates of detected image to draw bounding box

for (x,y,w,h) in faces:
    # Drawing the rectangle aroung the image
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    # Using Haarcascade to detect Facial Properties
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
cv2.imshow('img',roi_gray)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




