import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import os

base_url = os.getcwd()
df=pd.read_csv(base_url+'/training data/6_port_data.csv')  

def train_modal():
    # Dataframes 
    X=(df.iloc[:,1:])
    y=df['Angle']
    y = pd.DataFrame(y, columns = ['Angle'])
    print(X,y)
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.20, random_state=0)
    # Transform the input data into a polynomial feature space
    poly = PolynomialFeatures(degree=9)
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)
    # Initialize Linear Regression model
    reg = LinearRegression()
    # Fit the model to the training data
    reg.fit(X_train_poly, y_train)
    y_pred = reg.predict(X_test_poly)
    # Calculate R-squared score to evaluate the model
    r2 = r2_score(y_test, y_pred)
    print("R-squared score:", r2)
    print(y_test)
    print(y_pred)
    return reg,poly,y,X,X_test,y_pred,y_test

def predict_angle(input_,reg):
    y_predict = reg.predict(input_)
    return y_predict

