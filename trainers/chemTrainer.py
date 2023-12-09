# Import libraries
import tensorflow as tf
import os
import keras
from keras import layers
import os
import cv2
import imghdr

# Suppress warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = "2"

# Configure GPUs
gpus = tf.config.experimental.list_physical_devices("GPU")
for gpu in gpus:
  tf.config.experimental.set_memory_growth(gpu, True)

# Find data directory
dataDir = "data/chemData"
imageExts = ["jpeg", "jpg", "bmp", "png"]

# Create dataset from data directory
data = tf.keras.utils.image_dataset_from_directory(dataDir, label_mode="categorical", image_size=(256, 256))

# Normalize training data
data = data.map(lambda x, y: (x / 255, y))

# Seperate training data to training data, validation data and test data
train_size = int(len(data) * 0.7)
val_size = int(len(data) * 0.2)
test_size = int(len(data) * 0.1)
train = data.take(train_size)
val = data.skip(train_size).take(val_size)
test = data.skip(train_size + val_size).take(test_size)

# Add bad images to a list
images_to_remove = []
for imageClass in os.listdir(dataDir):
    for image in os.listdir(os.path.join(dataDir, imageClass)):
        imagePath = os.path.join(dataDir, imageClass, image)
        try:
            img = cv2.imread(imagePath)
            tip = imghdr.what(imagePath)
            if tip not in imageExts:
                images_to_remove.append(imagePath)
        except:
            print("Image Issue")

# Remove bad images
for image_path in images_to_remove:
    os.remove(image_path)

# Create model
num_classes = len(os.listdir(dataDir))
model = keras.models.Sequential()

model.add(layers.Conv2D(8, (3, 3), 1, activation='relu', input_shape=(256, 256, 3)))
model.add(layers.MaxPooling2D())
model.add(layers.Conv2D(16, (3, 3), 1, activation='relu'))
model.add(layers.MaxPooling2D())
model.add(layers.Conv2D(16, (3, 3), 1, activation='relu'))
model.add(layers.MaxPooling2D())
model.add(layers.Conv2D(16, (3, 3), 1, activation='relu'))
model.add(layers.MaxPooling2D())
model.add(layers.Conv2D(16, (3, 3), 1, activation='relu'))
model.add(layers.MaxPooling2D())

model.add(layers.Flatten())

model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dense(num_classes, activation='softmax'))

# Compile model
optimizer = keras.optimizers.Adam(learning_rate=0.01)
model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

# Display the model summary
model.summary()

# Train model
early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=8, restore_best_weights=True)
model.fit(train, epochs=100, validation_data=val, callbacks=[early_stopping])

# Evaluate model
test_loss, test_accuracy = model.evaluate(test)
print(f'Test Accuracy: {test_accuracy * 100:.2f}%')

# Save model
model.save("chemModel")