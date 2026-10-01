import os
import ssl
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
ssl._create_default_https_context = ssl._create_unverified_context

import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras import datasets, layers, models, Input

# -----------------------------------------------------------------
# Step A: Load and preprocess the MNIST dataset
# -----------------------------------------------------------------
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(f"  Training images shape: {x_train.shape}")
print(f"  Training labels shape: {y_train.shape}")
print(f"  Testing images shape:  {x_test.shape}")
print(f"  Testing labels shape:  {y_test.shape}")

# Normalize pixel values from 0-255 to 0-1 (helps gradient descent)
x_train = x_train / 255.0
x_test = x_test / 255.0

# Reshape to add the channel dimension expected by a CNN: (height, width, channels)
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

print(f"  After reshape - x_train: {x_train.shape}, x_test: {x_test.shape}")


# -----------------------------------------------------------------
# Step B: Display the first 10 digit images from the dataset
# -----------------------------------------------------------------
plt.figure(figsize=(12, 6))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(x_test[i].reshape(28, 28), cmap='gray')
    plt.title(f"Label: {y_test[i]}")
    plt.axis('off')
plt.suptitle("First 10 MNIST Test Images")
plt.show()

# -----------------------------------------------------------------
# Step C: Create a Sequential CNN model
# -----------------------------------------------------------------
# Convolutional base: Conv -> Pool -> Conv -> Pool -> Conv
model = models.Sequential([
    Input(shape=(28, 28, 1)),
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((1, 1)),
    layers.Conv2D(64, (2, 2), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.summary()


# -----------------------------------------------------------------
# Step D: Train the model on the training data
# -----------------------------------------------------------------
history = model.fit(
    x_train, y_train,
    epochs=5,
    batch_size=64,
    validation_split=0.2,
    verbose=2
)

# -----------------------------------------------------------------
# Step E: Evaluate the model on the test data
# -----------------------------------------------------------------
test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=2)
print(f"\nTest Loss:     {test_loss:.4f}")
print(f"Test Accuracy: {test_accuracy:.4f}")


# -----------------------------------------------------------------
# Step F: Generate predictions on the test data
# -----------------------------------------------------------------
predictions = model.predict(x_test)
print(f"\nExample prediction probabilities (image 0): {predictions[0]}")
print(f"Predicted class (image 0): {np.argmax(predictions[0])}")
print(f"Actual class    (image 0): {y_test[0]}")


# -----------------------------------------------------------------
# Step G: Display the first 10 test images WITH predictions
# -----------------------------------------------------------------
plt.figure(figsize=(12, 6))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(x_test[i].reshape(28, 28), cmap='gray')
    predicted_label = np.argmax(predictions[i])
    actual_label = y_test[i]
    color = 'green' if predicted_label == actual_label else 'red'
    plt.title(f"Predicted: {predicted_label} \n Actual: {actual_label}", color=color)
    plt.axis('off')
plt.suptitle("First 10 Test Images — Predicted vs Actual")
plt.show()