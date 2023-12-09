import tensorflow as tf
import os
import keras
from keras import layers
import os
import cv2
import imghdr

os.environ['TF_CPP_MIN_LOG_LEVEL'] = "2" 

gpus = tf.config.experimental.list_physical_devices("GPU")
for gpu in gpus:
  tf.config.experimental.set_memory_growth(gpu, True)

dataDir = "Data"
imageExts = ["jpeg", "jpg", "bmp", "png"]
counter = 0

# Load data with image size specified
data = tf.keras.utils.image_dataset_from_directory("Data", label_mode="categorical", image_size=(256, 256))

# Normalize Data
data = data.map(lambda x, y: (x / 255, y))

# Apply data augmentation to the training set
train_size = int(len(data) * 0.7)
val_size = int(len(data) * 0.2)
test_size = int(len(data) * 0.1)

train = data.take(train_size)
val = data.skip(train_size).take(val_size)
test = data.skip(train_size + val_size).take(test_size)

# Create a list of images to remove
images_to_remove = []

for imageClass in os.listdir(dataDir):
    for image in os.listdir(os.path.join(dataDir, imageClass)):
        print(counter)
        imagePath = os.path.join(dataDir, imageClass, image)
        try:
            img = cv2.imread(imagePath)
            tip = imghdr.what(imagePath)
            if tip not in imageExts:
                images_to_remove.append(imagePath)
        except:
            print("Image Issue")

# Remove images
for image_path in images_to_remove:
    os.remove(image_path)

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

# Compile the model with a specified learning rate
optimizer = keras.optimizers.Adam(learning_rate=0.001)
model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

# Display the model summary
model.summary()

# Training with early stopping
early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
model.fit(train, epochs=32, validation_data=val, callbacks=[early_stopping])

# Evaluate the model on the test set
test_loss, test_accuracy = model.evaluate(test)
print(f'Test Accuracy: {test_accuracy * 100:.2f}%')

model.save("BioModel")