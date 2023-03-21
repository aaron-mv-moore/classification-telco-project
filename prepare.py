import pandas as pd
import numpy as np
from acquire import get_telco_data
from sklearn.model_selection import train_test_split

def clean_telco(df):
    '''
    Arguments: telco df 
    Actions:
        1. Assigns contents of duplicate columns to new columns with different names
        2. Drops unnecessary columns including duplicate columns and primary/foreign key columns
        3. Change data type of column from object to float
        4. Create a list of columns with object data types
        5. Create dummy variables for all object type data types
        6. Concatenates dummay variabels to original dataframe
    Returns: telco df prepared to be split
    '''
    # creating a list of duplicate columns ending with numbers which appears to be a signifier for a duplicate columns
    dupe_cols = df.columns[df.columns.str.endswith('1') | df.columns.str.endswith('2')].to_list()
    
    # dropping duplicates
    df = df.drop(columns=dupe_cols)
    
    # identifying the columns that end in '_id'
    id_cols_drop = [col for col in df if col[-3:] == '_id']
    
    # Drop unnecessary columns that have '_id'
    df = df.drop(columns=id_cols_drop)
    
    # Convert columns data type from object to float
    df['total_charges'] = (df['total_charges'] + '0').astype(float)
    
    return df


def split_data(df, target=None):
    '''
    Arguments: prepared dataframe, optional target - must be a string literal that is a column title
    Actions: 
        1. Splits the dataframe with 80% of the data assigned to tv and 20% assigned to test
        2. Splits the tv dataset with 70% of tv assigned to train and 30% assigned to validate
    Returns: 3 variables, each containing a portion
    Note: Order matters with variable assignment
    '''
    
    # when the target is a string that is a column title
    if target in df.columns.to_list():
        # the data is split 80/20 with the target used for stratification
        train_validate, test = train_test_split(df, train_size=.8, random_state = 1017,
                stratify = df[target])
        
         # splitting train_validate 70/30 with the target used for stratification
        train, validate = train_test_split(train_validate, train_size=.7, stratify=train_validate[target])
    # for all other targets
    else:
        # inform user that there is no stratification
        print('No stratification applied during the split')
        
        # split that data 80/20
        train_validate, test = train_test_split(df, train_size=.8, random_state = 1017)
        
        # splitting train_validate 70/30
        train, validate = train_test_split(train_validate, train_size=.7)
    
    return train, validate, test


def prep_telco(df, base_explore=True):
    '''
    Arguments: cleaned telco df
    Actions:
        1. Creates a dataframe with only dummy variables, numerical variables, and the target
        2. Formats all the column titles for python usability
        3. Splits data into train validate, and test with straitification on churn
    Return: train, validate, test
    '''
    
    if base_explore == True:
        
        pass
    
    else:
        # Create list of object type/categorical columns
        df_objects = [col for col in df if df[col].dtype == 'O' and col != 'churn']
        
        # Create dummy variables and add them to the df
        df = pd.concat([df, pd.get_dummies(df[df_objects], drop_first=True)], axis=1)
    
        # Create a list of all non-object variables and including the target churn
        num_cols = [col for col in df if df[col].dtype != 'O' or col == 'churn']

        # creating a df with only the variables needed for exploring and modeling
        df = df[num_cols]
    
    # editing the churn series to reflect 1,0 for yes and no
    df.churn.replace(['Yes', 'No'], [1, 0], inplace=True)
    
    # change the titles of the encoded variables to be python friendly
    df.columns = df.columns.str.lower().str.strip().str.replace(' ','_').str.replace('(','').str.replace(')','')
    
    # splits the df into train, validate, and test with a stratification on the target
    train, validate, test = split_data(df, target='churn')
    
    return train, validate, test
