## Flight-Price-Prediction
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-310/)
[![Dash 2.7](https://img.shields.io/badge/Dash-2.7-blue)](https://dash.plotly.com/)
[![Plolty 5.11](https://img.shields.io/badge/Plotly-5.11-blue)](https://pypi.org/project/plotly/)
![GitHub repo size](https://img.shields.io/github/repo-size/santos-k/Flight-Price-Prediction?logo=github) 
![GitHub Repo stars](https://img.shields.io/github/stars/santos-k/Flight-Price-Prediction?style=social) 
![GitHub watchers](https://img.shields.io/github/watchers/santos-k/Flight-Price-Prediction?style=social) 
![GitHub followers](https://img.shields.io/github/followers/santos-k?style=social) 
![Bower](https://img.shields.io/bower/l/flask) 


This project is an end-to-end solution for predicting flight booking prices based on a given dataset. The project is developed and designed using Python, and it includes several key features and functionalities:

1. **Data Analysis:** The dataset is analyzed in depth to find hidden patterns and insights that can be used to make accurate predictions. The project includes several techniques for data cleaning, feature creation, and exploratory data analysis (EDA).
2. **Model Selection and Training:** The project includes several models that are trained and tested to find the best model for making predictions. The models are selected based on their accuracy and performance, and the best model is chosen for making predictions. 
3. **Prediction and Accuracy Check:** The project includes a feature for making predictions based on the selected model. The predictions are checked for accuracy against the test dataset.

## About the Dataset:
The dataset used in this project is a [flight dataset](https://www.kaggle.com/datasets/shubhamsarafo/flight-price) downloaded from Kaggle, containing 10,683 records and 11 features. These features include the airline name, date of journey, source and destination cities, route, departure and arrival times, duration, number of stops, additional information and the price of the ticket in INR. The dataset includes both categorical and numerical features, and will be used to make predictions on flight booking prices.


## Analysis and Model Training
Analysis and Model training code uploaded on [Kaggle](https://www.kaggle.com/code/kuchhbhi/flight-price-prediction-above-90/).

### Feature Engineering:

- Extraction of date, month, and day from the 'Date_of_Journey' feature
- Extraction of hour, minute, and week number from the 'Dep_Time' and 'Arrival_Time' features
- Extraction of hour and minute from the 'Duration' feature
- Creation of new features for the source and destination cities
- One-hot encoding of the 'Airline' and 'Source' features

### Transformation:
- Dropping of the 'Route' and 'Additional_Info' features
- Replacing the missing values in the 'Total_Stops' feature with the mode

 
## Snapshots: 
### Prediction Page
![image](https://user-images.githubusercontent.com/40932902/167579924-63502ca7-138a-427b-bcc3-ed9b4d8b1bce.png)
![image](https://user-images.githubusercontent.com/40932902/167580002-d0f9373d-8f61-4821-9b6c-55f81b95ac0f.png)
![image](https://user-images.githubusercontent.com/40932902/167580185-3f696244-3739-425a-9157-3bd0fda527f0.png)

### Model Result Report
![image](https://user-images.githubusercontent.com/40932902/167579328-72dc10ef-8b9c-4c90-9734-82ce868096e9.png)
![image](https://user-images.githubusercontent.com/40932902/167579477-8ded0820-e0bd-4c63-92fb-48eee8e8ffaa.png)
![image](https://user-images.githubusercontent.com/40932902/167579564-64a421c4-e3f1-4d4f-add0-d9f02ac2c956.png)
![image](https://user-images.githubusercontent.com/40932902/167579663-75389d36-ddf6-4cea-865a-0e70f54bfc22.png)
![image](https://user-images.githubusercontent.com/40932902/167579767-97f6ae47-0b2b-417c-840d-dd0d1bd26026.png)

### EDA Report 
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



