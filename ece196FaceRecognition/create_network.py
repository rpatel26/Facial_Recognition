"""
ECE196 Face Recognition Project
Author: W Chen

Adapted from: https://keras.io/getting-started/functional-api-guide/

Modify this code to write a LeNet with the following requirements:
* Input dimensions: 32x32x1
* C1: convolutional layer, output: 6 layers of 28x28 feature maps, filter size: 5x5,
  strides: 1 both horizontally and vertically, activation function: sigmoid
* S2: max pooling layer, output: 6 layers of 14x14 feature maps, pooling size: 2x2,
  strides: 2 both horizontally and vertically
* C3: convolutional layer, output: 16 layers of 28x28 feature maps, filter size: 5x5,
  strides: 1 both horizontally and vertically, activation function: sigmoid
* S4: max pooling layer, output: 16 layers of 28x28 feature maps, pooling size: 2x2,
  strides: 2 both horizontally and vertically
* C5: convolutional layer, output: 120 layers of 1x1 feature maps, filter size: 5x5, activation function: sigmoid
* F6: fully connected layer, output 84-dimensional vector, activation function: tanh
* F7: fully connected layer, output 10-dimensional vector, activation function: softmax

"""


from keras.layers import Input, Dense
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.models import Model


inputs = Input( shape = (32,32,1) )

c1 = Conv2D(filters=6, kernel_size = (5,5), activation = 'sigmoid') (inputs)
s2 = MaxPooling2D(pool_size = (2,2)) (c1)
c3 = Conv2D(filters=16, kernel_size = (5,5), activation = 'sigmoid') (s2)
s4 = MaxPooling2D(pool_size = (2,2)) (c3)
c5 = Conv2D(filters=120, kernel_size = (5,5), activation = 'sigmoid') (s4)
f6 = Dense(84, activation='tanh') (c5)
f7 = Dense(10, activation = 'softmax') (f6)


print ('c1 = ', c1)
print('s2 = ', s2)
print('c3 = ', c3)
print('s4 = ',s4)
print('c5 = ',c5)
print('f6 = ',f6)
print('f7 = ',f7)




# This creates a model that includes
# the Input layer and three Dense layers
model = Model(inputs=inputs, outputs=f7)

# print model architecture
model.summary()

