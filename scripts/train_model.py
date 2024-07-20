import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score


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
import numpy as np
pred=model.predict(np.array([79248.64,6.0,6.7,3.09,40173.07]).reshape(1,-1))
print(pred)
# Save model
import joblib
joblib.dump(model, 'scripts/health_model.pkl')