# modules for tabular data
import pandas as pd
import numpy as np

# statistics package for hypothesis testing
from scipy import stats

# modeling packages
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

# model evaluation packages
from sklearn.metrics import classification_report, confusion_matrix

def chi_squared_dependent_cat_cols(train):
    '''
    Argument: teclo train data(encoded)
    Action:
        1. assigns target as churn
        2. Sets alpha to 0.05
        3. Loops through each columns in train datatset
        4. Conducts chi squred testing on each columns that are categorical, not churn, and not multipline lines
        5. If the p-value is less than alpha the columns will be added to a list of dependent columns
    Returns: list of categorical columns that are statistically significant
    Modules: scipy.stats as stats, pandas as pd
    '''

    # initlaize variables
    target = 'churn'

    # set slpha
    α = 0.05

    # intiailize blanks list
    dependent_cols = []

    # start for loop for columns in train ds
    for col in train:

        # control sructures to get categorical variables but excluding churn and mulitple_lines
        if train[col].nunique() < 10 and col != 'churn' and col != 'multiple_lines_yes':

            # bind cross tab results to observed  
            observed = pd.crosstab(train[target], train[col])

            # conducts contingency test and assigns outputs to respective variables
            chi2, p, degf, expected = stats.chi2_contingency(observed)

            # if p less than alphs
            if p < α:

                # add the columns to the initialized lost
                dependent_cols.append(col)

            # if p grater than alpha
            else:

                # skip the column
                pass

    # exit the function and return the lost of statistically significant columns            
    return dependent_cols

def model_prep(train, validate, test):
    '''
    Arguemnts: telco train, validate, test datasets
    Returns: X_train, y_train, X_val, y_val, X_test, y_test
    Modules: model, pandas as pd, 
    '''
    # gather list of variables used in modeling
    dependent_cat_cols = chi_squared_dependent_cat_cols(train)

    # creates x_train with select variables
    X_train = train[dependent_cat_cols]
    # creates y_train with target churn
    y_train = train.churn

    # create x validate df with selevt variables
    X_val = validate[dependent_cat_cols]
    # creates validate with churn
    y_val = validate.churn

    # creates test df with select columns
    X_test = test[dependent_cat_cols]
    # creates y test with churn
    y_test = test.churn

    # returns all variables 
    return X_train, y_train, X_val, y_val, X_test, y_test


def telco_best_rf(X_train, y_train, X_val, y_val):
    '''
    Arguments: X_train, y_train, X_val, y_val
    Actions: Uses a rf with a max depth of 4
    Returns: print statement with stats
    '''

    # initial model with  max depth of 4
    clf = RandomForestClassifier(max_depth=4)

    # fitting the model to the training ds
    clf.fit(X_train, y_train)

    # storing predicted values to the variable
    y_preds = clf.predict(X_train)  

    # getting confusiona matrix values
    tn, fn, fp, tp = confusion_matrix(y_train, y_preds).ravel()

    # calucalting the false negative rates
    fn_rate = fn / (fn + tp)
    # calcuatins the accuracy
    score = clf.score(X_train, y_train)

    # getting validate predicagtions
    y_val_preds = clf.predict(X_val)
    # getting validate confusion matrix values
    tn, fn, fp, tp = confusion_matrix(y_val, y_val_preds).ravel()
    # calculatinf validate treu negative rates
    fn_rate_val = fn / (fn + tp)

    # caluculating the false negative rrate difference
    fn_diff = fn_rate - fn_rate_val
    # calcualating the validate accuracy
    score_val = clf.score(X_val, y_val)
    # calculating the train and validate accuracy differe,ce
    score_diff = score - score_val

    # printing the results
    print(f'''
        Model: Random Forest | Max Depth 4
        
        False Negative on Train: {fn_rate:.2%}
        False Negative on Validate/Test: {fn_rate_val:.2%}
        False Negative Difference: {fn_diff:.2%}
        
        Accuracy on Train: {score:.2%}
        Accuracy on Validate/Test: {score_val:.2%}
        Accuracy Difference: {score_diff:.2%}
        ''')

    return


def telco_best_knn(X_train, y_train, X_val, y_val):
    '''
    Arguments: X_train, y_train, X_val, y_val
    Actions: Uses a knn with 18 nieghbors
    Returns: print statement with stats
    '''
    # initial model with  18 neighbors
    knn = KNeighborsClassifier(n_neighbors=18, weights='uniform')

    # fitting the model to the training ds
    knn.fit(X_train, y_train)

    # storing predicted values to the variable
    y_preds = knn.predict(X_train)

    # getting confusiona matrix values    
    tn, fn, fp, tp = confusion_matrix(y_train, y_preds).ravel()

    # calucalting the false negative rates
    fn_rate = fn / (fn + tp)

    # calculating the accuracy
    score = knn.score(X_train, y_train)
    
    # getting validate predictions
    y_val_preds = knn.predict(X_val)

    # getting validate confusion matrix values
    tn, fn, fp, tp = confusion_matrix(y_val, y_val_preds).ravel()

    # calculating validate true negative rates
    fn_rate_val = fn / (fn + tp)

    # caluculating the false negative rrate difference
    fn_diff = fn_rate - fn_rate_val
    #  calcualating the validate accuracy
    score_val = knn.score(X_val, y_val)
    # calculating the train and validate accuracy difference
    score_diff = score - score_val
    # printing the results
    print(f'''
        Model: KNN | 18 Neighbors
        
        False Negative on Train: {fn_rate:.2%}
        False Negative on Validate/Test: {fn_rate_val:.2%}
        False Negative Difference: {fn_diff:.2%}
        
        Accuracy on Train: {score:.2%}
        Accuracy on Validate/Test: {score_val:.2%}
        Accuracy Difference: {score_diff:.2%}
        ''')
    
    return

def telco_best_logit(X_train, y_train, X_val, y_val):
    '''
    Arguments: X_train, y_train, X_val, y_val
    Actions: Uses a logistic regression with a class of 0.01
    Returns: print statement with stats
    '''
    # initial model with  class of 0.01
    logit = LogisticRegression(C=.01)
    # fit model
    logit.fit(X_train, y_train)
    # predict on train
    y_preds = logit.predict(X_train)

    # getting confusion matrix values
    tn, fn, fp, tp = confusion_matrix(y_train, y_preds).ravel()
    # calculate fn rate
    fn_rate = fn / (fn + tp)
    # calculate score
    score = logit.score(X_train, y_train)

    # calculate validate predications
    y_val_preds = logit.predict(X_val)
    # getting confucion matrix values
    tn, fn, fp, tp = confusion_matrix(y_val, y_val_preds).ravel()
    # getting validate false negative rate
    fn_rate_val = fn / (fn + tp)

    # calculate false negative difference
    fn_diff = fn_rate - fn_rate_val
    # calculates validate accuracy
    score_val = logit.score(X_val, y_val)
    # calculatss accuracy differnces
    score_diff = score - score_val

        # prints results
    print(f'''
        Model: Logistic Regression
        
        False Negative on Train: {fn_rate:.2%}
        False Negative on Validate/Test: {fn_rate_val:.2%}
        False Negative Difference: {fn_diff:.2%}
        
        Accuracy on Train: {score:.2%}
        Accuracy on Validate/Test: {score_val:.2%}
        Accuracy Difference: {score_diff:.2%}
        ''')
    
    return
