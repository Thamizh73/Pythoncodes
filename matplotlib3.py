import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,5,11)
y=x**2
#plotting using OOP Method - sub plots 
fig=plt.figure()
axes=fig.add_axes([0.1,0.1,.8,.8])
axes.plot(x,y)
axes.set_xlabel('X-Axis')
axes.set_ylabel('Y-Axis')
axes.set_title('My graph')
fig2=plt.figure()
axes1=fig2.add_axes([.1,.1,.8,.8])
axes2=fig2.add_axes([.15,.45,.4,.4])
axes1.plot(x,y)
axes2.plot(y,x)
