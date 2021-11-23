import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# import splitting and imputing functions
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

# turn off pink boxes for demo
import warnings
warnings.filterwarnings("ignore")

def clean_telco(df):
    ''' 
    Function cleans and prepares Telco data frame and ensures clean and tidy data \
    before is split 
    '''
    
    # Drop unnecessary columns
    
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



def clean_telco(df):

    #df = acquire.get_telco_data() # grabbing the telco data
    df = df.drop_duplicates() # Dropping Duplicates
    df = df.drop(columns = ['customer_id']) # Don't need this column
    
    # If total charges are null, then remove the entire row 
    list_of_null_indexs = list(df[df.total_charges.str.contains(" ")].index)
    df = df.drop(list_of_null_indexs)
    
    # Convert total_charges from datatype object to float
    total_charges = df.total_charges.astype("float")
    df = df.drop(columns='total_charges')
    df = pd.concat([df, total_charges], axis = 1)
    
    # In the three lines below are mapping out the current values for what they actually represent.
    payment = df.payment_type_id.map({1: 'Electronic check', 2: 'Mailed check', 3:'Bank transfer', 4:'Credit card'})
    internet = df.internet_service_type_id.map({1: 'DSL', 2: 'Fiber optic', 3:'None'})
    contract = df.contract_type_id .map({1: 'Month-to-month', 2: 'One year', 3:'Two year'})
    senior = df.senior_citizen.map({1: "Yes", 0: "No"})
    
    # In the three lines below im adding each series to my dataframe and renaming the columns
    df = pd.concat([df, payment.rename("payment")], axis = 1)
    df = pd.concat([df, internet.rename("internet_service")], axis = 1)
    df = pd.concat([df, contract.rename("contract")], axis = 1)
    df = pd.concat([df, senior.rename("senior")], axis = 1)
    
    df = df.drop(columns=['payment_type_id', 'payment_type_id.1','contract_type_id', 'contract_type_id.1', 'payment_type' ,'internet_service_type','internet_service_type_id', 'internet_service_type_id.1']) # Dropping old and duplicate columns
    
    boolean = df.nunique()[df.nunique() <= 2].index # boolean is a list of columns who's values are either true/false or 1/0

    # In the line below, I am making dummies for all the boolean columns.  Dropping the first so I dont get two columns back
    boolean_dummy = pd.get_dummies(df[boolean], drop_first=[True, True, True, True, True, True, True])
    
    # Adding my encoded boolean_dummy DataFrame back to my original Data Frame
    df = pd.concat([df, boolean_dummy], axis = 1)

    # Dropping the none encoded columns
    df = df.drop(columns=boolean) 
    
    # In the line below, I am grabbing all the categorical columns(that are greater than 2) and saving the values into categ as a list
    categ = df.nunique()[(df.nunique() > 2) & (df.nunique() < 5)].index

    # Grabbing dummies, this time dont drop the first columns.
    categ_dummy = pd.get_dummies(df[categ]) # Grabbing dummies, this time dont drop the first columns.
    
    
    df = pd.concat([df, categ_dummy], axis = 1) # Adding my encoded categ_dummy DataFrame back to my original Data Frame
    df = df.drop(columns=categ)  # Dropping the none encoded columns
    
    df = df.rename(columns={'churn_Yes': 'churn'})
    return df
