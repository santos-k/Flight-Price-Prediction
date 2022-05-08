# Flight-Price-Prediction
Flight price dataset analysis and prediction end to end project

This is an end to end project developed and design in python.
## Problem: 
Build a model that predict flight booking price with given input data. Analyse the data in depth and find the hidden pattern.
Also develope a web UI and deploye on web server.

## About the Dataset:
 This is an fligh dataset downloaded from kaggle.
 It has 10683 records, 11 features.
 **Columns details as below:**
 0   Airline         : Name of airlines, categorical
 1   Date_of_Journey : datetime
 2   Source          : Source city, categorical
 3   Destination     : destination city, categorical
 4   Route           : via which route flying, categorical
 5   Dep_Time        : Departure time in 24 hr format, object
 6   Arrival_Time    : Arrival time in 24 hr format, object
 7   Duration        : Total travel time, object
 8   Total_Stops     : Total stops between source and destination, object
 9   Additional_Info : Some other additional info, object
 10  Price           : Price of the ticket in INR, int
 
 **Techniques applied:**
 1. Null value imputation : dropped null value as it was only one null record
 2. Feature Creation : few new features created from date feature
 3. EDA: In depth analysis
 4. Prepared train/test data
 5. Model selection : 
 6. Model training
 7. Model Prediction and Accuracy check on multiple models
 8. selected the best final model
 9. Web UI designing: three section 1. Prediction, 2. Model Report, 3. Analysis Report
 10. Deployment

# Feature of the this project:
1. Navbar on top of page, with Header, logo, some buttons to direct to sections
2. This is single page app
3. Starting with Price Prediction and then below Model Result report and the Analysis report which done in EDA
4. Tab in navbar: 
    - i. Predict: This will direct to initail page
    - ii. Model: will direct to the Model Result report
      - This inlude Model Name
      - A radio button to see model reports charts
       - Accuracy score in Guage chart
       - Feature Importance in Bar chart
       - KDE plot of Test and Predicted result
       - Scatterplot of test and predicted result
