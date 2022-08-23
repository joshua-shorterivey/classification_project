import pandas as pd
import os
from env import host, user, password

def get_telco_data():
    """
    purpose: initial acquisition and conversion of project data from codeup database
    ---
    inputs: none
    ---
    returns: pandas dataframe containing desired information
    """
    filename = "telco.csv"
    
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        sql = """
        SELECT * 
        FROM customers
        JOIN contract_types USING (contract_type_id)
        JOIN payment_types USING (payment_type_id)
        JOIN internet_service_types USING (internet_service_type_id)
        ;
        """

        url = f'mysql+pymysql://{user}:{password}@{host}/telco_churn'

        return pd.read_sql(sql, url)
