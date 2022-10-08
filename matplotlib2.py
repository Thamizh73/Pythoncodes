import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,5,11)
y=x**2
#plotting using Functional Method - sub plots
plt.subplot(1,2,1)
plt.plot(x,y,'r')
plt.subplot(1,2,2)
plt.plot(y,x,'b')
plt.show()
