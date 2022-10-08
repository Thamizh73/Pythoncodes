import numpy
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

#this r2_score gives how much the given data fit in polynomial regression.
#Values range from 0 t 1  where 100 is perfect fit and 0 is not fit.
print(r2_score(y, mymodel(x))) 

#Drawing the line of polynomial regression
myline = numpy.linspace(1, 22, 100)
plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

#predicting the speed of a car that passes around at 17. hours
speed = mymodel(17)
print(speed)
