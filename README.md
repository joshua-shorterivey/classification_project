# Classification Project
## Objective 
> Analyze dataset featuring customer details of a telecummunications company  
Utilize statistical models to aid in analysis and production of actionable insights  
Construct report summarizing findings

<Details>
<summary> Cancer </summary>
<li> alksdjflkjasdf


</Details>

## Business Goals
> Find drivers for customer churn at Telco. Why are customers churning?  
Construct a ML classification model that accurately predicts customer churn.  

## Deliverables
> Final report outlining what steps were taken, why and what was the outcome  
Key findings, recommendations, and takeaways from project  
`final_predictions.csv` file laying out model predictions  
Python modules and jupyter notebooks needed to create the project  
Instructions on project reproducibility

## Data Dictionary
|Target|Datatype|Definition|
|:-----|:-----|:-----|
|churn|xxx non-null: uint8| customer churn status

|Feature|Datatype|Definition|
|:-----|:-----|:-----|
customer_id                           | 4225 non-null   object | customer company identification code
gender                                | 4225 non-null   object | customer gender 
senior_citizen                        | 4225 non-null   int64  | customer status as senior citizen
partner                               | 4225 non-null   object | customer partner status
dependents                            | 4225 non-null   object | customer dependent status
tenure                                | 4225 non-null   int64  | customer tenure in months
phone_service                         | 4225 non-null   object | customer phone service status
multiple_lines                        | 4225 non-null   object | customer subscription to multiple phone lines
online_security                       | 4225 non-null   object | customer online security service status
online_backup                         | 4225 non-null   object | customer online backup service status
device_protection                     | 4225 non-null   object | customer device protection service status
tech_support                          | 4225 non-null   object | customer tech support service status
streaming_tv                          | 4225 non-null   object | customer streaming tv service status
streaming_movies                      | 4225 non-null   object | customer streaming movie service status
paperless_billing                     | 4225 non-null   object | customer paperless billing status
monthly_charges                       | 4225 non-null   float64| customer monthly charges
total_charges                         | 4216 non-null   float64| customer total charges
churn                                 | 4225 non-null   object | customer churn status
contract_type                         | 4225 non-null   object | customer contract type
payment_type                          | 4225 non-null   object | customer payment type
internet_service_type                 | 4225 non-null   object | customer internet service 


## Initial Questions and Hypotheses
> Did customers that have churned pay higher monthly prices?   
* ${\alpha}$ = .05

* ${H_0}$: Customers that have churned pay equal or less than those that have not churned.

* ${H_a}$: Customers that have curned pay more than those that have not churned.

* Conclusion: I rejected the null hypothesis after statistical testing supported the conclusion that churned customers did in fact pay higher monthly prices

> Are longer tenured customers at less risk of churn?
* ${\alpha}$ = .05

* ${H_0}$: Customers that have churned show little to no difference in legnth of tenure.

* ${H_a}$: Customers that have curned show significant difference in length of tenure.

 * Conclusion: I rejected the null hypothesis after statistical testing supported the conclusion that churned customers did in fact pay higher monthly prices

## Summary of Key Findings
* Month-to-month customers seem more sensitive to higher prices than other groups
* Customers with less than 12 months more sensitive to higher prices
* Fiber customers pay higher than average, but those that churn pay *less* than those that do not
* 'Newer fiber customers at higher risk for churn

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
> In addition to customer demographic data, I am also using:
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
> Multivariate:
* Visuals exploring features as they relate to churn

### Model

> Set Baseline Prediction and evaluate accuracy  
> Set up comparison dataframes for evaluation metrics and model descriptions  
> Explore various models and feature combinations.
* Decision Tree Models - Poorest performing on initial subset
* Random Forest Models - Best performing on initial train subset
* K-Nearest Neighbor Models: Settled on 3 for nearest neighbor count
* Logistic Regression - Relatively weak performance

> Choose **three** models to validate
* Initial set all performed barely above baseline. 

>Choose **one** model to test

### Deliver
> Create project report in form of jupyter notebook  
> Finalize and upload project repository with appropirate documentation  
> Present to audience of Code Up instructors and classmates

## Project Reproduction Requirements
> Requires personal `env.py` file containing database credentials  
> Steps:
* Fully examine this `README.md`
* Download `acquire.py, model.py, prepary.py, and final_report.ipynb` to working directory
* Create and add personal `env.py` file to directory. Requires user, password, and host variables
* Run ``final_report.ipynb`