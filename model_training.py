# Imports

import os
import numpy as np
import pandas as pd
import cv2
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt

# Load Dataset(Local)

BASE_FOLDER = "data_set"

train_df = pd.read_csv(os.path.join(BASE_FOLDER, "Train.csv"))
test_df  = pd.read_csv(os.path.join(BASE_FOLDER, "Test.csv"))
meta_df  = pd.read_csv(os.path.join(BASE_FOLDER, "Meta.csv"))

# Fix paths to images
train_df["Path"] = train_df["Path"].apply(lambda x: os.path.join(BASE_FOLDER, x))
test_df["Path"]  = test_df["Path"].apply(lambda x: os.path.join(BASE_FOLDER, x))


# Prepare Data

IMG_SIZE = (32, 32)

def load_images(df):
    images, labels = [], []
    for _, row in df.iterrows():
        img = cv2.imread(row["Path"])
        img = cv2.resize(img, IMG_SIZE)
        images.append(img)
        labels.append(row["ClassId"])
    return np.array(images), np.array(labels)

X, y = load_images(train_df)
X = X / 255.0
y = to_categorical(y, num_classes=len(meta_df))

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)


# Build CNN Model

model = models.Sequential([
    layers.Conv2D(32, (3,3), activation="relu", input_shape=(32,32,3)),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(64, (3,3), activation="relu"),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(128, (3,3), activation="relu"),
    layers.Flatten(),
    layers.Dense(256, activation="relu"),
    layers.Dropout(0.5),
    layers.Dense(len(meta_df), activation="softmax")
])

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
model.summary()


# Train Model

history = model.fit(
    X_train, y_train,
    epochs=15,
    batch_size=64,
    validation_data=(X_val, y_val)
)


#Save model

model.save("traffic_sign_cnn.h5")
print("Model saved as traffic_sign_cnn.h5")

# Save Training Graphs

plt.plot(history.history['accuracy'], label='Train Acc')
plt.plot(history.history['val_accuracy'], label='Val Acc')
plt.legend()
plt.savefig("static/accuracy.png")   #saved for frontend
plt.clf()

plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Val Loss')
plt.legend()
plt.savefig("static/loss.png")
print("Graphs saved in static/")
