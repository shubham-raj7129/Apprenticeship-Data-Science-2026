import pandas as pd
import numpy as np
import scipy as sp
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from textblob import TextBlob, Word
from nltk.stem.snowball import SnowballStemmer
import matplotlib.pyplot as plt
import sys
import os

#Ignoring warnings
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

#Set working directory to the script's folder so relative paths work
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Open a file handle for assignment results.
f = open("IN404_Unit4.txt", "a")
#Set the writeFunction boolean
#True = write to concole
#False = write to file for assignment turnin
PRINT = True

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
def _fmt(val):
    """Format a value for readable output."""
    if isinstance(val, float) or type(val).__name__ == 'float64':
        if 0 < val < 1:                       # accuracy score → percentage
            return f"{val * 100:.2f}%"
        return f"{val:.4f}"
    if isinstance(val, tuple) and len(val) == 2:   # shape tuple → rows x cols
        return f"{val[0]} rows x {val[1]} columns"
    return str(val)

def writeFunction(message1, *message2):

    #Print to console
    if PRINT:
        if message2:
            print(f"  {message1}  {_fmt(message2[0])}")
        else:
            print(message1)
        print()
    #Print to file for assignment
    else:
        f.write(str(message1))
        if message2:
            f.write(" " + _fmt(message2[0]))
        f.write("\n\n")

###############################################
##
##PURPOSE: Function to get sentiment
##
##INPUT: Review text
##
##OUTPUT: Senitment polarity
##
###############################################
def detectSentiment(review):
    return TextBlob(review).sentiment.polarity

#Widen the column display
pd.set_option('max_colwidth',500)

#Read reviews into a DataFrame
reviews = pd.read_csv('IN404_Reviews.csv', encoding='unicode-escape')

#Notice the NaN representing not a number
#Replace them NaN with the work none
reviews.replace(['NaN', np.nan], 'none', inplace=True)

#Create a new DataFrame column for sentiment using the detectSentiment function
reviews['sentiment'] = reviews.Review_Text.apply(detectSentiment)

#Create a new data set only filled with actual reviews
new_reviews = reviews[(reviews.Review_Text != 'none')]

X = new_reviews.Review_Text
y = new_reviews.Star
writeFunction("Number of star ratings\n", y.value_counts())

#Split the new DataFrame into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

#Verify training set
writeFunction("Top rows of training set")
writeFunction(X_train.head())

#Verify testing set
writeFunction("Top rows of testing set")
writeFunction(X_test.head())

###############
##
##
## Nothing beat the null model, so we need to try more
##
##
###############

###############
## Reduce the features
###############
#Create a new DataFrame called reviews_best_worst
# that only contains the 5-star and 1-star reviews
reviews_best_worst = new_reviews[(new_reviews.Star==5) | (new_reviews.Star==1)]

#Print the dimensions
writeFunction ("Print best_worst reviews data set dimensions")
writeFunction (reviews_best_worst.shape)

#Create a new DataFrame column for sentiment title
reviews_best_worst['sentiment_title'] = reviews_best_worst.Review_Title.apply(detectSentiment)

#Print the dimensions
writeFunction ("Print best_worst reviews data set dimensions")
writeFunction (reviews_best_worst.shape)

#Define X and y
X = reviews_best_worst.Review_Text
y = reviews_best_worst.Star
writeFunction ( y.value_counts())

#Do a train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2)


###############
## Default count vectorizer
###############
#Apply default CountVectorizer
print("=" * 60)
print("  SECTION 1: TRAIN/TEST SPLIT MODELS (Reduced Data Set)")
print("=" * 60)
print()
vect = CountVectorizer()
X_train_dtm = vect.fit_transform(X_train)
X_test_dtm = vect.transform(X_test)


# rows are documents, columns are terms (phrases) (aka "tokens" or "features")
writeFunction("Training set", X_train_dtm.shape)
writeFunction("Testing set", X_test_dtm.shape)


