import pandas as pd
import numpy as np

#models
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

#Visualization modules
import seaborn as sns
import matplotlib.pyplot as plt

#For ignoring warning
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
    f = open("IN404_Unit9.txt", "a")

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

######################
##
##
## Analyze the device installs versus the device uninstalls
##
## Uses linear regression, decision tree, and random forest
##
##
######################

#Get CSV data and put into a dataframe
col_names = ['Date','Package_Name','Daily_Device_Installs','Daily_Device_Uninstalls','Daily_Device_Upgrades','Total_User_Installs','Daily_User_Installs','Daily_User_Uninstalls']
data = pd.read_csv("IN404_Installs.csv", names=col_names)

#Print the top 4 rows
################# YOUR CODE HERE #######################

#Print the data set shape
################# YOUR CODE HERE #######################

#Plot a regression model fit across a FacetGrid using seaborn and data frame
sns.lmplot(x='Daily_Device_Installs', y='Daily_Device_Uninstalls', data=data, ci=None)
plt.title("Seaborn Plot")
plt.xlabel('Installs')
plt.ylabel('Uninstalls')
plt.show()

#Scatter plot using pandas
################# YOUR CODE HERE #######################
plt.title("Pandas Plot")
plt.xlabel("Installs")
plt.ylabel("Uninstalls")
plt.show()

#Linear Regression model and the data for uninstalls and install.
linreg = LinearRegression()
feature_cols = ["Daily_Device_Installs"]
X = data[feature_cols]
y = data.Daily_Device_Uninstalls
linreg.fit(X, y)

#Print the intercept
################# YOUR CODE HERE #######################

#Print the coefficient
################# YOUR CODE HERE #######################

#Get all values of X, and then plot those predictions connected by a line
di_pred = linreg.predict(X)

#Plot regression line with matplotlib and pandas
plt.scatter(data.Daily_Device_Installs, data.Daily_Device_Uninstalls)
plt.plot(data.Daily_Device_Installs, di_pred, color='red')
plt.title("Linear Regression Plot Using Predictions on X")
plt.xlabel("Installs")
plt.ylabel("Uninstalls")
plt.show()

#Predict how many unistalls for Android Mood Tracker will happen given X number of devices -- daily
#Use 25, 51, and 90 for three predictions
writeFunction("Linear regression predicted uninstalls based on 25 daily device install", linreg.predict([[25]]))

#Print the prediciton for 51 daily device installs
################# YOUR CODE HERE #######################

#Print the prediction for 90 daily device installs
################# YOUR CODE HERE #######################

#Train/test split 70% train, 30% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

#Build a decision tree model
tree = DecisionTreeClassifier(random_state=1)

#Fit the tree using X and y
################# YOUR CODE HERE #######################

#Print the accuracy of the tree
################# YOUR CODE HERE #######################

#Build a random forest tree model
rf=RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
rf.fit(X_train,y_train)

#Predict using X_test
y_pred=rf.predict(X_test)

#Print the random forest results for y_pred
################# YOUR CODE HERE #######################

#Print the accuracy for the random forest model
################# YOUR CODE HERE #######################

#Predict uninstalls for number of device install
#  Use 25, 51, 90
writeFunction("Random forest predicted uninstalls based on 25 daily device install is", rf.predict([[25]]))

#Print the prediction for 51 daily device installs
################# YOUR CODE HERE #######################

#Print the predicitomn for 90 daily device installs
################# YOUR CODE HERE #######################

#Close the file handle
if PRINT == False:
    f.close()
