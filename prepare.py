import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

def prep_telco(df):
    """
    purpose: accepts pandas dataframe and prepares it for analysis according to spec
    ---
    inputs: pandas dataframe 
    ---
    returns: the prepared dataframe
    """
    df = df.drop(columns=['customer_id','internet_service_type_id', 'payment_type_id', 'contract_type_id'])
    
    df['gender_encoded'] = df.gender.map({'Female':1, 'Male':0})
    df['partner_encoded'] = df.partner.map({'Yes':1, 'No':0})
    df['dependents_encoded'] = df.dependents.map({'Yes':1, 'No':0})
    df['phone_service_encoded'] = df.phone_service.map({'Yes':1, 'No':0})
    df['paperless_billing_encoded'] = df.paperless_billing.map({'Yes':1, 'No':0})
    df['churn_encoded'] = df.churn.map({'Yes':1, 'No':0})

    dummy_telco = pd.get_dummies(df[['contract_type',\
                                    'payment_type', \
                                    'internet_service_type', \
                                    'multiple_lines', \
                                    'online_security',\
                                    'online_backup',\
                                    'device_protection',\
                                    'tech_support',\
                                    'streaming_tv',\
                                    'streaming_movies']],\
                                 dummy_na=False, drop_first=True)
    
    
    df = pd.concat([df, dummy_telco], axis=1)
    df.total_charges = pd.to_numeric(df.total_charges.str.strip())
    
    
    return df

def final_prep(df):
    """
    purpose: final clean up of column names before feeding into model
    ---
    inputs: a pandas dataframe
    ---
    returns: the prepared dataframe
    """
              
    df = df.select_dtypes(exclude='object')

    # rename binary encoded columns
    df.rename(columns={'gender_encoded': 'gender', 'partner_encoded': 'partner', \
                    'dependents_encoded': 'dependents', 'phone_service_encoded': 'phone_service', \
                    'paperless_billing_encoded': 'paperless_billing'})

    return df   

def split_data(df, target):
    """
    purpose: splits up data into apporiate subsets for modeling
    ---
    inputs: a pandas dataframe, the target variable to perform the split on
    ---
    returns: train, validate, and test subsets in form of pandas dataframes
    """
    
    train, test = train_test_split(df, test_size=.2, random_state=514, stratify=df[target])
    train, validate = train_test_split(train, test_size=.25, random_state=514, stratify=train[target])
    
    #verify shapes of prepared df, train, validate, and test subsets
    print(f'Prepared df: {df.shape}')
    print()
    print(f'Train: {train.shape}')
    print(f'Validate: {validate.shape}')
    print(f'Test: {test.shape}')
    
    return train, validate, test