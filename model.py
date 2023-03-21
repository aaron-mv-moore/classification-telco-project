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
    Action:
    
    Modules: scipy.stats
    '''
    
    target = 'churn'
    α = 0.05
    dependent_cols = []
    for col in train:
        if train[col].nunique() < 10 and col != 'churn' and col != 'multiple_lines_yes':
            observed = pd.crosstab(train[target], train[col])
            chi2, p, degf, expected = stats.chi2_contingency(observed)
            if p < α:
                dependent_cols.append(col)
            else:
                pass
                
    return dependent_cols

def model_prep(train, validate, test):
    '''
    
    '''
    dependent_cat_cols = chi_squared_dependent_cat_cols(train)
    X_train = train[dependent_cat_cols]
    y_train = train.churn

    X_val = validate[dependent_cat_cols]
    y_val = validate.churn

    X_test = test[dependent_cat_cols]
    y_test = test.churn
    
    return X_train, y_train, X_val, y_val, X_test, y_test


def telco_best_rf(X_train, y_train, X_val, y_val):
    '''
    
    '''

    # initial model with min samp of 01 and max depth of 10
    clf = RandomForestClassifier(max_depth=4)

    # fitting the model to the training ds
    clf.fit(X_train, y_train)

    # storing predicted values to the variable
    y_preds = clf.predict(X_train)  

    tn, fn, fp, tp = confusion_matrix(y_train, y_preds).ravel()
    fn_rate = fn / (fn + tp)
    score = clf.score(X_train, y_train)


    y_val_preds = clf.predict(X_val)
    tn, fn, fp, tp = confusion_matrix(y_val, y_val_preds).ravel()
    fn_rate_val = fn / (fn + tp)

    fn_diff = fn_rate - fn_rate_val
    score_val = clf.score(X_val, y_val)
    score_diff = score - score_val
    
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
    
    '''
    
    knn = KNeighborsClassifier(n_neighbors=18, weights='uniform')
    knn.fit(X_train, y_train)
    y_preds = knn.predict(X_train)
    tn, fn, fp, tp = confusion_matrix(y_train, y_preds).ravel()
    fn_rate = fn / (fn + tp)
    score = knn.score(X_train, y_train)
    
    y_val_preds = knn.predict(X_val)
    tn, fn, fp, tp = confusion_matrix(y_val, y_val_preds).ravel()
    fn_rate_val = fn / (fn + tp)
    
    fn_diff = fn_rate - fn_rate_val
    score_val = knn.score(X_val, y_val)
    score_diff = score - score_val
    
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
    
    '''

    logit = LogisticRegression(C=.01)
    logit.fit(X_train, y_train)
    y_preds = logit.predict(X_train)
    tn, fn, fp, tp = confusion_matrix(y_train, y_preds).ravel()
    fn_rate = fn / (fn + tp)
    score = logit.score(X_train, y_train)

    y_val_preds = logit.predict(X_val)
    tn, fn, fp, tp = confusion_matrix(y_val, y_val_preds).ravel()
    fn_rate_val = fn / (fn + tp)

    fn_diff = fn_rate - fn_rate_val
    score_val = logit.score(X_val, y_val)
    score_diff = score - score_val

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
