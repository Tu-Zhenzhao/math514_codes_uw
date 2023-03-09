import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, exp, pi, sqrt


# initialized data
N = 1024
h = 2*pi/N


# define function f(x)
def f(x):
    return cos(exp(3*cos(x)))

# exact df(x)
def df(x):
    return 3*sin(x)*exp(3*cos(x))*sin(exp(3*cos(x)))

# df(x) for diff_1
def df_1(x):
    return (f(x-2*h)+np.random.normal(0,1)*1e-3-8*(f(x-h)+np.random.normal(0,1)*1e-3)+8*(f(x+h)+np.random.normal(0,1)*1e-3)-(f(x+2*h)+np.random.normal(0,1)*1e-3))/(12*h)

# df(x) for diff_2
def df_2(x):
    return (-2*(f(x-2*h)+np.random.normal(0,1)*1e-3)-(f(x-h)+np.random.normal(0,1)*1e-3)+f(x+h)+np.random.normal(0,1)*1e-3+2*(f(x+2*h)+np.random.normal(0,1)*1e-3))/(10*h)

# define the error E function
def E(f0, fd):
    sum_f = 0
    #er_ls = []
    for k in range(N):
        x_k = k*h
        sqr_error = (f0(x_k) - fd(x_k))**2
        #er_ls.append(sqr_error)
        print(k, x_k, sqr_error)
        sum_f += sqr_error

    e = sqrt(sum_f/N)
    return e

# compute E_1 and E_2
E_1 = E(df, df_1)
E_2 = E(df, df_2)


print("E_1 =", E_1)
print("E_2 =", E_2)

