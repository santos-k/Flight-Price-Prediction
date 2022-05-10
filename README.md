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
 
 ## Feature Creation:
 1. from **Date_of_Journey**
    - Month
    - Day
    - Week of year
    - day name
  2. from **Dep_TIme**
     - Departure Hour
     - Departure Min
  3. from **Arrival_Time**
     - Arrival_Hour
     - Arrival_Min
  4. from **Duration**
     - Duration_Hour
     - Duration_Min

# Feature of the this project:
1. Navbar on top of page, with Header, logo, some buttons to direct to sections
2. This is single page app
3. Starting with Price Prediction and then below Model Result report and the Analysis report which done in EDA
4. Tab in navbar: Navbar is fixed on top, it will always visible
    - i. Predict: This will direct to initail page
    - ii. Model: will direct to the Model Result report
      - This inlude Model Name
      - A radio button to see model reports charts
       - Accuracy score in Guage chart
       - Feature Importance in Bar chart
       - KDE plot of Test and Predicted result
       - Scatterplot of test and predicted result
     - iii. Analysis: it will redirect to EDA section 
        - Analysis of Categorical Features in bar chart- Univeriate Anlysis
           - Radio button to change the category and bar chart
              - Airline
              - Source
              - Destination
              - Day Name
              - Month Name
              - Total_Stops
        - Analysis of Numerical Features: Bi-variate Analsis
          - Radio Buttons to change the value and graph
             - X-Axis: Arrival_Time | Day of Month | Week of Year | Duration | Departure_Time | PriceTotal_Stops
             - Color: None | Airline | Day Name | Month Name | Total_Stops
             
        - Box plot(Outlier detection) of Price: Bi-variate analysis
          - Radio Buttons to change the chart
            - Airline | Day Name | Month Name | Total_Stops
        - More way to visualize Numerical Features : Multi-variate analysis (Scatterplot, X-axis: Price)
           - Three dropdown for different feature selection
              - Y-Axis: select any available feature 
              - Color : select any available feature 
              - Size  : select any available feature 
        - Comparing two Categorical Features
          - Heatmap and crosstab of two categorical features
          - X-axis/Y-axis
        - Airport in Map 
          - All the Source and Destination airport shown in map   
      - iv. Source Code:
        - It will redirect to the github repository of this project
      - v. Profile
          - it will redirect to My own web profile which is developed in dash. 
      - vi. More
          -  Github | Kaggle | Linkedin | About


## Data and Code files:
 1. app.py: mail python file where all the web ui designed
 2. functions.py: some custome fuctions written to override the repeatation of code
 3. directory: 'assests/' pictures stored in this assests folder 1. fevicon.ico, 2. sk2.png(logo)
 4. df.csv: preprocessed data file for displaying charts in web app
 5. test_data.csv: only X_test and y_test  data in this file to display Model report in web app
 6. model.pkl: built model packed in it, unable to upload here due big size issue, download from [Kaggle](https://www.kaggle.com/code/kuchhbhi/flight-price-prediction-multiple-models)
 
## files for deployment on Heroku:
   - 1. .gitignore  
   - 2. Procfile 
   - 3. requirements.txt
 
 
## Snapshots: 
# Prediction
![image](https://user-images.githubusercontent.com/40932902/167579924-63502ca7-138a-427b-bcc3-ed9b4d8b1bce.png)
![image](https://user-images.githubusercontent.com/40932902/167580002-d0f9373d-8f61-4821-9b6c-55f81b95ac0f.png)
![image](https://user-images.githubusercontent.com/40932902/167580185-3f696244-3739-425a-9157-3bd0fda527f0.png)

# Model Result Report
![image](https://user-images.githubusercontent.com/40932902/167579328-72dc10ef-8b9c-4c90-9734-82ce868096e9.png)
![image](https://user-images.githubusercontent.com/40932902/167579477-8ded0820-e0bd-4c63-92fb-48eee8e8ffaa.png)
![image](https://user-images.githubusercontent.com/40932902/167579564-64a421c4-e3f1-4d4f-add0-d9f02ac2c956.png)
![image](https://user-images.githubusercontent.com/40932902/167579663-75389d36-ddf6-4cea-865a-0e70f54bfc22.png)
![image](https://user-images.githubusercontent.com/40932902/167579767-97f6ae47-0b2b-417c-840d-dd0d1bd26026.png)

# EDA Report 
![image](https://user-images.githubusercontent.com/40932902/167307594-5fdce2b8-0d81-4ccb-a958-65b2c20128e9.png)
![image](https://user-images.githubusercontent.com/40932902/167307605-900c4b37-ce2f-4693-9033-165c87f91957.png)
![image](https://user-images.githubusercontent.com/40932902/167307616-ab8eb82e-deca-46d4-9392-30d023dd8691.png)
![image](https://user-images.githubusercontent.com/40932902/167307629-6dd873f3-3e41-4d1e-9a1a-b2dc9c6e5f74.png)
![image](https://user-images.githubusercontent.com/40932902/167307634-3989bb4c-fba0-4e8f-9870-fbbdafde35f6.png)
![image](https://user-images.githubusercontent.com/40932902/167307645-d16b938a-8b05-4388-9cb5-32a4fbe9af79.png)
![image](https://user-images.githubusercontent.com/40932902/167307658-f336d99c-4b6c-4e08-aba6-83434ca30895.png)
![image](https://user-images.githubusercontent.com/40932902/167307681-610a58f0-7ad5-46ec-8f4b-b14be2d3f733.png)
![image](https://user-images.githubusercontent.com/40932902/167307685-7e112fe0-6133-409f-b7df-fb6f9e8e3096.png)
![image](https://user-images.githubusercontent.com/40932902/167307700-4113319d-96de-41f1-9ecc-25db8374dd9b.png)
![image](https://user-images.githubusercontent.com/40932902/167307711-46e115dc-de34-4060-bef3-f23b7df25021.png)



