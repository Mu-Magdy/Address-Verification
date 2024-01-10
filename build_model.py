import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

data = pd.read_csv("labeled_addresses.csv", index_col=False)

train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(train_data["address"])

X_train = tokenizer.texts_to_sequences(train_data["address"])
X_test = tokenizer.texts_to_sequences(test_data["address"])

X_train = tf.keras.preprocessing.sequence.pad_sequences(X_train, padding="post")
X_test = tf.keras.preprocessing.sequence.pad_sequences(X_test, padding="post")

y_train = train_data["label"].values
y_test = test_data["label"].values


model = models.Sequential()
model.add(
    layers.Embedding(
        input_dim=len(tokenizer.word_index) + 1,
        output_dim=50,
        input_length=X_train.shape[1],
    )
)
model.add(layers.Flatten())
model.add(layers.Dense(64, activation="relu"))
model.add(layers.Dense(1, activation="sigmoid"))

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

accuracy = model.evaluate(X_test, y_test)[1]
print(f"Test Accuracy: {accuracy * 100:.2f}%")


model.save("address_verification_model_v1.h5")
