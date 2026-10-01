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


#Ignoring warnings
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

#Open a file handle for assignment results.
f = open("IN404_Unit3.txt", "a")
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


#Widen the column display
pd.set_option('max_colwidth',500)

#Read reviews into a DataFrame
reviews = pd.read_csv('IN404_Reviews.csv', encoding='unicode-escape')

#Print the first 5 rows in the data set
writeFunction("First 5 rows of the reviews from the data set")
writeFunction(reviews.head(5))

#Print the data frame dimensions
r = str(reviews.shape)
writeFunction("The dimensions of the data set", r)

#Notice the NaN representing not a number
#Replace them NaN with the work none
reviews.replace(['NaN', np.nan], 'none', inplace=True)

#Print the first 5 rows in the data set
writeFunction("First 5 rows after NaN replaced with none", reviews.head(5))


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


#Create a new DataFrame column for sentiment using the detectSentiment function
reviews['sentiment'] = reviews.Review_Text.apply(detectSentiment)

#Print the results with new sentiment column
writeFunction("Sentiment column added", reviews.head(5))

#Also print the dimensionals to show the 9th column was added
writeFunction("Dimensions with new sentiment column", reviews.shape)

#Create a new data set only filled with actual reviews
new_reviews = reviews[(reviews.Review_Text != 'none')]

#Print the dimensions of the new data set
writeFunction("The new reviews data set dimensions", new_reviews.shape)

#Print the first 5 rows of the sliced data set
writeFunction("New reviews data set", new_reviews.head(5))


#Make a box plot of sentiment grouped by stars
new_reviews.boxplot(column='sentiment', by='Star')
plt.show()

#Plot a histogram of review sentiment
#Mostly neutral sentiment
new_reviews['sentiment'].hist()
plt.show()

##########
# Display sentiment analysis results
#########

#Print the reviews with most positive sentiment
writeFunction("Most positive reviews by sentiment analysis")
writeFunction(new_reviews[new_reviews.sentiment == 1].Review_Text.head())

#Print the reviews with most negative sentiment, use -0.66.
writeFunction("Most negative reviews by sentiment analysis")
writeFunction(new_reviews[new_reviews.sentiment < -0.66].Review_Text.head())


#########
# Display sentiment analysis outliers
#########

#Negative sentiment in a 5-star review. Use 5 star & -0.3 sentiment values
writeFunction("Negative sentiment with 5 star rating")
writeFunction(new_reviews[(new_reviews.Star == 5) & (new_reviews.sentiment < -0.3)].head())

#Positive sentiment in a 1-star review. Use 5 star & 0.5 sentiment values.
writeFunction("Positive sentiment with 1 star rating")
writeFunction(new_reviews[(new_reviews.Star == 1) & (new_reviews.sentiment > 0.5)].head())



##########
##
##
##Can we create a model for predicting stars?
##
#########

#Define X and y
X = new_reviews.Review_Text
y = new_reviews.Star
writeFunction("Number of star ratings", y.value_counts())

#Split the new DataFrame into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

#Verify training set
writeFunction("Top rows of training set")
writeFunction(X_train.head())

#Verify testing set
writeFunction("Top rows of testing set")
writeFunction(X_test.head())

################
##
##Use CountVectorizer to create document-term matrices from X_train and X_test
##
################
vect = CountVectorizer()

#Fit and transform the training set
X_train_dtm = vect.fit_transform(X_train)

#Transform the training set
X_test_dtm = vect.transform(X_test)

#Rows are documents, columns are phrases
writeFunction ("Dimensions of the training set on line 172", X_train_dtm.shape)
writeFunction ("Dimensions of the testing set on line 173", X_test_dtm.shape)


#Print first 50 features
writeFunction ("First fifty features, or words, in the count vectorizer - line 177", vect.get_feature_names_out()[:50])


#Print last 50 features
writeFunction ("Last fifty features, or words, in the count vectorizer - line 181",vect.get_feature_names_out()[-50:])


#Show the count vectorizer options
writeFunction ("Current count vectorizer options",vect)

#Apply logistic regression on the new document-term matrices
logreg = LogisticRegression()
logreg.fit(X_train_dtm, y_train)
y_pred_class = logreg.predict(X_test_dtm)

#Calculate model accuracy
writeFunction ("Print the default count vectorizer accuracy metric - line 193", metrics.accuracy_score(y_test, y_pred_class))



#########
##
##Another count vectorizer model to not lowercase the words
##
########

#Create a count vectorizer that doesn't lowercase the words
vect = CountVectorizer(lowercase=False)

#Fit and transform X_train
X_train_dtm = vect.fit_transform(X_train)

#Print the dimensions after fit/transform for training set
writeFunction ("The new CV training set on line 219", X_train_dtm.shape)

#Transform the X_test data set
X_test_dtm = vect.transform(X_test)

#Print first 50 features
writeFunction ("First fifty features, or words, in the count vectorizer - line 225", vect.get_feature_names_out()[:50])

#Print the last fifty features
writeFunction ("Last fifty features, or words, in the count vectorizer - line 228", vect.get_feature_names_out()[-50:])

#Apply the logistic regression model with document-term feature matrix
logreg = LogisticRegression()
logreg.fit(X_train_dtm, y_train)
y_pred_class = logreg.predict(X_test_dtm)

#Print the model accuracy
writeFunction ("Print the no-lowercase count vectorizer accuracy metric - line 236", metrics.accuracy_score(y_test, y_pred_class))

#########
##
##Another count vectorizer model using 1-3 word combinations
##
########

#The lower and upper boundary of the range of n-values for different n-grams
#Includes 1-3 word combinations using ngram_range
vect = CountVectorizer(ngram_range=(1, 3))

#Fit and transform the training set
X_train_dtm = vect.fit_transform(X_train)

#Print the dimensions of the new training data set
writeFunction ("Dimensions of the new data set on line 252", X_train_dtm.shape)

#Transform X_test training set
X_test_dtm = vect.transform(X_test)

#Print the first 50 features
writeFunction ("First fifty features, or words, in the count vectorizer - line 258", vect.get_feature_names_out()[:50])

#Print the last fifty features
writeFunction ("Last fifty features, or words, in the count vectorizer - line 261", vect.get_feature_names_out()[-50:])

#Apply the logistic regression model with ngram document-term feature matrix
logreg = LogisticRegression()
logreg.fit(X_train_dtm, y_train)
y_pred_class = logreg.predict(X_test_dtm)

#Print the model accuracy
writeFunction ("Print the ngram count vectorizer accuracy metric - line 270", metrics.accuracy_score(y_test, y_pred_class))

#Calculate null model accuracy
y_test_binary = np.where(y_test==5, 1, 0)
writeFunction ("Null model accruacy - line 255", max(y_test_binary.mean(), 1 - y_test_binary.mean()))

f.close()
