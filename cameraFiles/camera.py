from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()
camera.resolution = ( 1920, 1080 )
camera.framerate = 15
# open camear to preview real-time videos
# alpha = transperency
camera.start_preview( alpha = 200 )

camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
camera.annotate_text = "Hello World"
'''
for i in range( 5 ):
    sleep( 2 )
    camera.capture( '/home/pi/Desktop/cameraFiles/img%s.jpg' %i )
'''

#camera.start_recording('/home/pi/Desktop/cameraFiles/video1.h264' )
sleep( 5 )
#camera.stop_recording()
i = 0
for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    camera.annotate_text = "Effect: %s" %effect
    sleep(2)
    camera.capture('/home/pi/Desktop/cameraFiles/img%s.jpg' %i)
    i = i + 1
    if i == 10:
        break

camera.stop_preview()
