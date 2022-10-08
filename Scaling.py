#Predict the CO2 emission from a 1.3 liter car that weighs 2300 kilograms:
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("cars.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

scaledX = scale.fit_transform(X) #using StandardScaler/standardaization formula
print('printing scaled/transformed values of Weight ad Volume')
print(scaledX)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]]) #convert the given weight and volume into scale for prediction
print('scaled',scaled)
predictedCO2 = regr.predict([scaled[0]]) #predicting the CO2 omission for the scaled value
print('Predicted Emission:',predictedCO2)
