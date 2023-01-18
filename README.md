## Flight-Price-Prediction

![image](https://user-images.githubusercontent.com/40932902/213074591-8d20668b-94a4-42bc-9844-12129444053d.png)

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

## Getting Started
- These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Python 3.6 or later
- Scikit-Learn
- Python Dash & Plotly
- Other dependencies are listed in requirements.txt

### Installation
1. Clone the repository to your local machine
   ```
   git clone https://github.com/santos-k/Flight-Price-Prediction
   ```
2. Install the required packages
   ```
   pip install -r requirements.txt
   ```
### Running the System
1. Run the following command to start the web application
   ```
   python app.py
   ```
2. Open your web browser and navigate to http://localhost:port_no to access the system


## To deploy this project on Google Cloud Platform (GCP), you will need to follow these steps:

1. Create a new project on GCP by going to the GCP Console (https://console.cloud.google.com/) and selecting "Select a Project" or "Create Project".
2. Create a virtual machine instance by going to the GCP Console, selecting "Compute Engine", and clicking on "Create Instance".
3. Choose the appropriate machine type and configure it as per your requirements. Make sure to open the required ports for the application.
4. Once the virtual machine is created, connect to it using SSH by going to the GCP Console, selecting "Compute Engine", and clicking on "SSH" next to the instance.
5. Install the required packages on the virtual machine by running the command pip install -r requirements.txt.
6. Clone the repository to the virtual machine by running the command git clone https://github.com/username/flight-price-prediction.git.
7. Unzip the `random_model.zip` in same directory
8. Run the application by running the command python app.py
9. Assign a static IP to your instance and map it to the domain name of your choice for easy access.

The system should now be accessible by navigating to the domain name or the IP address of the virtual machine.
You can also use containerization tools such as Docker to deploy this project on GCP, but it is beyond the scope of this overview.


## To deploy this project on GCP, you will need the following files:
1. `app.py`: This is the main file that runs the web application. It contains the code for the neural network model, the front-end design using Python Dash, and the integration with Flipkart data.
2. `requirements.txt`: This file contains a list of all the dependencies required for the project. It includes packages such as TensorFlow, Keras, and Python Dash.
3. `model.pkl`: This is the trained model file. It contains the weights and architecture of the Resnet50 model.
4. `data`: This folder contains the data used for training the model. It should include the scraped images and their corresponding labels.
5. `config.py`: This file contains the configuration settings for the project, such as the number of results to display and the Flipkart API key.
6. `Dockerfile` (Optional): This file is used to create a Docker image of the application. It contains instructions on how to build the image and what dependencies to install.
7. `deployment.yaml` (Optional): This file is used to deploy the application on GCP using Kubernetes. It contains instructions on how to create the necessary resources and configure the application.

Please make sure that these files are properly configured and in the correct location for successful deployment on GCP.


## To deploy this project on Heroku, you will need to follow these steps:
1. Create a new account on Heroku if you don't have one already.
2. Install the Heroku CLI by following the instructions on the [Heroku](https://devcenter.heroku.com/articles/heroku-cli) website.
3. Clone the repository to your local machine.
4. Create a new app on Heroku by running the command `heroku create` in the project directory.
5. Add the required buildpacks by running the command `heroku buildpacks:set heroku/python`
6. Push the code to Heroku by running the command `git push heroku master`
7. Create a new instance of PostgreSQL by running the command `heroku addons:create heroku-postgresql:hobby-dev`
8. Set the environment variables for the application by running the command `heroku config:set VARIABLE_NAME=value`
9. Open the app by running the command `heroku open`

- Note:
  - You will also need to add the `Procfile` file to your root directory. It is a file that tells Heroku how to run your application.
  - You will also need to add the `requirements.txt` file to your root directory.

You should now be able to access the application by going to the URL provided by Heroku.
Please make sure that these files are properly configured and in the correct location for successful deployment on Heroku.

## Authors
Santosh Kumar - [Github](https://github.com/santos-k/)

## License
This project is licensed under the MIT License - see the LICENSE.md file for details

### Don't forget to give a star if you find it helpful.
This system is made as a part of the project and is open for contributions and modifications.

 
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



Super cool
