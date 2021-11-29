# Telco Classification Project
---------------
## Objectives 

- Document code, process, findings, and key takeaways in a Jupyter Notebook Final Report.
    - Data Science Pipeline
        - Planning
        - Acquisition
        - Preparation
        - Exploration and Pre-processing
        - Modeling
        - Delivery   
    - Data acquistion
    - Preparation 
    - Exploratory data analysis
    - Statistical testing
    - Modeling
    - Model evaluation)
    
- Create modules 
  - acquire.py
  - prepare.py 
  
- Construct a model to predict customer churn using classification techniques, and make predictions for a group of customers. 

- 5 minute presentation to a group of collegues and managers about the work you did, why, goals, what you found, your methdologies, and your conclusions.

 
 <br><br><br><br><br><br><br><br><br>

----------------------------------------------------------
# Business Goals

- Find drivers for customer churn at Telco. Why are customers churning?

- Construct a ML classification model that accurately predicts customer churn.

- Deliver a report that a non-data scientist can read through and understand what steps were taken, why and what was the outcome?  

 <br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

# Initial Questions

- Fiber optic is causing churn. Are there any other services related to fiber optics that are driving churn?

- Is people getting beneficiary tratment for singnig a 2 year contract?

-  Is the payment methode related to churn?

- Are online do different services relate to churn?

 <br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

## Acquire Data

Use file `acquire.py` that will upload data to the final noteboolk.

|idx  |Feature                           |Not null values |data type|
| --- | ---------------------------------|----------------|--------|  
| 0   |payment_type_id                   | 7032 non-null  | int64  |
| 1   |internet_service_type_id          | 7032 non-null  | int64  |
| 2   |contract_type_id                  | 7032 non-null  | int64  |
| 3   |senior_citizen                    | 7032 non-null  | int64  |
| 4   |partner                           | 7032 non-null  | int64  |
| 5   |dependents                        | 7032 non-null  | int64  |
| 6   |tenure                            | 7032 non-null  | int64  |
| 7   |phone_service                     | 7032 non-null  | int64  |
| 8   |multiple_lines                    | 7032 non-null  | object |
| 9   |online_security                   | 7032 non-null  | object |
| 10  |online_backup                     | 7032 non-null  | object |
| 11  |device_protection                 | 7032 non-null  | object |
| 12  |tech_support                      | 7032 non-null  | object |
| 13  |streaming_tv                      | 7032 non-null  | object |
| 14  |streaming_movies                  | 7032 non-null  | object |
| 15  |paperless_billing                 | 7032 non-null  | int64  |
| 16  |monthly_charges                   | 7032 non-null  | float64|
| 17  |total_charges                     | 7032 non-null  | float64|
| 18  |churn                             | 7032 non-null  | int64  |
| 19  |contract_type                     | 7032 non-null  | object |
| 20  |internet_service_type             | 7032 non-null  | object |
| 21  |payment_type                      | 7032 non-null  | object |
| 22  |is_female                         | 7032 non-null  | int64  |
| 23  |multiple_lines_No phone service   | 7032 non-null  | uint8  |
| 24  |multiple_lines_Yes                | 7032 non-null  | uint8  |
| 25  |online_security_Yes               | 7032 non-null  | uint8  |
| 26  |online_backup_Yes                 | 7032 non-null  | uint8  |
| 27  |device_protection_Yes             | 7032 non-null  | uint8  |
| 28  |tech_support_Yes                  | 7032 non-null  | uint8  |
| 29  |streaming_tv_Yes                  | 7032 non-null  | uint8  |
| 30  |streaming_movies_Yes              | 7032 non-null  | uint8  |
| 31  |contract_type_One year            | 7032 non-null  | uint8  |
| 32  |contract_type_two_years           | 7032 non-null  | uint8  |
| 33  |internet_service_type_fiber_optic | 7032 non-null  | uint8  |
| 34  |internet_service_type_None        | 7032 non-null  | uint8  |
| 35  |payment_type_electronic_check     | 7032 non-null  | uint8  |
| 36  |payment_type_Mailed check         | 7032 non-null  | uint8  |
| 37  |no_internet                       | 7032 non-null |  uint8 |
