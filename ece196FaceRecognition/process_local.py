import cv2
"""
ECE196 Face Recognition Project
Author: W Chen

Prerequisite: You need to install OpenCV before running this code
The code here is an example of what you can write to print out 'Hello World!'
Now modify this code to process a local image and do the following:
1. read geisel-hr.jpg
2. convert color to gray scale
3. resize to half of its original dimensions
4. draw a box at the center the image with size 10x10
5. save image with a new name to local directory
All the above steps should be in one function called process_image()
"""


# TODO: edit this function
def process_image():
    img = cv2.imread( "geisel.jpg", 0 )
    newImage = cv2.resize( img, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_CUBIC )

    newImageSize = newImage.shape
    centerX = int( 0.5 * newImageSize[0] )
    centerY = int( 0.5 * newImageSize[1] )
    topLeft = ( centerX - 5, centerY - 5 )
    bottomRight = ( centerX + 5, centerY + 5 )

    print "newImageSize = ", newImageSize
    print "centerX = ", centerX
    print "topLeft = ", topLeft
    recImage = cv2.rectangle( newImage, topLeft, bottomRight, ( 255, 255, 255 ), 3 )
    #cv2.imwrite( 'geisel_rectangle.jpg', recImage )
    #cv2.imshow( "geisel", recImage )
    #cv2.waitKey( 0 )
    return


def hello_world():
    print 'Hello World!'
    return


def main():
    hello_world()
    return


if __name__ == '__main__':
    main()

process_image()
