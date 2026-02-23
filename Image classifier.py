#import neccessary libraries
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers,datasets, models  
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt

#load the MNIST dataset
(train_images, train_labels), (test_images, test_labels)=datasets.mnist.load_data()

#preprocess the data: Normalize the pixel values to be between 0 and 1
train_images = train_images / 255.0
test_images = test_images / 255.0

#Reshape the images to (28, 28, 1) as they are grayscale images

train_images = train_images.reshape((train_images.shape[0], 28, 28, 1))
test_images = test_images.reshape((test_images.shape[0], 28, 28, 1))

#Convert the labels to one-hot encoding
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

#Build the CNN model
model = models.Sequential()

#First convolutional layer
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))

#Second convolutional layer
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

#Third convolutional layer
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

#Flatten the 3D output to ID and add dense layers
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))


# Output layer with 10 NEURONs (for 10 digits) and softmax activation
model.add(layers.Dense(10, activation='softmax'))

#Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

#Train the model
model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_data=(test_images, test_labels))

#Evaluate the model
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f'Test accuracy: {test_acc * 100:.2f}%')

#make predictions on test images
predictions = model.predict(test_images)
print(f"Predictions for the first test image: {np.argmax(predictions[4])}")


plt.imshow(test_images[4].reshape(28, 28), cmap='gray')
plt.title(f"Predicted Label: {np.argmax(predictions[4])}")
plt.show()