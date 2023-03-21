# Churn: The Road to Low False Negatives and High True Gains

## Project Description
- This project is the first project in the data science methodologies course. It will go through the data science pipeline and attempt to discover why customers are churning at Telco. This project is important for two reasons:
  1. For experience with a project that cycles through a full data science pipeline
  2. For experience merging the different business and writing components neccessary to succesfully deliver information to stakeholders

## Project Goals
- Find drivers for customer churn at Telco
- Construct a ML classification model that accurately predicts customer churn
- Deliver a report that a non-data scientist can read through and understand 

## Initial Questions
1. What is the companies overall churn rate?
2. Does the churn rate change based on the core service the customer has?
3. Do supplementary internet support services impact churn?
4. Do streaming services impact churn?

## Project Plan
- Acquire data from MySQL
- Prepare data
  - Remove unnecessary features
  - Identify and replace missing values
  - Alter innapropriate data types
- Explore the data to find drivers of churn and answer intital questions above
- Create a model to predict if a customer will churn
  - Use features identified in explore to build predictive models
  - Evaluate models on train and validate data
  - Select the best model based on highest accuracy, lowest false negative rate, and lowest difference between test and validate scores
  - Evaluate the best model on test data
- Conclude with recommendations and next steps

## Data Dictionary
| Feature | Definition | Data Type |
|:--------|:-----------|:----------|
| gender | The customer's gender. | object |
| senior_citizen | An indicator of old age. Information on what age is used to determine senior citizen status was not found | int64 |
| partner | Indicates if a customer has a partner. | object |
| dependents | Indicates if a customer has dependents. | object |
| phone_service | Indicates if a customer has phone service. | object |
| online_security | Indicates if a customer has online security.| object |
| online_backup | Indicates if a customer has online backup. | object |
| device_protection | Indicates if a customer has device protection. | object |
| tech_support | Indicates if a customer has tech support. | object |
| streaming_tv | Indicates if a customer has tv streaming. | object |
| streaming_movies | Indicates if a customer has movie streaming. | object |
| paperless_billing | Indicates if a customer has paperless billing. | object |
| churn | Indicates if a customer has churned. | object |
| contract_type | The customer's contract type| object |
| internet_service_type | The customer's internet service type| object |
| payment_type | The customer's payment method.| object |
|Additional Features|Encoded categorical data| uint8 |

## Steps to Reproduce
1. Clone this repo
2. Insert credentials in the blank_eny.py file and save
3. Run notebook
