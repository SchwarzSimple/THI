# Artificial Neural Networks Modeling project

## Car Detection

### Model description
- For the first modeling project, we used some libraries of python such as NumPy and matplotlib,
to be able to create and use matrices and arrays. Indeed, after dividing the images in two
categories, we reshape the images in a convenient format and number of pixels, so that the
amount of data to analyze stays reasonable. We also made the choice to switch the images colors
to scales of gray, in order to reduce the dimension of the matrix mapping the pixels (we use an
array of three values for RGB values but only one for a grayscale). Once the images are
processed, we shuffle the data, and divide it in three parts to make the training, testing and
validation.

### Network architecture
- Concerning the network architecture, we are doing applying a series convolution and pooling
layers. For each convolution layers, we are learning 64 filters and the feature detector windows
have a dimension of 3x3. For a set of images that have a dimension of 100x40 pixels. The
activation functions that we use then is “Rectified Linear Unit”, “Hyperbolic Tangent” and
“Sigmoid”. The window used for the pooling is 2x2 sized. We defined lists of values (Dense
Layers, Layer Sizes and Convolutional Layers) to make different combinations in between, so
we have a 3x64 layer convolutional network. Then, we modified the number of neurons and
epochs to generate several models.

### Learning, test, and validation protocols
- Size of the database and database division

### Learnig curve


## Face-mask Detection

### Model description
- The model is a feedforward backpropagation network to classify images into two categories,
which are those who wear a mask and those who don’t.

### Network architecture
- We used a different method for the second project, still on python, but using the activation
function “Softmax”, additionally to “ReLU”, to enhance efficiency.

### Learning, test, and validation protocols
- Size of the database and database division
- Description of the input and output data format: Input data are resized to 64*64(color
images). Output data are classified to “With Mask” or “Without Mask”.
- Normalization: All data are normalized before feeding to the network by using the mean
and standard deviation values to keep the values between 0 and 1.
- Optimizer: Adam is used as an optimizer, which uses a learning rate per parameter, and
adapts that learning rate depending on the rate of change of those parameters.
- Loss function: Cross Entropy is used as a loss function, which is calculated using the
probabilities of the events from P and Q, as follows: H(P, Q) = -sum x in X P(x) *
log(Q(x)).
- Learning rate: 0.001

### Learnig curve