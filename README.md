# Classification Project
## Objective 
> Analyze dataset featuring customer details of a telecummunications company
Utilize statistical models to aid in analysis and prodcution of actionable insights
Construct .....

## Business Goals
> Find drivers for customer churn at Telco. Why are customers churning?</br>
Construct a ML classification model that accurately predicts customer churn.</br>

## Deliverables
> Report outlining what steps were taken, why and what was the outcome?</br>
> Key findings, recommendations, and takeaways from project</br>
> Code detailing the above

## Executive Summary


## Data Dictionary
|Target|Datatype|Definition|
|:-----|:-----|:-----|
|churn|xxx non-null: uint8| titanic passenger status

|Feature|Datatype|Definition|
|:-----|:-----|:-----|
customer_id                           | 4225 non-null   object |
gender                                |4225 non-null   object | customer gender (female:1, male:2)
senior_citizen                        | 4225 non-null   int64  |
partner                               | 4225 non-null   object |
dependents                            | 4225 non-null   object |
tenure                                 |4225 non-null   int64  | customer tenure in months
phone_service                          |4225 non-null   object |
multiple_lines                         |4225 non-null   object |
online_security                        |4225 non-null   object |
online_backup                         | 4225 non-null   object |
device_protection                     | 4225 non-null   object |
tech_support                          | 4225 non-null   object |
streaming_tv                          | 4225 non-null   object |
streaming_movies                      | 4225 non-null   object |
paperless_billing                     | 4225 non-null   object |
monthly_charges                       | 4225 non-null   float64|
total_charges                         | 4216 non-null   float64|
churn                                 | 4225 non-null   object |
contract_type                         | 4225 non-null   object |
payment_type                          | 4225 non-null   object |
internet_service_type                 | 4225 non-null   object |
gender_encoded                        | 4225 non-null   int64  |
partner_encoded                       | 4225 non-null   int64  |
dependents_encoded                    | 4225 non-null   int64  |
phone_service_encoded                 | 4225 non-null   int64  |
paperless_billing_encoded             | 4225 non-null   int64  |
churn_encoded                         | 4225 non-null   int64  |
contract_type_One year                | 4225 non-null   uint8  |
contract_type_Two year                | 4225 non-null   uint8  |
payment_type_Credit card (automatic)  | 4225 non-null   uint8  |
payment_type_Electronic check         | 4225 non-null   uint8  |
payment_type_Mailed check             | 4225 non-null   uint8  |
internet_service_type_Fiber optic     | 4225 non-null   uint8  |
internet_service_type_None            | 4225 non-null   uint8  |
multiple_lines_No phone service       | 4225 non-null   uint8  |
multiple_lines_Yes                    | 4225 non-null   uint8  |
online_security_No internet service   | 4225 non-null   uint8  |
online_security_Yes                   | 4225 non-null   uint8  |
online_backup_No internet service     | 4225 non-null   uint8  |
online_backup_Yes                     | 4225 non-null   uint8  |
device_protection_No internet service | 4225 non-null   uint8  |
device_protection_Yes                 | 4225 non-null   uint8  |
tech_support_No internet service      | 4225 non-null   uint8  |
tech_support_Yes                      | 4225 non-null   uint8  |
streaming_tv_No internet service      | 4225 non-null   uint8  |
streaming_tv_Yes                      | 4225 non-null   uint8  |
streaming_movies_No internet service  | 4225 non-null   uint8  |
streaming_movies_Yes                  |  4225 non-null   uint8  |

## Initial Questions and Hypotheses
> What differientiates a customer that has churned from those that have not?  

> Is churn more likely to be affected by price or service? Is it some combination of the two?

## Pipeline Walkthrough
### Plan
> Create required repository, modules, notebooks, and readme's.  
Review previous work with telco data for lessons learned  
Take necessary steps to acquire data and streamline acquire module  
Adapt prepare module for better workflow when preparing data  
Work with classifcation models; focus on logistic regression  
Finalize model selection and testing. 
Rinse and repeat steps as needed prior to deadline
Export chosen model predictions concatenated with customer_id and export csv  
Tidy up repository and notebooks for sharing and presentation  

### Acquire
> Acquire the `telco` dataset from the Code Up database  
> In addition to customer demographic data using:
- Contract type, payment method, and internet service type  
> Read into `pd.DataFrame` for further preparation

### Prepare
> Utlize takeways from Acquire phase to inform prepare decisions  
> Quickly explore the data for initial findings and document
> Crafted functions to **clean** up data for Explore and Model phases
* `prep_telco`, `final_prep`, `split_data` --> prepare.py

### Explore
> Univariate: 
* Basic histograms for categories, disregarding encoded columns in dataframe for now
* 

### Model

> asdflkj;af

### Deliver
> asdflkj;af

## Project Reproduction Requirements