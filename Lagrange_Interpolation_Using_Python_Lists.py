"""
This code is complementary to my Numerical Computing (CSC-475) course
offered at COMSATS University Islamabad, Wah Campus.
"""

#Creating x and y data points as separate lists
x = [0, 20, 40, 60, 80, 100]
y = [26.0, 48.6 , 78, 92.3, 290.9, 320.32]

n = len(x) - 1 # degree of the polynomial
# Taking x point as input for which y point will be calculated
xp = float(input("Enter the x data point:\t"))
# Calculated y is the sum of the products so that's why initialized to 0
yp = 0
# Here in the loop the lagrange interpolation logic is implemented
for i in range(n + 1):
    p = 1
    for j in range(n + 1):
        if j != i:
            p *= (xp - x[j])/(x[i] - x[j])# Calculating individual terms
    yp += p * y[i] # Adding the individual terms
print("For x = %.4f, y = %.4f" % (xp, yp))