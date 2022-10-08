#numpy arrays
import numpy as np
import pandas as pd
diabetes_data=pd.read_csv('diabetes.csv')
print (diabetes_data.head(3))
print(diabetes_data[0:1])
glucose_data=diabetes_data.Glucose 
print(glucose_data)
result=diabetes_data.Outcome
print(result)
print('reshapes')
a = np.arange(6)
print(a)
a = a.reshape((-1, 1))
print(a)
'''
arr1,arr2 = np.array([1, 2, 3, 4, 5]),np.array([11, 22, 33, 44, 55])
print(arr1)
print(type(arr1))
print(arr2)
print(type(arr2))
'''