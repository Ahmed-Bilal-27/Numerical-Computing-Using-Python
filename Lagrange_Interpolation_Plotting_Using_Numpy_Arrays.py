"""
This code is complementary to my Numerical Computing (CSC-475) course
offered at COMSATS University Islamabad, Wah Campus.
"""

#------------Imports------------
import numpy as np
import matplotlib.pyplot as plt

#Creating x and y data points as separate numpy arrays
x = np.array([0, 20, 40, 60, 80, 100], dtype=float)
y = np.array([26.0, 48.6 , 78, 92.3, 290.9, 320.32], dtype=float)
# Creating numpy array for x data points to plot
xplt = np.linspace(x[0], x[-1])
# Creating empty numpy array for y data points which will be calculated for
# every corresponding x data point stored in xplt to plot
yplt = np.array([], dtype=float)
# Calculating yplt
for xp in xplt:
    yp = 0
    for xi,yi in zip(x,y):
        yp += yi * np.prod((xp - x[ x != xi])/(xi - x[x != xi]))
    yplt = np.append(yplt, yp)
# Plotting the points
plt.plot(x, y, 'ro', xplt, yplt, 'b-')
plt.xlabel('x')
plt.ylabel('y')
plt.show()