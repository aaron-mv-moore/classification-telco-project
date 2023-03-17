import env
import os
import pandas as pd

def get_telco_data():
    '''
    This function a dataframe containing all the contract, payment, and internet service options for each customer.
    Assigns the customer_id as the index. 
    '''
    filename = 'telco.csv'
    
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        db = 'telco_churn'
        url = env.get_db_url(db)
        query = '''SELECT *
            FROM customers c
            LEFT JOIN customer_contracts cc ON c.customer_id = cc.customer_id
            LEFT JOIN contract_types ct ON cc.contract_type_id = ct.contract_type_id
            LEFT JOIN internet_service_types ist ON c.internet_service_type_id = ist.internet_service_type_id
            LEFT JOIN customer_payments cp ON c.customer_id = cp.customer_id
            LEFT JOIN payment_types pt ON cp.payment_type_id = pt.payment_type_id;'''
        return pd.read_sql(query, url, index_col='customer_id')
    
