from keras.layers import Input, Dense
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.models import Model

# this returns a tensor
# inputs = Tensor( "input_1:0", shape = ( ?, 784 ), dtype = float32 )
inputs = Input( shape = (32,32,1) )

# creating hidden layers
c1 = Conv2D( filters=6, kernel_size=(5,5), activation='sigmoid')(inputs)
s2 = MaxPooling2D( pool_size = (2,2), strides=(2,2)) (c1)
c3 = Conv2D( filters=16, kernel_size=(5,5), activation='sigmoid')(s2)
s4 = MaxPooling2D( pool_size = (2,2) )(c3)
c5 = Conv2D( filters=120, kernel_size=(5,5), activation='sigmoid')(s4)
f6 = Dense( units=84, activation='tanh' )(c5)
f7 = Dense( units=10, activation='softmax' )(f6)

model = Model( inputs = inputs, outputs = f7 )
model.summary()

print "c1 = ", c1
print "s2 = ", s2
print "c3 = ", c3
print "s4 = ", s4
print "c5 = ", c5
print "f6 = ", f6
print "f7 = ", f7