# use logistic regression with document feature matrix
logreg = LogisticRegression()
logreg.fit(X_train_dtm, y_train)
y_pred_class = logreg.predict(X_test_dtm)

# calculate accuracy
writeFunction ("Default count vectorizer on reduced data set", metrics.accuracy_score(y_test, y_pred_class))


###############
## Count vectorizer that does not lowercase words
###############
#Create a count vectorizer that doesn't lowercase the words
vect = CountVectorizer(lowercase=False)

#Transform and fit testing set
X_train_dtm = vect.fit_transform(X_train)

#Print dimensions
writeFunction("Training set - no lowercase", X_train_dtm.shape)

#Transform test set
X_test_dtm = vect.transform(X_test)

#Apply logistic regression
logreg = LogisticRegression()
logreg.fit(X_train_dtm, y_train)
y_pred_class = logreg.predict(X_test_dtm)

#Print accuracy
writeFunction ("Reduced data set no lowercase applied", metrics.accuracy_score(y_test, y_pred_class))


###############
## Count vectorizer using ngrams 1-3
###############
#Count vectorization using 1-3 word combination
vect = CountVectorizer(ngram_range=(1, 3))

#Transform and fit the training set
X_train_dtm = vect.fit_transform(X_train)

#Print the new dimensions
writeFunction ("Reduced data set with 1-3 ngrams", X_train_dtm.shape)

#Transform the testing set
X_test_dtm = vect.transform(X_test)

#Apply logistic regression
logreg = LogisticRegression()
logreg.fit(X_train_dtm, y_train)
y_pred_class = logreg.predict(X_test_dtm)

#Print accuracy
writeFunction ("Accuracy for reduced data set and 1-3 ngrams", metrics.accuracy_score(y_test, y_pred_class))

###############
## Null model on new reduced data set
###############
#Calculate null accuracy on reduced data set
print("=" * 60)
print("  SECTION 2: NULL MODEL BASELINE")
print("=" * 60)
print()
y_test_binary = np.where(y_test==5, 1, 0)
writeFunction ("Null model accuracy (majority class baseline)", max(y_test_binary.mean(), 1 - y_test_binary.mean()))


###############################################
##
##PURPOSE: Function to get accuracy score.
## Performs logistic regression in a function.
## Determines the dimensions and accuracy
## Uses cross validation.
##
##INPUT: Message to print and the algorithm to test
##
##OUTPUT: Nothing
##
###############################################
def testVector(message, vect):
    logreg = LogisticRegression()
    X_dtm = vect.fit_transform(X)
    acc = cross_val_score(logreg, X_dtm, y, cv=5, scoring='accuracy').mean()
    print(f"  ┌─ {message}")
    print(f"  │  Dimensions:  {X_dtm.shape[1]:,} features")
    print(f"  │  Accuracy:    {acc * 100:.2f}%")
    print(f"  └─────────────────────────────────────────")
    print()
    if not PRINT:
        f.write(f"{message}\n  Dimensions: {X_dtm.shape[1]}\n  Accuracy: {acc * 100:.2f}%\n\n")


###############
## Count vectorizer with 1-3 ngrams and using cross validation
###############
#Try count vectorization using 1-grams, 2-grams, and 3-grams
print("=" * 60)
print("  SECTION 3: CROSS-VALIDATED CountVectorizer MODELS")
print("=" * 60)
print()
vect = CountVectorizer(ngram_range=(1, 3))
testVector("Ngram 1-3 model", vect)


###############
## Count vectorizer removing english stop words, 1-3 ngrams, and cross validation
###############
#Remove English stop words
vect = CountVectorizer(stop_words='english', ngram_range=(1, 3))
testVector("Ngram 1-3 & english stop words", vect)

