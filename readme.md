# House Price Prediction Web App

Welcome to the House Price Prediction Web App repository! This project aims to predict house prices in the USA using a linear regression model. The dataset used for this project is from Kaggle (`USA_house.csv`).

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model](#model)
- [Web App](#web-app)
- [Preview](#preview)
- [Author](#Author)
- [Contact](#contact)

## Overview

This project utilizes a linear regression model to predict house prices based on various features. The model is trained on the `USA_house.csv` dataset and is deployed as a web application using Django.

## Features

- Data preprocessing and visualization
- Linear regression model for house price prediction
- Django-based web application for user interaction
- User-friendly interface for inputting house features and getting price predictions

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/itz-shakil-92/House-Price-Prediction-Web-App.git
    cd House-Price-Prediction-Web-App
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv myenv
    
    # Unix/MacOS:
    source myenv/bin/activate   
    
    # Windows 
    myenv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

1. Open your web browser and go to `http://127.0.0.1:8000/`.
2. You will be find home page of the App 
3. Click on the start button then you'll get the prediction input page
4. Enter the required house features in the input fields.
5. Click on the "Predict" button to get the predicted house price.

## Dataset

- Dataset source: [USA_House.csv](https://www.kaggle.com/datasets/vedavyasv/usa-housing)

## Model

The linear regression model is built using Python's `scikit-learn` library. The model is trained on the `USA_house.csv` dataset and is used to make predictions based on the input features provided by the user.
You can refer to my previous repository for better explaination of the model and dataset

[Link for House-Price-Prediction Machina learning model](https://github.com/itz-shakil-92/House-price-prediction)

If you find any error to get predition please run `scripts/train_model.py` file after it you can proceed


## Web App

The web application is built using the Django framework. It provides a user-friendly interface for inputting house features and getting price predictions. The app is currently in the development stage and has not been deployed yet.



## Preview
Home Page:-

![Home_Page](/screenshots/Page_1.jpg)


Prediction Page:-

![Home_Page](/screenshots/Page_2.jpg)


Result of Prediction:-


![Home_Page](/screenshots/Page_3.jpg)


## Author
- [Shakil Kathat](https://www.github.com/itz-shakil-92)

## Contact
If you have any questions or need further assistance, please feel free to contact us at shakilkathat5603@gmail.com
