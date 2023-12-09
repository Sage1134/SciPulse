import openai
from dotenv import load_dotenv
import os
import tensorflow as tf
import numpy as np
import cv2

classLabels = ["peter lee", "cheetah", "parrot"]

# Load the model
model = tf.keras.models.load_model("classifiers/BioModel")

load_dotenv()
APIKEY = os.getenv("APIKEY")

openai.api_key = APIKEY

def getResponse(topic):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "physical facts about " + topic + ", shortest possible answer while maximizing the information, max 500 chars"}
        ]
    )

    return response.choices[0].message.content.strip()

def predict(imageFile):
    # Load the image
    im = cv2.imread(os.path.join("tempAssets", imageFile))

    # Decode the image using TensorFlow
    image = tf.image.decode_image(tf.io.encode_jpeg(im).numpy(), channels=3)

    # Resize the image
    resize = tf.image.resize(image, (256, 256))

    # Preprocess the image for prediction
    input_image = np.expand_dims(resize / 255.0, axis=0)

    # Make the prediction
    prediction = model.predict(input_image)

    # Get the index of the maximum probability
    predictedClassIndex = np.argmax(prediction)

    # Map the index back to the class label
    predictedClass = classLabels[predictedClassIndex]

    return getResponse(predictedClass)