import pandas as pd
import numpy as np
import scipy as sp
from sklearn.pipeline import Pipeline, FeatureUnion, make_pipeline, make_union
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_selection import SelectKBest
from sklearn.preprocessing import StandardScaler
from textblob import TextBlob, Word
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets, metrics
import logging
import tensorflow.compat.v1 as tf
tf.enable_eager_execution()
tf.get_logger().setLevel(logging.ERROR)
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
import sys

#Ignoring warnings
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")


#Set the writeFunction boolean
#True = write to concole
#False = write to file for assignment turnin
PRINT = True

#Open a file handle for assignment results.
if PRINT == False:
    f = open("IN404_Unit8.txt", "a")
###############################################
##
##PURPOSE: Write to console or file based on
##  the writeFunction variable
##      True = write to concole
##      False = write to file for assignment turnin
##
##INPUT: Message to write (message1)
##   Optional: message2
##
##OUTPUT: None
##
###############################################
def writeFunction(message1, *message2):

    #Print to console
    if PRINT:
        print(message1)
        print(message2)
        print()
    #Print to file for assignment
    else:
        f.write(str(message1))
        f.write(str(message2))
        f.write("\n\n")


#Read the IN404_Reviews.csv into a data frame
reviews = pd.read_csv('IN404_Reviews.csv', encoding='unicode-escape')

#Replace missing values with none
reviews.replace(['NaN', np.nan], 'none', inplace=True)

#Set a score column with a binary value: 1 or 0.
# If greater than 3-stars, then 1, if less then 0.
#################### YOUR CODE HERE ########################

#Define a function that accepts text and returns the polarity
def detect_sentiment(text):
    return TextBlob(text).sentiment.polarity

#Create a new DataFrame column for sentiment
reviews['sentiment'] = reviews.Review_Text.apply(detect_sentiment)

#Add a sentiment_score column where the sentiment is >= 0.15.
#  If greater, enter 1, if less enter 0.
#################### YOUR CODE HERE ########################

#Create a new data set where the rows witout reviews are removed.
new_reviews = reviews[(reviews.Review_Text != 'none')]

# Create a new DataFrame called reviews_best_worst
# that removes 3-star ratings
#################### YOUR CODE HERE ########################

#Create a new DataFrame column for sentiment
reviews_best_worst['sentiment_title'] = reviews_best_worst.Review_Title.apply(detect_sentiment)

# Use feature columns to predict stars, not just text & title
reviews_best_worst.drop(['Package_Name', 'App_Version', 'Language', 'Device', 'Date', 'Review_Title', 'sentiment_title'], inplace=True,  axis=1)

#Define X and y
X = reviews_best_worst.Review_Text
y = reviews_best_worst.score

#Split the new DataFrame into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2)

#Cross validate naive bayes models.
# Fit to the count vectorized text
# Fit over a 10-fold validation with accuracy.
vect = CountVectorizer()
all_dtm = vect.fit_transform(reviews_best_worst.Review_Text)
nb = MultinomialNB()
#################### YOUR CODE HERE ######################## mean = ?
writeFunction("The mean of CV on NB model", mean)


#Fit to the tfidfed text. Cross validate naive bayes models.
# Fit over a 10-fold validation with accuracy
vect = TfidfVectorizer()
all_dtm = vect.fit_transform(reviews_best_worst.Review_Text)
nb = MultinomialNB()
#################### YOUR CODE HERE ######################## mean = ?
writeFunction("The mean of CV on NB model using TF-IDF text", mean)



######### Scaling using the sentiment score and good/bad marker for sentiment #######

#Define X using sentiment score and sentiment columns
#  and y using score.
feature_cols = ['sentiment_score', 'sentiment']
X = reviews_best_worst[feature_cols]
y = reviews_best_worst.score

#Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

#Standardize X_train
scaler = StandardScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)

# Standard scalar does a basic z-score normalization
# So for each element, x, it computes z = (x - mean) / std
# This gives the entire series a mean and a standard deviation (and variance)

#First column of X_train_scaled
writeFunction("X_train scaled (first column - mean)", X_train_scaled[:, 0].mean())
writeFunction("X_train scaled (first column - std)", X_train_scaled[:, 0].std())

