import pandas as pd
import numpy as np
import scipy as sp
from sklearn.pipeline import Pipeline, FeatureUnion, make_pipeline, make_union
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from textblob import TextBlob, Word
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn import metrics
import sys


#Ignoring warnings
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

#Set the writeFunction boolean
#True = write to console
#False = write to file for assignment turnin
PRINT = True

#Open a file handle for assignment results.
if PRINT == False:
    f = open("IN404_Unit7_1.txt", "a")


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


#Read IN404_Reviews.csv into a DataFrame
reviews = pd.read_csv('IN404_Reviews.csv', encoding='unicode-escape')

#Set values as NaN to none
reviews.replace(['NaN', np.nan], 'none', inplace=True)

#Add a score column
reviews['score'] = np.where(reviews.Star > 3, 1, 0)

#Create new dataframe eliminating rows without reviews
new_reviews = reviews[(reviews.Review_Text != 'none')]

#Create a new DataFrame called reviews_best_worst that removes 3-star ratings
################# YOUR CODE HERE #########################

#Pipeline example using GridSearchCV
pipe = Pipeline([
  ('features', FeatureUnion([
        #With count vectorization
        ('counts', CountVectorizer()),
        #With TF-IDF
        ('tf_idf', TfidfVectorizer())
  ])),
    #With Multinomial Naive Bayes classification
  ('classifier', MultinomialNB())
])

#Find best n_neighbors value using GridSearchCV
gram_range = [(1, n) for n in range(1, 5)]
param_grid = {
    'features__counts__ngram_range': gram_range,
    'features__tf_idf__ngram_range': gram_range,
}

#Print the grid
################# YOUR CODE HERE #########################

#Get the accuracy score of the pipelined model
# Use cross validation of 5 and scoring to accuracy
################# YOUR CODE HERE #########################

#Fit the data set without 3-star ratings
# for Reviews_Test and score
################# YOUR CODE HERE #########################

#Print the grid's best score
################# YOUR CODE HERE #########################

#Print the grid's best parameter
################# YOUR CODE HERE #########################



