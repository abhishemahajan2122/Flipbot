import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer

# Sample labeled data
data = [
    ("Blue T-Shirt", ["topwear"]),
    ("Denim Jeans", ["bottomwear", "denim"]),
    ("Red Skirt", ["bottomwear"]),
    ("Hoodie", ["topwear", "casual"]),
    ("Black Pants", ["bottomwear"]),
    ("White Blouse", ["topwear", "formal"]),
    ("Denim Jacket", ["topwear", "denim"])
]

# Separate data into features (X) and labels (y)
X = [item[0] for item in data]
y = [item[1] for item in data]

# Tokenize and pad sequences
tokenizer = Tokenizer()
tokenizer.fit_on_texts(X)
X_sequences = tokenizer.texts_to_sequences(X)
X_padded = pad_sequences(X_sequences)

# MultiLabelBinarizer for label encoding
mlb = MultiLabelBinarizer()
y_encoded = mlb.fit_transform(y)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X_padded, y_encoded, test_size=0.2, random_state=42)

# Build the model
model = keras.Sequential([
    keras.layers.Embedding(input_dim=len(
        tokenizer.word_index) + 1, output_dim=128, input_length=X_padded.shape[1]),
    keras.layers.GlobalAveragePooling1D(),
    keras.layers.Dense(64, activation='relu'),
    # Sigmoid for multi-label classification
    keras.layers.Dense(len(mlb.classes_), activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=10, batch_size=16,
          validation_data=(X_test, y_test))
example_text = ["Denim Bottomwear"]
example_sequence = tokenizer.texts_to_sequences(example_text)
example_padded = pad_sequences(example_sequence, maxlen=X_padded.shape[1])
predictions = model.predict(example_padded)

predicted_labels = mlb.classes_[predictions[0] > 0.1]
print("Predicted labels:", predicted_labels)
