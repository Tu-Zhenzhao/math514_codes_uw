import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin, exp, pi


# initial data
m = 50
def h(m):
    return 2*pi/m

# define function
def f(x):
    return 1/(5/4 -cos(x))
    #return sin(x)

# define Composite trapezium rule
def comp_trap(x_0, x_m, m):
    h_val = h(m)
    sum_f=0
    for i in range(m):
        x_1 = x_0 + h_val
        sum_f += (f(x_0) + f(x_1))
        x_0 = x_1
    return 0.5*h_val*sum_f
# exact reslut for int f(x)
exact_f = 8*pi/3


# create error lists
e_ls =[]
h_ls = []


# loop each m for Composite trapezium rule
for i in range(1,m+1):
    f_val = comp_trap(-pi, pi, i)
    error = abs(exact_f - f_val)
    print(i, f_val, error)
    e_ls.append(error)
    h_ls.append(h(i))



plt.xscale('log')
plt.yscale('log')
plt.scatter(h_ls, e_ls)
plt.show()

