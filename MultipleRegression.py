# Code source: Jaques Grobler
# License: BSD 3 clause

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Load the diabetes dataset
#diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
data= pd.read_csv('diabetes_original.csv') 
#multiple type of data is given for multiple regression
X=data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] 
#result based on the above column values
y=data['Outcome']

regr = linear_model.LinearRegression()
regr.fit(X, y)

predictedOutcome = float(regr.predict([[183, 64,0,0,23]]))
print(round(predictedOutcome,0))
predictedOutcome =float(regr.predict([[89, 66,23,94,28]]))
print(round(predictedOutcome,0))
print(type(predictedOutcome))

print('Coefficient',regr.coef_)