"""
ECE196 Face Recognition Project
Author: W Chen

What this script should do:
0. assume the local host is already connected to ec2 instance.
1. start running the camera.
2. detect a face, display it, and get confirmation from user.
3. send it for classification and fetch result.
4. show result on face display.
"""

import cv2, os, time, subprocess
from picamera import PiCamera
from picamera.array import PiRGBArray

# TODO: declare useful paths here if you plan to use them
CASCADE_PATH = "/home/pi/opencv-2.4.13.4/data/haarcascades/haarcascade_frontalface_default.xml" # this might change based on where it is loated on the pi
EC2_IP = "ec2-user@ec2-54-148-16-187.us-west-2.compute.amazonaws.com"  # ec2
KEY_PAIR_PATH = "/home/pi/Facial_rec_pem_file/skomatin2_gpupem.pem"  # local #this is where the pem file is stored in the rpi
NEW_FACE_PATH = "/home/pi/new_face" # i think this is local #path to the new folder that i have to make on the rpi to store the new captured face
NEW_FACE_NAME = "/new_face.jpg"
face_path = (NEW_FACE_PATH + NEW_FACE_NAME) #local, i added this
IMG_DEST_DIR = "/home/ec2-user/Facial_Recognition/ece196FaceRecognition/new_face" # ec2 #directory where the new face image is stored
FONT = cv2.FONT_HERSHEY_SIMPLEX
RESULT_SRC_DIR = "/home/ec2-user/Facial_Recognition/ece196FaceRecognition/result/result.txt"  # ec2
RESULT_DEST_DIR = "/home/pi/result/result.txt"  # local # the path up to the directory (not including the result file) where the result is stored in rpi 
NEW_RESULT_PATH = "/home/pi/result/result.txt"  # local # path where the result file is stored in the rpi (including where the new result file is stored


def send_file(file_path):
    """
    send file to ec2
    :param file_path: path of local file
    """
    send_command = ["scp", "-i", KEY_PAIR_PATH, file_path, EC2_IP + ":" + IMG_DEST_DIR]
    subprocess.call(send_command)
    print 'sending file to server'
    return


def fetch_file():
    """
    use a loop to check if new result is available and if yes fetch it
    :return: local path for result
    """
    fetch_command = ["scp", "-i", KEY_PAIR_PATH, EC2_IP + ":" + RESULT_SRC_DIR, RESULT_DEST_DIR]
    while True:
        try:
            subprocess.check_call(fetch_command)
            return NEW_RESULT_PATH
        except subprocess.CalledProcessError:
            continue


def read_result(result_path):
    """
    read result and extract name and confidence
    :param result_path: path of the result file
    :return: name and confidence
    """
    result_file = open(result_path, 'r')
    result = result_file.read()
    details = result.split(',')
    name = details[0]
    conf = details[1]
    print name, conf
    return name, conf


def main():

    print 'face path: ', face_path
    # 1. start running the camera.
    # TODO: initialize face detector # OK
    face_cascade = cv2.CascadeClassifier(CASCADE_PATH)

    # TODO: initialize camera and update parameters #take a look
    camera = PiCamera()
    width = 160 # initially 640
    height = 128  #initially 480
    camera.framerate = 32 # i added this, not sure if this is necessary
    #camera.rotation = 180 #i commented this out
    camera.resolution = (width, height)
    rawCapture = PiRGBArray(camera, size=(width, height))

    # warm up
    print 'Let me get ready ... 2 seconds ...'
    time.sleep(2)
    print 'Starting ...'

    # 2. detect a face, display it, and get confirmation from user.
    for f in camera.capture_continuous(rawCapture, format='bgr', use_video_port=True):
        frame = f.array
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # TODO: use face detector to get faces  #OK
        faces = face_cascade.detectMultiScale(img) #i added this
        
        for (x, y, w, h) in faces:
            print '=================================='
            print 'Face detected!'
            cv2.imshow('Face Image for Classification', img) #not sure if this should be img or frame 
            
            cv2.waitKey(2000)
            cv2.destroyAllWindows()
            cv2.waitKey(1)
            cv2.waitKey(1)
            cv2.waitKey(1)
            cv2.waitKey(1)
            answer = input('Confirm image (1-yes / 0-no): ')
            print '=================================='

            if answer == 1:
                # TODO: save face to local #OK
                cv2.imwrite(face_path, frame)

                # TODO: send it for classification and fetch result. #OK
                send_file(face_path) #using the function written above

                os.remove(face_path)
                print 'Let\'s see who you are...'
                # look for new result
                apple =  fetch_file() #check this line
                for i in range(3):
                    time.sleep(1)
                    print 'Still thinking...'

                # TODO: get new result path and get name and confidence #OK
                final_name, final_confidence = read_result(apple)
            
                print 'New result found!'

                # TODO: display on face image #OK
                result_to_display = final_name
                
                cv2.putText(frame, result_to_display, (10, 30), FONT, 1, (0, 255, 0), 2)
                cv2.imshow('Face Image for Classification', frame)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                cv2.waitKey(1)
                cv2.waitKey(1)
                cv2.waitKey(1)
                cv2.waitKey(1)
                # remove result
                #os.remove(NEW_RESULT_PATH)
                break

        rawCapture.truncate(0)
        print 'Waiting for image...'
        time.sleep(1)
    return


if __name__ == '__main__':
    main()
