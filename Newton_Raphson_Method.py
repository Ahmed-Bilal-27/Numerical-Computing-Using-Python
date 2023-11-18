"""
This code is complementary to my Numerical Computing (CSC-475) course
offered at COMSATS University Islamabad, Wah Campus.
"""

# Defining method for Newton Raphson Method with default tolerance of 0.001 and
# maximum iterations of 1000.
# fx is the function of x
# dfx is the derivative of fx
# x is the starting data point in domain
def newton_raphson(fx, dfx, x, tol=0.001, maxiter=1000):
    for i in range(maxiter):
        x_new = x - fx(x) / dfx(x)
        # Checking the error
        if abs(x_new - x) < tol: break
        x = x_new
    return x_new, i

y = lambda x: x**2 - 6
dy = lambda x: 2*x
x, n = newton_raphson(y, dy, -1)
print('The root is %f after %d iterations' % (x, n))