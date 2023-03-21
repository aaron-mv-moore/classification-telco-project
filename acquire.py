import env
import os
import pandas as pd

def get_telco_data():
    '''
    Argument: No arguments required
    Actions: 
        1. Checks for the existence of the telco csv in thw current directory
            a. if present:
                i. reads the csv
            b. if not present:
                i. queries MySQL dtabase using the env.py file for the credentials
                ii. saves the csv to the current working directory
    Return: telco churn dataframe
    Modules: pandas, os, env
    '''
    # a variable to hold the xpected or future file name
    filename = 'telco.csv'
    
    # if the file is present in the directory 
    if os.path.isfile(filename):
      
        # read the csv and assign it to the variable df
        df = pd.read_csv(filename)
        
        # return the dataframe and exit the funtion
        return df
    
    # if the file is not in the current working directory,
    else:
        # assign the name of the database to db
        db = 'telco_churn'
        
        # use the env.py function to get the url needed from the db
        url = env.get_db_url(db)
        
        # assign the sql query into the variable query
        query = '''SELECT *
            FROM customers c
            inner JOIN customer_contracts cc ON c.customer_id = cc.customer_id
            inner JOIN contract_types ct ON cc.contract_type_id = ct.contract_type_id
            inner JOIN internet_service_types ist ON c.internet_service_type_id = ist.internet_service_type_id
            inner JOIN customer_payments cp ON c.customer_id = cp.customer_id
            Inner JOIN payment_types pt ON cp.payment_type_id = pt.payment_type_id;'''
        
        # query sql using pandas function
        df = pd.read_sql(query, url, index_col='customer_id')
        
        # save the dataframe as a csv to the current working directory
        df.to_csv(filename)
        
        # returns the dataframe
        return df
    
