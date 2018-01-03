"""
ECE196 Face Recognition Project
Author: W Chen

Adapted from:
http://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/

Use this code as a template to process images in real time, using the same techniques as the last challenge.
You need to display a gray scale video with 320x240 dimensions, with box at the center
"""


# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import numpy as np
import cv2

def createRectangle( image, dim ):
    height = np.size( image, 0 )
    width = np.size( image, 1 )
    centerX = int( 0.5 * width )
    centerY = int( 0.5 * height )
    topL = ( centerX - int(dim[0]/2), centerY - int(dim[1]/2) )
    bottomR = ( centerX + int(dim[0]/2), centerY + int(dim[1]/2) )

    cv2.rectangle( image, topL, bottomR, ( 255, 255, 255 ), 3 )

    return image

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (240, 240) #initially 160, 128
camera.framerate = 32 
camera.color_effects = (128,128) #This adds a grayscale effect
rawCapture = PiRGBArray(camera, size=(240, 240)) #initially 160, 128

# initialized cascade classifier for facial detection
face_cascade = cv2.CascadeClassifier( '/home/pi/opencv-2.4.13.4/data/haarcascades/haarcascade_frontalface_default.xml' )
# allow the camera to warmup
time.sleep(0.1)

count = 0
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array

    faces = face_cascade.detectMultiScale( image )
    
    for (x,y,w,h) in faces:
        cv2.rectangle( image, (x,y), (x+w,y+h), (255,0,0), 1 )
        newImg = image[ y:y+h, x:x+w ]
        cv2.imshow( "faceImg", newImg )
        count += 1
        if count <= 500:
            filePath = './yaleB_faces/19/face%s.jpg' %count
            cv2.imwrite( filePath, newImg )
            print count
        else:
            print 'done collecting faces'
        #time.sleep( 5 )

    #image = createRectangle( image, (100,100) )
    
    # show the frame
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
