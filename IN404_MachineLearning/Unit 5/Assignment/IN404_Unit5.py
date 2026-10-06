import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
import sys

#Set working directory to the script's own folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))

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
    f = open("IN404_Unit5.txt", "a")


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
        if message2:
            for m in message2:
                print(m)
        print()
    #Print to file for assignment
    else:
        f.write(str(message1))
        if message2:
            for m in message2:
                f.write(str(m))
        f.write("\n\n")


#Widen the column display
pd.set_option('max_colwidth',500)

#Read reviews into a DataFrame
df1 = pd.read_csv('IN404_Unit5and6_1.csv', encoding='unicode-escape')
#Read reviews into a DataFrame
df2 = pd.read_csv('IN404_Unit5and6_2.csv', encoding='unicode-escape')


writeFunction("########## Dataframe 1 ############")

#Print top rows in dataframe 1
writeFunction("Top rows in dataframe 1")
writeFunction(df1.head(10))

#Print data types in dataframe 1
writeFunction("Data types in dataframe 1")
writeFunction(df1.dtypes)

#Print shape for dataframe 1
writeFunction("Shape for dataframe 1")
writeFunction(df1.shape)

#Print number of dimensions for dataframe 1
writeFunction("Number of dimensions for dataframe 1")
writeFunction(df1.ndim)

#Print the statistics for dataframe 1
writeFunction("Statistics for dataframe 1")
writeFunction(df1.describe())

#Print the max value for dataframe 1 number1 column
writeFunction("Max value for dataframe 1 number1 column")
writeFunction(df1['Number1'].max())

#Print the min value for dataframe 1 number1 column
writeFunction("Minimum value for dataframe 1 number1 column")
writeFunction(df1['Number1'].min())

#Print the max value for dataframe 1 date column
writeFunction("Max value for dataframe 1 date column")
writeFunction(df1['Date'].max())

#Print the min value for dataframe 1 date column
writeFunction("Minimum value for dataframe 1 date column")
writeFunction(df1['Date'].min())

#Print the count for dataframe 1 number1 column
writeFunction("Count for dataframe 1 number1 column")
writeFunction(df1['Number1'].value_counts())

#Print the count for dataframe 1 date column
writeFunction("Count for dataframe 1 date column")
writeFunction(df1['Date'].value_counts())

##########Dataframe 2################

writeFunction("########## Dataframe 2 ############")

#Print top rows in dataframe 2
writeFunction("Top rows in dataframe 2")
writeFunction(df2.head(10))

#Print data types  in dataframe 2
writeFunction("Data types in dataframe 2")
writeFunction(df2.dtypes)

#Print shape for dataframe 2
writeFunction("Shape for dataframe 2")
writeFunction(df2.shape)

#Print number of dimensions for dataframe 2
writeFunction("Number of dimensions for dataframe 2")
writeFunction(df2.ndim)

#Print the statistics for dataframe 2
writeFunction("Statistics for dataframe 2")
writeFunction(df2.describe())

#Print the max value for dataframe 2 number1 column
writeFunction("Max value for dataframe 2 number1 column")
writeFunction(df2['Number1'].max())

#Print the min value for dataframe 2 number1 column
writeFunction("Minimum value for dataframe 2 number1 column")
writeFunction(df2['Number1'].min())

#Print the max value for dataframe 2 number2 column
writeFunction("Max value for dataframe 2 number2 column")
writeFunction(df2['Number2'].max())

#Print the min value for dataframe 2 number2 column
writeFunction("Minimum value for dataframe 2 number2 column")
writeFunction(df2['Number2'].min())

#Print the count for dataframe 2 number1 column
writeFunction("Count for dataframe 2 number1 column")
writeFunction(df2['Number1'].value_counts())

#Print the count for dataframe 2 number2 column
writeFunction("Count for dataframe 2 number2 column")
writeFunction(df2['Number2'].value_counts())

###################################
#Convert object to datetime
df1['Date'] = pd.to_datetime(df1['Date'])

#Convert datetime to float
df1['DATE_NUM'] = (df1['Date'] - df1['Date'].min())  / np.timedelta64(1,'D')

