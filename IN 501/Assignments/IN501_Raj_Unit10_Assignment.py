import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, random_split
from torchvision import datasets, transforms

# -----------------------------------------------------------------
# Step A: Load and preprocess the MNIST dataset
# -----------------------------------------------------------------
# ToTensor converts PIL images to float tensors in [0, 1].
# Normalize applies (pixel - mean) / std using the precomputed MNIST
# dataset-wide mean (0.1307) and standard deviation (0.3081), which
# centers the distribution around zero and improves gradient flow.
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

# Download/load the official 60 000-sample training set and 10 000-sample test set.
train_full = datasets.MNIST(root='./data', train=True,  download=True, transform=transform)
test_set   = datasets.MNIST(root='./data', train=False, download=True, transform=transform)

# Reserve 20 % of the training set as a validation split so we can
# monitor generalization performance after each epoch without touching
# the held-out test set.
val_size   = int(0.2 * len(train_full))
train_size = len(train_full) - val_size
train_set, val_set = random_split(train_full, [train_size, val_size])

# DataLoader wraps the datasets into iterable mini-batches.
# shuffle=True for training prevents the model from memorizing batch order.
train_loader = DataLoader(train_set, batch_size=64, shuffle=True)
val_loader   = DataLoader(val_set,   batch_size=64, shuffle=False)
test_loader  = DataLoader(test_set,  batch_size=64, shuffle=False)

print(f"Training samples:   {train_size}")
print(f"Validation samples: {val_size}")
print(f"Test samples:       {len(test_set)}")

# -----------------------------------------------------------------
# Step B: Display the first 10 digit images from the dataset
# -----------------------------------------------------------------
# Use a separate loader without normalization so pixel values stay in
# [0, 1] and the images render with natural contrast in Matplotlib.
raw_test = datasets.MNIST(root='./data', train=False, download=False,
                          transform=transforms.ToTensor())

plt.figure(figsize=(12, 6))
for i in range(10):
    image, label = raw_test[i]
    plt.subplot(2, 5, i + 1)
    plt.imshow(image.squeeze(), cmap='gray')  # squeeze removes the channel dim for display
    plt.title(f"Label: {label}")
    plt.axis('off')
plt.suptitle("First 10 MNIST Test Images")
plt.tight_layout()
plt.show()

# -----------------------------------------------------------------
# Step C: Create a Sequential CNN model
# -----------------------------------------------------------------
# nn.Sequential stacks layers in order, identical in concept to Keras Sequential.
# Architecture: two conv-pool blocks extract spatial features, a third conv
# refines them, then a fully connected head maps the features to 10 digit classes.
model = nn.Sequential(
    # --- Convolutional base ---
    nn.Conv2d(in_channels=1,  out_channels=32, kernel_size=3),  # 28x28 -> 26x26
    nn.ReLU(),                                                   # non-linear activation
    nn.MaxPool2d(kernel_size=2, stride=2),                       # 26x26 -> 13x13

    nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3),  # 13x13 -> 11x11
    nn.ReLU(),
    nn.MaxPool2d(kernel_size=2, stride=2),                       # 11x11 -> 5x5

    nn.Conv2d(in_channels=64, out_channels=64, kernel_size=2),  # 5x5   -> 4x4
    nn.ReLU(),

    # --- Classifier head ---
    nn.Flatten(),               # flatten 64 feature maps of 4x4 -> 1024-dim vector
    nn.Linear(64 * 4 * 4, 64), # fully connected layer reduces to 64 features
    nn.ReLU(),
    nn.Linear(64, 10)           # output layer: one logit per digit class (0-9)
)

# Move the model to GPU if available, otherwise run on CPU.
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model  = model.to(device)
print(f"\nUsing device: {device}")
print(model)

# CrossEntropyLoss combines log-softmax and negative log-likelihood in one step,
# making it the standard choice for multi-class classification with integer labels.
criterion = nn.CrossEntropyLoss()
# Adam adapts the learning rate per parameter, converging faster than plain SGD.
optimizer = optim.Adam(model.parameters(), lr=1e-3)

