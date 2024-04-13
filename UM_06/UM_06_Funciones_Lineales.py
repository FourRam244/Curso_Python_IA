import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,50,100)
y1=30*x+1000
y2=50*x+100
plt.plot(x,y1,c="orange")
plt.plot(x,y2,c="blue")
plt.show()