###############
## Count vectorizer removing english stop words, 250 features, and cross validation
###############
#Remove English stop words and only keep 250 features
vect = CountVectorizer(stop_words='english', max_features=250)
testVector("English stop words and features = 250", vect)

###############
## Count vectorizer 1-3 ngrams, 250 features, and cross validation
###############
#Include 1-grams to 3-grams, and limit the number of features
vect = CountVectorizer(ngram_range=(1, 3), max_features=250)
testVector("Ngram 1-3 & features = 250", vect)

###############
## Count vectorizer 1-3 ngrams, word must appear at least 3 times, and cross validation
###############
# include 1-grams to 3-grams, and only include terms that appear at least 3 times
vect = CountVectorizer(ngram_range=(1, 3), min_df=3)
testVector("Ngrams 1-3 & terms appear at least three times", vect)


###############
## Default TF-IDF
###############
#Using Term Frequency - Inverse Document Frequency
print("=" * 60)
print("  SECTION 4: CROSS-VALIDATED TF-IDF MODELS")
print("=" * 60)
print()
vect = TfidfVectorizer()
dtm = vect.fit_transform(new_reviews.Review_Text)
features = vect.get_feature_names_out()
dtm.shape
testVector("Default TF-IDF", vect)

###############
## TF-IDF with english stop words removed
###############
#Using Term Frequency - Inverse Document Frequency
vect = TfidfVectorizer(stop_words='english')
dtm = vect.fit_transform(new_reviews.Review_Text)
features = vect.get_feature_names_out()
dtm.shape
testVector("TF-IDF removing english stop words", vect)

###############
## TF-IDF with 1-3 ngrams
###############
#Using Term Frequency - Inverse Document Frequency
vect = TfidfVectorizer(ngram_range=(1, 3))
dtm = vect.fit_transform(new_reviews.Review_Text)
features = vect.get_feature_names_out()
dtm.shape
testVector("TF-IDF 1-3 ngrams", vect)

###############
## TF-IDF with 1-2 ngrams
###############
#Using Term Frequency - Inverse Document Frequency
vect = TfidfVectorizer(ngram_range=(1, 2))
dtm = vect.fit_transform(new_reviews.Review_Text)
features = vect.get_feature_names_out()
dtm.shape
testVector("TF-IDF 1-2 ngrams", vect)

###############
## TF-IDF with words appearing at least 3 times
###############
#Using Term Frequency - Inverse Document Frequency
vect = TfidfVectorizer(min_df=3)
dtm = vect.fit_transform(new_reviews.Review_Text)
features = vect.get_feature_names_out()
dtm.shape
testVector("TF-IDF 3 words", vect)


#################
#
# Accuracy is not changing using TF-IDF
#
#################


###############
## Reducing the data set to 4 columns
###############
#Define a new X and y using a reduced feature set
print("=" * 60)
print("  SECTION 5: FINAL REDUCED FEATURE SET (4 Columns)")
print("=" * 60)
print()
feature_cols = ['Review_Text', 'Review_Title', 'sentiment', 'sentiment_title']
X = reviews_best_worst[feature_cols]
y = reviews_best_worst.Star

#Perform tran/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

###############
## Default count vectorizer
###############
#Apply default CountVectorizer with text column only
vect = CountVectorizer()

#Transform and fit the training set
X_train_dtm = vect.fit_transform(X_train.Review_Text)

#Transform the testing set
X_test_dtm = vect.transform(X_test.Review_Text)

#Print the dimensions of the training set
writeFunction ("Final training set dimensions", X_train_dtm.shape)

#Print the dimensions of the testing set
writeFunction ("Final testing set dimensions", X_test_dtm.shape)

#Apply logistic regression model with text column only
logreg = LogisticRegression()
logreg.fit(X_train_dtm, y_train)
y_pred_class = logreg.predict(X_test_dtm)

#Print accuracy
writeFunction ("Final reduced data set accuracy", metrics.accuracy_score(y_test, y_pred_class))

f.close()
