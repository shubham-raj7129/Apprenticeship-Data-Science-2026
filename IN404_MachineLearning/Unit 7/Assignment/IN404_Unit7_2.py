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
    f = open("IN404_Unit7_2.txt", "a")


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

#Replace NaN values with none
reviews.replace(['NaN', np.nan], 'none', inplace=True)

#Define a function that accepts text and returns the polarity
def detect_sentiment(text):
    return TextBlob(text).sentiment.polarity

#Add a new DataFrame column for sentiment
reviews['sentiment'] = reviews.Review_Text.apply(detect_sentiment)

#Find reviews with none
dt_reviews = reviews[(reviews.Review_Text != 'none')]

#Create a prediction column using the mean
dt_reviews['prediction'] = dt_reviews.sentiment.mean()

#Calculate RMSE for those predictions (uses sentiment and prediction)
writeFunction("RMSE for sentiments and predictions", np.sqrt(metrics.mean_squared_error(dt_reviews.sentiment, dt_reviews.prediction)))

#Define a function that calculates the RMSE for a given split of sentiment
def sentiment_split(sentiment):
    #Calculate the mean Star for sentiment under the sentiment split
    lower_sentiment_star = dt_reviews[dt_reviews.sentiment < sentiment].Star.mean()
    #Calculate the mean Star for sentiment above the sentiment split
    higher_sentiment_star = dt_reviews[dt_reviews.sentiment >= sentiment].Star.mean()

    #Slice the prediciotn column with mean star for sentiment
    dt_reviews['prediction'] = np.where(dt_reviews.sentiment < sentiment, lower_sentiment_star, higher_sentiment_star)

    #Return the RMSE using Star and prediction values
    RMSE = np.sqrt(metrics.mean_squared_error(dt_reviews.Star, dt_reviews.prediction))
    return RMSE


#Check sentiment splits using np.arange
# with range from -1.0 to 1.05 and a scale of 0.05
# Call the variable sentiment _range
sentiment_range = np.arange(-1.0, 1.05, 0.05)

#Print the sentiment range [:100]
writeFunction("Sentiment range", sentiment_range[:100])

#Get the RMSE value list
RMSE = [sentiment_split(sentiment) for sentiment in sentiment_range]


#Plot a line chart using the sentiment cutpoint versus RMSE
plt.plot(sentiment_range, RMSE)
plt.xlabel('Sentiment cutpoint')
plt.ylabel('RMSE (lower is better)')
plt.show()