# -----------------------------------------------------------------
# Step D: Train the model on the training data
# -----------------------------------------------------------------
EPOCHS = 5  # number of full passes over the training set

for epoch in range(1, EPOCHS + 1):
    # --- Training phase ---
    model.train()  # enables dropout/batch-norm layers if present
    running_loss, correct, total = 0.0, 0, 0
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()          # clear gradients from the previous batch
        outputs = model(images)        # forward pass: compute predictions
        loss = criterion(outputs, labels)
        loss.backward()                # back-propagation: compute gradients
        optimizer.step()               # update model weights

        # Accumulate metrics scaled by batch size for a correct epoch average.
        running_loss += loss.item() * images.size(0)
        # argmax selects the class index with the highest logit as the prediction.
        correct      += (outputs.argmax(dim=1) == labels).sum().item()
        total        += images.size(0)

    train_loss = running_loss / total
    train_acc  = correct / total

    # --- Validation phase ---
    model.eval()  # disables gradient tracking layers
    val_loss, val_correct, val_total = 0.0, 0, 0
    with torch.no_grad():  # no_grad saves memory; gradients not needed for evaluation
        for images, labels in val_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            loss    = criterion(outputs, labels)
            val_loss    += loss.item() * images.size(0)
            val_correct += (outputs.argmax(dim=1) == labels).sum().item()
            val_total   += images.size(0)

    val_loss = val_loss / val_total
    val_acc  = val_correct / val_total

    print(f"Epoch {epoch}/{EPOCHS}  "
          f"Train Loss: {train_loss:.4f}  Train Acc: {train_acc:.4f}  "
          f"Val Loss: {val_loss:.4f}  Val Acc: {val_acc:.4f}")

# -----------------------------------------------------------------
# Step E: Evaluate the model on the test data
# -----------------------------------------------------------------
# Final evaluation uses only the held-out test set — data the model
# has never seen — to give an unbiased estimate of real-world accuracy.
model.eval()
test_loss, test_correct, test_total = 0.0, 0, 0
with torch.no_grad():
    for images, labels in test_loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        loss    = criterion(outputs, labels)
        test_loss    += loss.item() * images.size(0)
        test_correct += (outputs.argmax(dim=1) == labels).sum().item()
        test_total   += images.size(0)

# Divide by total samples to get the per-sample average loss and accuracy.
test_loss = test_loss / test_total
test_acc  = test_correct / test_total

print(f"\nTest Loss:     {test_loss:.4f}")
print(f"Test Accuracy: {test_acc:.4f}")

# -----------------------------------------------------------------
# Step F: Generate predictions on the test data
# -----------------------------------------------------------------
# Collect predictions for all 10 000 test images so Step G can look
# up the predicted class for any image by index.
all_preds, all_labels = [], []
model.eval()
with torch.no_grad():
    for images, labels in test_loader:
        outputs = model(images.to(device))
        # argmax returns the index of the highest logit = predicted digit.
        all_preds.extend(outputs.argmax(dim=1).cpu().numpy())
        all_labels.extend(labels.numpy())

all_preds  = np.array(all_preds)
all_labels = np.array(all_labels)

print(f"\nExample prediction (image 0): predicted={all_preds[0]}, actual={all_labels[0]}")

# -----------------------------------------------------------------
# Step G: Display first 10 test images WITH predictions
# -----------------------------------------------------------------
plt.figure(figsize=(12, 6))
for i in range(10):
    image, label = raw_test[i]
    predicted = all_preds[i]
    actual    = all_labels[i]
    # Green title = correct prediction; red = incorrect, making errors easy to spot.
    color     = 'green' if predicted == actual else 'red'

    plt.subplot(2, 5, i + 1)
    plt.imshow(image.squeeze(), cmap='gray')
    plt.title(f"Pred: {predicted}\nActual: {actual}", color=color)
    plt.axis('off')

plt.suptitle("First 10 Test Images — Predicted vs Actual")
plt.tight_layout()
plt.show()
