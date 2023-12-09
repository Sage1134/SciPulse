import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

texts = ["This is a positive example.", "Negative sentiment in this one."]
labels = [1, 0]  # 1 for positive, 0 for negative

tokenizer = Tokenizer(oov_token="<OOV>")
tokenizer.fit_on_texts(texts)

sequences = tokenizer.texts_to_sequences(texts)
padded_sequences = pad_sequences(sequences, maxlen=100, padding="post", truncating="post")

model = Sequential()
model.add(Embedding(input_dim=10000, output_dim=100, input_length=100))
model.add(LSTM(100))
model.add(Dense(1, activation="sigmoid"))

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

model.fit(padded_sequences, labels, epochs=10, validation_split=0.2)

new_texts = ["Another positive example.", "A negative example."]
new_sequences = tokenizer.texts_to_sequences(new_texts)
new_padded_sequences = pad_sequences(new_sequences, maxlen=100, padding="post", truncating="post")

predictions = model.predict(new_padded_sequences)
