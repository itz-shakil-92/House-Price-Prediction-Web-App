import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import joblib

# Load the dataset from CSV
df = pd.read_csv('scripts/USA_Housing.csv')

# Exploratory Data Analysis (EDA)
df=df.drop(['Address'],axis=1)


# Train test split
X=df.drop('Price',axis=1)
y=df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Building the Linear Regression Model
model = LinearRegression()

# Fitting the model on the training data
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'scripts/health_model.pkl')