import tensorflow as tf
import os
import cv2
import imghdr
import numpy as np
import keras
from keras import layers
import os
gpus = tf.config.experimental.list_physical_devices("GPU")
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)

dataDir = "Data"
imageExts = ["jpeg", "jpg", "bmp", "png"]

for imageClass in os.listdir(dataDir):
    for image in os.listdir(os.path.join(dataDir, imageClass)):
        imagePath = os.path.join(dataDir, imageClass, image)
        try:
            img = cv2.imread(imagePath)
            tip = imghdr.what(imagePath)
            if tip not in imageExts:
                os.remove(imagePath)
        except:
            print("Image Issue")

data = tf.keras.utils.image_dataset_from_directory("Data", label_mode="categorical")

data_iterator = data.as_numpy_iterator()
batch = data_iterator.next()

data = data.map(lambda x,y: (x/255, y)) # Normalize Data
data.as_numpy_iterator().next()

# Establish batch count
trainSize = int(len(data) * 0.7) + 1
valSize = int(len(data) * 0.2) + 1
testSize = int(len(data) * 0.1) + 1

# Create batches
train = data.take(trainSize)
val = data.skip(trainSize).take(valSize)
test = data.skip(trainSize + valSize).take(testSize)

# Create model
num_classes = len(os.listdir(dataDir))

# Create a Sequential model
model = keras.models.Sequential()

# Add convolutional layers
model.add(layers.Conv2D(16, (3, 3), 1, activation='relu', input_shape=(256, 256, 3)))
model.add(layers.MaxPooling2D())
model.add(layers.Conv2D(32, (3, 3), 1, activation='relu'))
model.add(layers.MaxPooling2D())
model.add(layers.Conv2D(16, (3, 3), 1, activation='relu'))
model.add(layers.MaxPooling2D())

# Flatten the output
model.add(layers.Flatten())

# Dense layers
model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dense(num_classes, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
# Display the model summary
model.summary()

model.fit(train, epochs=20, validation_data=val)

# Evaluate the model on the test set
test_loss, test_accuracy = model.evaluate(test)
print(f'Test Accuracy: {test_accuracy * 100:.2f}%')