#Second column of X_train_scaled
#################### YOUR CODE HERE ########################
#################### YOUR CODE HERE ########################)

#Standardize X_test
X_test_scaled = scaler.transform(X_test)

#First column of X_test_scaled
writeFunction("X_train scaled after standardization (first column - mean)", X_test_scaled[:, 0].mean())
writeFunction("X_train scaled after standardization (first column - std)", X_test_scaled[:, 0].std())

#Second column of X_test_scaled
#################### YOUR CODE HERE ########################
#################### YOUR CODE HERE ########################

############### KNN #########################
#KNN accuracy on original data
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
#Predict on X_test
#################### YOUR CODE HERE ########################
writeFunction("KNN accuracy on original data",  metrics.accuracy_score(y_test, y_pred_class))

#KNN accuracy on scaled data
knn.fit(X_train_scaled, y_train)
#Predict on X_test
#################### YOUR CODE HERE ########################
writeFunction("KNN accuracy on scaled data", metrics.accuracy_score(y_test, y_pred_class))

#Make a pipeline that scales data and then runs a KNN with 3 neighbors
# cross validate your pipeline using cv=5 with accuracy metric
# Print the mean.
pipe = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=3))
writeFunction("Pipeline that scales data and then runs a KNN with 3 neighbors")
writeFunction(" cross validate your pipeline using cv=5 with accuracy metric")
#################### YOUR CODE HERE ########################

#Search for an optimal n_neighbors value using GridSearchCV
#Print the grid's best score and parameter
pipe = make_pipeline(StandardScaler(), KNeighborsClassifier())
neighbors_range = range(1, 21)
param_grid = dict(kneighborsclassifier__n_neighbors=neighbors_range)
grid = GridSearchCV(pipe, param_grid, cv=5, scoring='accuracy')
grid.fit(X, y)
#################### YOUR CODE HERE ######################## Print best score

#################### YOUR CODE HERE ######################## Print best parameter


############### TensorFlow #############################

#Declare feature_columns list
feature_columns = []

#Get tensor feature columns from X_train into list
for key in X_train.keys():
    feature_columns.append(tf.feature_column.numeric_column(key=key))

# Build 3 layer DNN with 10, 20, 10 units respectively.
# Classes = 2 because there are two outcomes.
#   1 = good and 0 = bad
# Optimizer is gradient-based optimization using Adagrad
classifier = tf.estimator.DNNClassifier(
                feature_columns= feature_columns,
                hidden_units=[10, 20, 10],
                optimizer="Adagrad",
                n_classes=2)

#Define function for taining
def train_input_fn(features, labels, batch_size):
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))
    dataset = dataset.shuffle(10).repeat().batch(batch_size)
    return dataset

#Train the model.
# Steps = 2000 Number of times to go over dataset
# Batches = 200
classifier.train(input_fn=lambda:train_input_fn(X_train, y_train,
                        200),steps=2000)

#Define a function for evaluations or predictions using tensorflow
def eval_input_fn(features, labels, batch_size):
    features=dict(features)
    if labels is None:
        inputs = features
    else:
        inputs = (features, labels)
    dataset = tf.data.Dataset.from_tensor_slices(inputs)
    assert batch_size is not None, "batch_size must not be None"
    dataset = dataset.batch(batch_size)

    return dataset

#Evaluate X_test and y_test using the eval_input_fun function
eval_result = classifier.evaluate(
    input_fn=lambda:eval_input_fn(X_test, y_test,400)
)

#Print the evaluation results
#################### YOUR CODE HERE ########################


#Setup predictions in dictionary
predict = {
    'sentiment_score': [0, 1, 1, 0],
    'sentiment': [-.5, .66, 0, -.25],
}

#Perform predictions on [0,-0.5], [1,.66], [1,0], and [0,-.25]
predictions = classifier.predict(
    input_fn=lambda:eval_input_fn(predict, labels=None, batch_size=200))

#Print the tensor prediction results
#  Classes hold the prediction.
#   1 = good and 0 = bad.
f#################### YOUR CODE HERE ########################


#Close a file handle for assignment results.
if PRINT == False:
    f.close()
