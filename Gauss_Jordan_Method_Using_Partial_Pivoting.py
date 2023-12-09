"""
This code is complementary to my Numerical Computing (CSC-475) course
offered at COMSATS University Islamabad, Wah Campus.
"""
#----------------Imports-----------------
import numpy as np
#----------------Imports-----------------
# Defining function for Gauss-Jordan Method
def gauss_jordan(a, b):
    a = np.array(a, float)
    b = np.array(b, float)
    n = len(b)
    # Loop for the main diagonal or fixed row entries
    for k in range(n):
        # Checking whether the pivot element is very small or equal to zero
        if np.fabs(a[k, k]) < 1.0e-12:
            # Loop to check a non-zero element in the row beneath the fixed row or current pivot column
            for i in range(k + 1, n):
                # Checking if there is any non-zero element
                if np.fabs(a[i, k]) > np.fabs(a[k, k]):
                    a[[k, i]] = a[[i, k]] # Swapping coefficient matrix rows
                    b[[k, i]] = b[[i, k]] # Swapping constant column matrix rows
                    break; # Once swapped break out of the loop
        # Division of the pivot row
        pivot = a[k, k]
        # Loop to traverse the columns
        for j in range(k, n):
            a[k, j] /= pivot
        b[k] /= pivot
        # Elimination Loop
        for i in range(n):
            # Skipping the row where the entry is zero or the row is equal to fixed row
            if a[i,k] == 0 or i == k: continue
            # Factor by which we are going to multiply
            factor = a[i, k]
            # Row transformation
            for j in range(k, n):
                a[i, j] -= factor * a[k, j]
            b[i] -= factor * b[k]
    return a, b
# Problem Link: https://math.libretexts.org/Bookshelves/Applied_Mathematics/Applied_Finite_Mathematics_(Sekhon_and_Bloom)/02%3A_Matrices/2.02%3A_Systems_of_Linear_Equations_and_the_Gauss-Jordan_Method
# Creating coefficient matrix
a = [[2, 1, 2], [1, 2, 1], [3, 1, -1]]
# Creating constant vector
b = [10, 8, 2]
# Getting constant vector and identity matrix of same size as coefficient matrix
identity, X = gauss_jordan(a, b)
# Printing the results
print("The solution of the system is:\n")
print(X)
print("The identity coefficient matrix is:\n")
print(identity)