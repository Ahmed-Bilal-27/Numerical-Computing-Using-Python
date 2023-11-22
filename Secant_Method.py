"""
This code is complementary to my Numerical Computing (CSC-475) course
offered at COMSATS University Islamabad, Wah Campus.
"""
# Defining method for Secant Method with default tolerance of 0.00001 and
# maximum iterations of 1000.
# fx is the function of x
# x1 is the first starting data point in domain
# x2 is the second starting data point in domain with default value of 0
def secant_method(fx, x1, x2 = 0, tol=0.00001, maxiter=1000):
    for i in range(maxiter):
        x_new = x2 -  (x2 - x1) / (fx(x2) - fx(x1)) * fx(x2)
        if abs(x_new - x2) < tol: break
        else:
            x1 = x2
            x2 = x_new
    else:
        print("Warning! Maximum iterations reached.")
    return x_new , i
fn = lambda x: x**3 - x - 1
p1 = float(input("Enter first starting point\t"))
p2 = float(input("Enter second starting point\t"))
p , n = secant_method(fn, p1, p2)
print("Root is at point %f at %d iteration" % (p, n))