"""
This code is complementary to my Numerical Computing (CSC-475) course
offered at COMSATS University Islamabad, Wah Campus.
"""
#----------------Imports-----------------
from numpy import array, zeros, fabs, linalg
#----------------Imports-----------------
a = array([[0, 7, -1, 3, 1],
           [0, 3, 4, 1, 7],
           [6, 2, 0, 2, -1],
           [2, 1, 2, 0, 2],
           [3, 4, 1, -2, 1]], float)
b = array([5, 7, 2, 3, 4], float)
n = len(b)
x = zeros(n, float)
print("Solution of the system using numpy:")
print(linalg.solve(a, b))
# Doing Elimination Step - Creating Upper Triangular Matrix
# Loop for the main diagonal entries
for k in range(n-1):
    # Checking whether the pivot element is very small or equal to zero
    if fabs(a[k, k]) < 1.0e-12:
        # Loop to check a non-zero element in the row beneath the fixed row or current pivot column
        for i in range(k + 1, n):
            # Checking if there is any non-zero element
            if fabs(a[i, k]) > fabs(a[k, k]):
                a[[k, i]] = a[[i, k]] # Swapping coefficient matrix rows
                b[[k, i]] = b[[i, k]] # Swapping constant column matrix rows
                break; # Once swapped break out of the loop
    # Loop for the entries beneath the main diagonal entries
    for i in range(k + 1, n):
        # Skipping the row where the entry beneath the current main diagonal entry is zero
        if a[i,k] == 0: continue
        # Calculating scaling factor
        scaling_factor = a[k,k] / a[i,k]
        # Loop to traverse the columns
        for j in range(k, n):
            # Calculating the new value of the entries beneath the current main diagonal entry
            a[i, j] = a[k, j] - a[i, j] * scaling_factor
        # Calculating the constant column matrix entry
        b[i] = b[k] - b[i] * scaling_factor
# Printing matrix a and column matrix b
print("The coefficient matrix:\n")
print(a)
print("The constant column matrix:\n")
print(b)
# Doing Backward substitution
# Calculating the last row
x[n - 1] = b[n - 1] / a[n - 1, n - 1]
# Loop to calculate rows from second last to the first
for i in range(n - 2, -1, -1): # End point is -1 so to include the first row at index 0
    sum_ax = 0
    # Calculating the sum of x values greater than the current x value as it is backward substitution
    for j in range(i + 1, n):
        sum_ax += a[i, j] * x[j]
    # Calculating the current x value
    x[i] = (b[i] - sum_ax) / a[i, i]
# Printing the solution of the system
print("The solution of the system:\n")
print(x)