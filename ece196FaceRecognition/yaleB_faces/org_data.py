'''
File description: organize face data from yaleB_faces into three separate folders,
    namely training set, validation set, and test set
'''
import os, glob, shutil

for i in range( 18 ):
    # generating path names/ folder names
    if i >= 10:
        filename = '../yaleB_faces/%s/*' %(i)
        newFile_train = './trainSet/%s/' %i
        newFile_val = './valSet/%s/' %i
        newFile_test = './testSet/%s/' %i

    else:
        filename = '../yaleB_faces/%s%s/*' %(0,i)
        newFile_train = './trainSet/%s%s' %(0,i)
        newFile_val = './valSet/%s%s/' %(0,i)
        newFile_test = './testSet/%s%s/' %(0,i)


    # iterating throught the current folder
    files = glob.glob( filename )
    
    train = int(0.7*len(files))
    val = train + int(0.1*len(files))

    trainSet = files[:train]
    valSet = files[train:val]
    testSet = files[val:len(files)]

    # creating new directory is its not already there
    if not os.path.exists( newFile_train ):
        os.makedirs( newFile_train )
  
    if not os.path.exists( newFile_val ): 
        os.makedirs( newFile_val)
    
    if not os.path.exists( newFile_test ):
        os.makedirs(newFile_test)
    
    # copying files from data folder to new folder created above
    for j in trainSet :
        shutil.copy (j, newFile_train)

    for j in valSet :
        shutil.copy(j,newFile_val)
    
    for j in testSet :
        shutil.copy(j,newFile_test)
