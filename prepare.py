import pandas as pd
import numpy as np
import math
from acquire import get_telco_data

# import splitting and imputing functions
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

# turn off pink boxes for demo
import warnings
warnings.filterwarnings("ignore")

def clean_data():
    ''' 
    Function cleans and prepares Telco data frame and ensures clean and tidy data \
    before is split 
    '''
    df = get_telco_data()

    df = df.drop_duplicates() # Drop duplicates 
    df = df.drop(columns = ['customer_id']) # Data does not add value
     # Delete records withiut tota charges 
    null_total_charges = list(df[df.total_charges.str.contains(" ")].index)
    df = df.drop(null_total_charges)
    # turn total_charges from iobject datatype to float
    df["total_charges"] = pd.to_numeric(df["total_charges"])
    # Change gender to is Female. Columns only contains Male and Female
    # If Female record == 1 
    # If Male recorf == 0
    df['is_female'] = df.gender == "Female"
    df.is_female.replace([True, False], [1,0], inplace = True)
    df = df.drop(columns=['gender']) # Drop old redundant data
    # Chage `object` data type to 1 and 0 for values that represent boolean values
    # Change Yes ==> 1
    # Change No ==> 0
    df.partner.replace(['Yes', 'No'], [1,0], inplace = True)
    df.phone_service.replace(['Yes', 'No'], [1,0], inplace = True)
    df.dependents.replace(['Yes', 'No'], [1,0], inplace = True)
    df.paperless_billing.replace(['Yes', 'No'], [1,0], inplace = True)
    df.churn.replace(['Yes', 'No'], [1,0], inplace = True)
    # create a daframe that holds the values of n
    dummy_df = pd.get_dummies(df[['multiple_lines', \
                                    'online_security', \
                                    'online_backup', \
                                    'device_protection', \
                                    'tech_support', \
                                    'streaming_tv', \
                                    'streaming_movies', \
                                    'contract_type', \
                                    'internet_service_type', \
                                    'payment_type'] \
                                    ], dummy_na=False, drop_first=True)
    # Attach duumy vairiables to the original data frame
    df = pd.concat([df, dummy_df], axis=1)
    # Creates a column holding boolean values if customer has internet
    df['no_internet'] = df['device_protection_No internet service']
    # get all the columns that that indicate customer does not have internet
    no_internet_columns = [col for col in df.columns if 'No internet service' in col]
    # Drop all the colums that repete no_internet data
    for col in df.columns:
        for str in no_internet_columns:
            if str in col:
                del df[col]
    
    return df

# Creates a fucntion that train_validate_test_split the data 
# before using it in the exploratory phase
def train_validate_test_split(x):
    """
    This function returns three datasets labeld as train, validate, test
    Data is divided as follows:
    - train    = 50%
    - validate = 30%
    - test     = 20%
    """
    train_validate, test = train_test_split(x, test_size=.2, 
                                            random_state=123, 
                                            stratify=x.churn)
    
    # Split train_validate into train and validate datasets.
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123, 
                                   stratify=train_validate.churn)
    return train, validate, test