import numpy as np
from matplotlib import pyplot as plt

# find the product of two polynomials
def poly_product(b, c):
    m = len(b) - 1
    n = len(c) - 1
    d = [0] * (m + n + 1)
    for i in range(m + 1):
        for j in range(n + 1):
            d[i+j] += b[i] * c[j]
    return d

# testing they are same
b = [1, 2, 3]
c = [1, 0, -3, 0, 9]
d = poly_product(b, c)
print(d)


# do integral for polynomial
def integral(b, s, r):
    n = len(b) - 1
    reslut = [0] * (n+1)
    for i in range(n+1):
        reslut[i] = (b[i]/(i+1))*(s**(i+1) - r**(i+1))
        #print(reslut)
    return sum(reslut)

k = integral(b, 1,0)
print(k)

# gram_schmidt to find orthrgnal basis
def gram_schmidt(n):
    # define the basis and set p_0 =1
    basis = np.zeros((n+1, n+1))
    basis[0][0] = 1
    for i in range(1, n+1):
        # set x^i 
        basis[i][i] = 1
        deg =  basis[i]
        for j in range(i):
            # computing nominator
            nmtr_val_1 =  poly_product(deg, basis[j])
            nmtr_1 = integral(nmtr_val_1, -0.5, -1) + integral(nmtr_val_1, 0.5, 0)
            nmtr_val_10 =  10*poly_product(deg, basis[j])
            nmtr_10 = integral(nmtr_val_10, 0, -0.5) + integral(nmtr_val_10, 1, 0.5)
            nmtr = nmtr_1 + nmtr_10
            # computing denominator
            denmtr_val_1 =  poly_product(basis[j], basis[j])
            denmtr_1 = integral(denmtr_val_1, -0.5, -1) + integral(denmtr_val_1, 0.5, 0)
            denmtr_val_10 =  10*poly_product(basis[j], basis[j])
            denmtr_10 = integral(denmtr_val_10, 0, -0.5) + integral(denmtr_val_10, 1, 0.5)
            denmtr = denmtr_1 + denmtr_10

            # compute the projection 
            norm = np.divide(nmtr, denmtr)
            p = norm*basis[j]
            # subtact for function
            basis[i]  = np.subtract(basis[i], p)
    return basis

m =  gram_schmidt(3)
print(m)



# define the polynomial functions 
def PolyCoefficients(x, coeffs):
    """ Returns a polynomial for ``x`` values for the ``coeffs`` provided.

    The coefficients must be in ascending order (``x**0`` to ``x**o``).
    """
    o = len(coeffs)
    print(f'# This is a polynomial of order {o}.')
    y = 0
    for i in range(o):
        y += coeffs[i]*x**i
    return y

x = np.linspace(0, 1, 100)
coeffs = gram_schmidt(11)
print("The coeffs of 12 degree =", coeffs[-1])
print("The coeffs of 11 degree =", coeffs[-2])
print("The coeffs of 10 degree =", coeffs[-3])
plt.plot(x, PolyCoefficients(x, coeffs[-1]))
plt.plot(x, PolyCoefficients(x, coeffs[-2]))
plt.plot(x, PolyCoefficients(x, coeffs[-3]))
plt.legend(['12 degree', '11 degree', '10 degree'])
plt.show()
