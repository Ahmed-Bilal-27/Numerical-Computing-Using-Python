"""
This code is complementary to my Numerical Computing (CSC-475) course
offered at COMSATS University Islamabad, Wah Campus.
"""
# Defining method for Regula Falsi/False Position Method with default tolerance of 0.00001 and
# maximum iterations of 1000.
# fx is the function of x
# x1 is the first starting data point in domain
# x2 is the second starting data point in domain
# f(x1) * f (x2) < 0 so that one root must exist within this domain
def false_position(fx, x1, x2, tol=0.00001, maxiter=1000):
    xh = 0
    iteration = 0
    if fx(x1) * fx(x2) < 0:
        for iteration in range(maxiter):
            xh = x2 - (x2 - x1)/(fx(x2) - fx(x1)) * fx(x2)
            if abs(fx(xh)) < tol: return xh, iteration
            elif fx(x1) * fx(xh) < 0:
                x2 = xh
            else:
                x1 = xh
    else:
        print("No root in the given domain because f(x1) * f(x2) < 0 is not satisfied!!")
    return xh, iteration
# Defining the function f(x)=x3-x-1
# Problem Link: https://atozmath.com/example/CONM/Bisection.aspx?q=fp&q1=E1
fn = lambda x: x**3 - x - 1
# Taking interval starting value
x1 = float(input("Enter interval start value:\t"))
# Taking interval ending value
x2 = float(input("Enter interval end value:\t"))
# Getting the root and iteration number
root, iter = false_position(fn, x1, x2)
# Printing root and iteration number
print("Root is at point %f at %d iteration" % (root, iter))