writeFunction("########## Datetime converted to float ############")
#Print top rows in dataframe 1
writeFunction("Top rows in dataframe 1 after adding row for number-based dates")
writeFunction(df1.head(10))

#Print data types in dataframe 1
writeFunction("Data types in dataframe 1 after adding row for number-based dates")
writeFunction(df1.dtypes)

#Print shape for dataframe 1
writeFunction("Shape for dataframe 1")
writeFunction(df1.shape)

#Print number of dimensions for dataframe 1
writeFunction("Number of dimensions for dataframe 1")
writeFunction(df1.ndim)

#Print the statistics for dataframe 1
writeFunction("Statistics for dataframe 1 after adding row for number-based dates")
writeFunction(df1.describe())

#Print the max value for dataframe 1 number1 column
writeFunction("Max value for dataframe 1 number1 column")
writeFunction(df1['Number1'].max())

#Print the min value for dataframe 1 number1 column
writeFunction("Minimum value for dataframe 1 number1 column")
writeFunction(df1['Number1'].min())

#Print the max value for dataframe 1 date column
writeFunction("Max value for dataframe 1 date column")
writeFunction(df1['Date'].max())

#Print the min value for dataframe 1 date column
writeFunction("Minimum value for dataframe 1 date column")
writeFunction(df1['Date'].min())

#Print the count for dataframe 1 number1 column
writeFunction("Count for dataframe 1 number1 column")
writeFunction(df1['Number1'].value_counts())

#Print the count for dataframe 1 date column
writeFunction("Count for dataframe 1 date column")
writeFunction(df1['Date'].value_counts())

############### X ##########################

writeFunction("########## X ############")

#Define X
feature_cols = ['Number1','DATE_NUM']

#Add all rows from the feature columns into X
X = df1.loc[:, feature_cols]

#Print top rows in X
writeFunction("Top rows in X")
writeFunction(X.head(10))

#Print data types in X
writeFunction("Data types in X")
writeFunction(X.dtypes)

#Print shape for X
writeFunction("Shape for X")
writeFunction(X.shape)

#Print number of dimensions for X
writeFunction("Number of dimensions for X")
writeFunction(X.ndim)

#Print the statistics for X
writeFunction("Statistics for X")
writeFunction(X.describe())

#Print the max value for X number1 column
writeFunction("Max value for X number1 column")
writeFunction(X['Number1'].max())

#Print the min value for X number1 column
writeFunction("Minimum value for X number1 column")
writeFunction(X['Number1'].min())

#Print the max value for X date_num column
writeFunction("Max value for X date_num column")
writeFunction(X['DATE_NUM'].max())

#Print the min value for X date_num column
writeFunction("Minimum value for X date_num column")
writeFunction(X['DATE_NUM'].min())

#Print the count for X number1 column
writeFunction("Count for X number1 column")
writeFunction(X['Number1'].value_counts())

#Print the count for X date_num column
writeFunction("Count for X date_num column")
writeFunction(X['DATE_NUM'].value_counts())


############### y #######################

writeFunction("########## y ############")

#Define y
y = df2['Number1']

#Print top rows in y
writeFunction("Top rows in y")
writeFunction(y.head(10))

#Print data types in y
writeFunction("Data types in y")
writeFunction(y.dtypes)

#Print shape for y
writeFunction("Shape for y")
writeFunction(y.shape)

#Print number of dimensions for y
writeFunction("Number of dimensions for y")
writeFunction(y.ndim)

#Print the statistics for y
writeFunction("Statistics for y")
writeFunction(y.describe())

#Print the max value for y number1 column
writeFunction("Max value for y number1 column")
writeFunction(y.max())

#Print the min value for y number1 column
writeFunction("Minimum value for y number1 column")
writeFunction(y.min())

#Print the count for y number1 column
writeFunction("Count for y number1 column")
writeFunction(y.value_counts())

##################### TRAIN/TEST Split ################

writeFunction("########## Train/test split ############")

#Split the new DataFrame into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

############## X_train ################

writeFunction("########## X_train ############")

