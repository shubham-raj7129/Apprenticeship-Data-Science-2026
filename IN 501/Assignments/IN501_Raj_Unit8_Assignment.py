import ssl

import numpy as np
import tensorflow as tf


keras = tf.keras
layers = tf.keras.layers

# Hyperparameters for the IMDB sentiment analysis model
# NUM_WORDS limits vocabulary to the 10,000 most frequent words to reduce noise
NUM_WORDS = 10_000
# MAX_LEN ensures all reviews are the same length for batch processing
MAX_LEN = 200
BATCH_SIZE = 64
EPOCHS = 3


def decode_review(encoded_review, reverse_word_index):
	"""Converts a list of integer-encoded tokens back into human-readable text."""
	words = []
	for token in encoded_review:
		word = reverse_word_index.get(token, "?")
		words.append(word)
	return " ".join(words)


def main():
	# Allows Keras dataset download on environments with missing root certificates.
	ssl._create_default_https_context = ssl._create_unverified_context

	# --- Step 1: Data Loading and Preprocessing ---
	print("Step 1: Loading and preprocessing IMDB dataset...")

	# Load the IMDB dataset; each review is encoded as a sequence of word indices
	(x_train_raw, y_train), (x_test_raw, y_test) = keras.datasets.imdb.load_data(num_words=NUM_WORDS)

	# Pad or truncate sequences so every review has a uniform length of MAX_LEN.
	# This is required because LSTM layers expect fixed-length input sequences.
	x_train = keras.preprocessing.sequence.pad_sequences(
		x_train_raw,
		maxlen=MAX_LEN,
		padding="post",
		truncating="post",
	)
	x_test = keras.preprocessing.sequence.pad_sequences(
		x_test_raw,
		maxlen=MAX_LEN,
		padding="post",
		truncating="post",
	)

	print(f"Training samples: {len(x_train)}")
	print(f"Test samples: {len(x_test)}")

	# --- Step 2: Model Building ---
	print("\nStep 2: Building Sequential LSTM model...")

	# Build a Sequential model with stacked LSTM layers for learning temporal patterns.
	# Embedding layer maps word indices to dense 128-dimensional vectors.
	# Two LSTM layers capture short- and long-term dependencies in the text.
	# Dense output layer with sigmoid activation outputs a probability for binary classification.
	model = keras.Sequential(
		[
			layers.Embedding(input_dim=NUM_WORDS, output_dim=128),
			layers.LSTM(64, return_sequences=True),
			layers.LSTM(32),
			layers.Dense(1, activation="sigmoid"),
		]
	)

	# Compile with binary_crossentropy (standard for binary classification)
	# and the Adam optimizer for adaptive learning rate.
	model.compile(
		optimizer="adam",
		loss="binary_crossentropy",
		metrics=["accuracy"],
	)

	model.summary()

	# --- Step 3: Training and Evaluation ---
	print("\nStep 3: Training model...")

	# Train the model; 20% of training data is held out for validation to monitor overfitting.
	model.fit(
		x_train,
		y_train,
		epochs=EPOCHS,
		batch_size=BATCH_SIZE,
		validation_split=0.2,
		verbose=1,
	)

	print("\nStep 4: Evaluating on test data...")

	# Evaluate on unseen test data to measure generalization performance.
	test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=0)
	print(f"Test Loss: {test_loss:.4f}")
	print(f"Test Accuracy: {test_accuracy:.4f}")

	# --- Step 4: Sentiment Prediction on 5 Sample Reviews ---
	print("\nStep 5: Predicting sentiment for 5 sample reviews...")

	# Build a reverse word index to convert integer tokens back to words for display.
	# Indices 0-3 are reserved for special tokens (PAD, START, UNK, UNUSED).
	word_index = keras.datasets.imdb.get_word_index()
	reverse_word_index = {value + 3: key for key, value in word_index.items()}
	reverse_word_index[0] = "<PAD>"
	reverse_word_index[1] = "<START>"
	reverse_word_index[2] = "<UNK>"
	reverse_word_index[3] = "<UNUSED>"

	# Select 5 reviews from the test set and predict their sentiment.
	review_subset = x_test[:5]
	predictions = model.predict(review_subset, verbose=0)

	# Display the review text, predicted sentiment, and actual sentiment for comparison.
	for i in range(5):
		predicted_probability = float(predictions[i][0])
		predicted_sentiment = "positive" if predicted_probability >= 0.5 else "negative"
		actual_sentiment = "positive" if y_test[i] == 1 else "negative"

		review_text = decode_review(x_test_raw[i], reverse_word_index)

		print(f"\nReview {i + 1} Text:")
		print(review_text)
		print(f"Predicted Sentiment: {predicted_sentiment} ({predicted_probability:.4f})")
		print(f"Actual Sentiment: {actual_sentiment}")

	# --- Reminder: capture screenshots of this output for submission ---
	print("\nStep 6: Take screenshot(s) of this output window for submission.")


if __name__ == "__main__":
	# Set random seeds for reproducibility across runs
	np.random.seed(42)
	keras.utils.set_random_seed(42)
	main()
