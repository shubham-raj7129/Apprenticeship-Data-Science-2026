import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
import sys
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix

import seaborn as sns
from mlxtend.plotting import plot_decision_regions

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
    f = open("IN404_Unit6.txt", "a")


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
df1 = pd.read_csv('IN404_Unit5and6_1.csv', encoding='unicode-escape')
#Read reviews into a DataFrame
df2 = pd.read_csv('IN404_Unit5and6_2.csv', encoding='unicode-escape')

#Plot frequency count over time
date_line = df1['Date'].value_counts().sort_index()
ax = date_line.plot(figsize=(12,6), title="Count by Time")
ax.set_xlabel("Date")
ax.set_ylabel("Frequency")
plt.show()

#Plot the numbers over time
count = df1.groupby(['Date', 'Number1']).size()
ax = count.plot(figsize=(12,6), title="Numbers over Time")
ax.set_xlabel("Date/Number")
ax.set_ylabel("Frequency")
plt.show()

#Bar chart showing number frequency
ax = df1['Number1'].value_counts().plot(kind='bar',
            figsize=(12,6),
            title="Frequency of Numbers")
ax.set_xlabel("Number")
ax.set_ylabel("Count")
plt.show()

#Convert object to datetime
df1['Date'] = pd.to_datetime(df1['Date'])

#Convert datetime to float
df1['DATE_NUM'] = (df1['Date'] - df1['Date'].min())  / np.timedelta64(1,'D')


############### X ##########################

#Define X
feature_cols = ['Number1','DATE_NUM']

#Add all rows from the feature columns into X
X = df1.loc[:, feature_cols]



############### y #######################

#Define y
y = df2['Number1']



##################### TRAIN/TEST Split ################

#Split the new DataFrame into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)


writeFunction("########## SVM  ############")
#Create a svm Classifier
# decision_function_shape‘ovo’, ‘ovr’, default=’ovr’
# Whether to return a one-vs-rest (‘ovr’) decision function of
# shape (n_samples, n_classes) as all other classifiers,
# or the original one-vs-one (‘ovo’) decision function
# of libsvm which has shape (n_samples, n_classes * (n_classes - 1) / 2).
# However, one-vs-one (‘ovo’) is always used as multi-class strategy.
# Changed in version 0.19: decision_function_shape is ‘ovr’ by default.
# New in version 0.17: decision_function_shape=’ovr’ is recommended.
# Changed in version 0.17: Deprecated decision_function_shape=’ovo’ and None.
clf = svm.SVC(decision_function_shape='ovr')

#Train the model using the training sets
clf.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)

#Print the prediction for the X_test set
writeFunction("Predict value", y_pred)

#Predict number 1 and day 0
writeFunction("Prediction for number 1, and day 0", clf.predict([[1,0]]))

#Predict number 1 and day 2
writeFunction("Prediction for number 1, and day 2", clf.predict([[1,2]]))

#Predict number 2 and day 2
writeFunction("Prediction for number 2, and day 2", clf.predict([[2,2]]))

#Predict number 3 and day 1
writeFunction("Prediction for number 3, and day 1", clf.predict([[3,1]]))

#Print the accuracy score
writeFunction("Accuracy score", metrics.accuracy_score(y_test, y_pred))

#Create and print the confusion matrix
writeFunction("Confusion matrix")
cm = confusion_matrix(y_test,y_pred)
writeFunction(cm)

#Plot the confusion matrix using matshow
plt.matshow(cm)
plt.title("Confusion Matrix")
plt.colorbar()
plt.show()

#Create and print the classification report
writeFunction("Classification report")
cr = classification_report(y_test,y_pred, output_dict=True)
writeFunction(cr)

#Plot the classification report using a heatmap
ax = plt.axes()
sns.heatmap(pd.DataFrame(cr).iloc[:-1, :].T, annot=True, ax=ax)
ax.set_title('Heatmap for Classification Report')
plt.show()


#Plot the decision boundaries using plot_decision_regions
plot_decision_regions(X=X.values,
                      y=y.values,
                      clf=clf,
                      legend=4)

# Update plot object with X/Y axis labels and Figure Title
plt.xlabel(X.columns[0], size=14)
plt.ylabel(X.columns[1], size=14)
plt.title('SVM Decision Regions', size=20)
plt.show()


#Visualize the scatter plot using scatter function in PyPlot
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=y, s=50, cmap='rainbow')
plt.xlabel(X.columns[0], size=14)
plt.ylabel(X.columns[1], size=14)
plt.title('Scatter Plot', size=20)
plt.colorbar();
plt.show()


#Open a file handle for assignment results.
if PRINT == False:
    f.close()
