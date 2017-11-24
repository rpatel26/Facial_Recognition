import glob, os, shutil

'''
files = glob.glob( './cameraFiles/*.jpg'  )
print files, "\n"
print "testType = ", type( files )
print "testSize = ", len( files)
train = int(0.7*len(files))
val=train + int(0.1*len(files))

trainSet = files[:train]
valSet = files[train:val]
testSet = files[val:len(files)]
print trainSet, "\n"
print valSet, "\n"
print testSet, "\n"
'''
pyFiles = glob.glob( './cameraFiles/*.py' )
print pyFiles[0]
shutil.copy( pyFiles[0], './' )
