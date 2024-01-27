"""
This code is complementary to my Numerical Computing (CSC-475) course
offered at COMSATS University Islamabad, Wah Campus.
"""
def bisection_method(fx, x1, x2, tol=0.0000001, maxiter=1000):
    """
    Finds the approximate root of linear or non-linear equation or system of equations using
    bisection method, an open root finding method.

    Parameters
    ----------
    fx : lambda function
        The function of which root is to be found.
    x1 : float
        First value in the domain before the root.
    x2 : float
        Second value in the domain before the root.
    tol : float, optional
        Minimum acceptable amount of error. The default is 0.00001.
    maxiter : float, optional
        Maximum number of iterations. The default is 1000.

    Returns
    -------
    It returns the acceptable root and the iteration at which it was found.

    """
    # Initializing the variables for iterations and middle values.
    iteration = mid = 0
    # Loop to iterate until the maximum iterations are reached or acceptable level of error.
    while abs(x2 - x1) > tol and iteration < maxiter:
        # Finding the middle value of domain.
        mid = (x1 + x2) / 2
        # Condition to check whether the root lies within the domain.
        if fx(x1) * fx(mid) < 0:
            x2 = mid
            iteration += 1
        elif fx(x2) * fx(mid) < 0:
            x1 = mid
            iteration += 1
        else:
            print("Condition of f(x1) * f(x2) < 0 is not satisfied. So there can be a root but we cannot find it using bisection method.\nSo exiting the program!!!!")
            break
    # Returning the root and the iteration at which the root is found.
    return mid, iteration + 1
# Defining the function f(x)=x^3-x-1
# Problem Link: https://atozmath.com/example/CONM/Bisection.aspx?q=fp&q1=E1
fn = lambda x: x**3 - x - 1
# Taking interval first value
x1 = float(input("Enter interval start value:\t"))
# Taking interval second value
x2 = float(input("Enter interval end value:\t"))
# Getting the root and iteration number
root, iter = bisection_method(fn, x1, x2)
# Printing root and iteration number
print("Root is at point %f after %d iteration" % (root, iter))