#Print top rows in X_train
writeFunction("Top rows in X_train")
writeFunction(X_train.head(10))

#Print data types in X_train
writeFunction("Data types in X_train")
writeFunction(X_train.dtypes)

#Print shape for X_train
writeFunction("Shape for X_train")
writeFunction(X_train.shape)

#Print number of dimensions for X_train
writeFunction("Number of dimensions for X_train")
writeFunction(X_train.ndim)

#Print the statistics for X_train
writeFunction("Statistics for X_train")
writeFunction(X_train.describe())

#Print the count for X_train number1 column
writeFunction("Count for X_train number1 column")
writeFunction(X_train['Number1'].value_counts())

#Print the count for X_train date_num column
writeFunction("Count for X_train date_num column")
writeFunction(X_train['DATE_NUM'].value_counts())

############### X_test ######################

writeFunction("########## X_test ############")

#Print top rows in X_test
writeFunction("Top rows in X_test")
writeFunction(X_test.head(10))

#Print data types in X_test
writeFunction("Data types in X_test")
writeFunction(X_test.dtypes)

#Print shape for X_test
writeFunction("Shape for X_test")
writeFunction(X_test.shape)

#Print number of dimensions for X_test
writeFunction("Number of dimensions for X_test")
writeFunction(X_test.ndim)

#Print the statistics for X_test
writeFunction("Statistics for X_test")
writeFunction(X_test.describe())

#Print the count for X_test number1 column
writeFunction("Count for X_test number1 column")
writeFunction(X_test['Number1'].value_counts())

#Print the count for X_test date_num column
writeFunction("Count for X_test date_num column")
writeFunction(X_test['DATE_NUM'].value_counts())

############### y_train ##################

writeFunction("########## y_train ############")

#Print top rows in y_train
writeFunction("Top rows in y_train")
writeFunction(y_train.head(10))

#Print data types in y_train
writeFunction("Data types in y_train")
writeFunction(y_train.dtypes)

#Print shape for y_train
writeFunction("Shape for y_train")
writeFunction(y_train.shape)

#Print number of dimensions for y_train
writeFunction("Number of dimensions for y_train")
writeFunction(y_train.ndim)

#Print the statistics for y_train
writeFunction("Statistics for y_train")
writeFunction(y_train.describe())

#Print the count for y_train number1 column
writeFunction("Count for y_train number1 column")
writeFunction(y_train.value_counts())

############## y_test ###################

writeFunction("########## y_test ############")

#Print top rows in y_test
writeFunction("Top rows in y_test")
writeFunction(y_test.head(10))

#Print data types in y_test
writeFunction("Data types in y_test")
writeFunction(y_test.dtypes)

#Print shape for y_test
writeFunction("Shape for y_test")
writeFunction(y_test.shape)

#Print number of dimensions for y_test
writeFunction("Number of dimensions for y_test")
writeFunction(y_test.ndim)

#Print the statistics for y_test
writeFunction("Statistics for y_test")
writeFunction(y_test.describe())

#Print the count for y_test number1 column
writeFunction("Count for y_test number1 column")
writeFunction(y_test.value_counts())


writeFunction("########## SVM  ############")
#Create a svm Classifier
# decision_function_shape'ovo', 'ovr', default='ovr'
# Whether to return a one-vs-rest ('ovr') decision function of
# shape (n_samples, n_classes) as all other classifiers,
# or the original one-vs-one ('ovo') decision function
# of libsvm which has shape (n_samples, n_classes * (n_classes - 1) / 2).
# However, one-vs-one ('ovo') is always used as multi-class strategy.
# Changed in version 0.19: decision_function_shape is 'ovr' by default.
# New in version 0.17: decision_function_shape='ovr' is recommended.
# Changed in version 0.17: Deprecated decision_function_shape='ovo' and None.
clf = svm.SVC(decision_function_shape='ovr')

#Train the model using the training sets
clf.fit(X_train, y_train)

#Print the SVM score
writeFunction("SVM score", clf.score(X, y))

#Open a file handle for assignment results.
if PRINT == False:
    f.close()
