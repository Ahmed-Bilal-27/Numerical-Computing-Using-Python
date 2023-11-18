"""
This code is complementary to my Numerical Computing (CSC-475) course
offered at COMSATS University Islamabad, Wah Campus.
"""
#------------Imports------------
import numpy as np

#Creating x and y data points as separate numpy arrays
x = np.array([0, 20, 40, 60, 80, 100])
y = np.array([26.0, 48.6 , 78, 92.3, 290.9, 320.32])
# Taking x point as input for which y point will be calculated
xp = float(input("Enter the x data point:\t"))
# Calculated y is the sum of the products so that's why initialized to 0
yp = 0
# Here in the loop the lagrange interpolation logic is implemented
for xi,yi in zip(x,y):
    yp += yi * np.prod((xp - x[ x != xi])/(xi - x[x != xi])) # Here the calculated terms
# using product are added together and stored in variable yp which is the required answer
# Printing the given x and calculated y data points
print("For x = %.4f, y = %f" % (xp, yp))