import numpy as np
import matplotlib.pyplot as plt
from math import exp, sin, cos, log
from scipy import stats

# initialized the data
k = 23
x=1
dis_dom =15
dis_dom_2 =11
def h(x):
    return 1/(2**x)
abs_err_1=[]
abs_err_2=[]
h_ls = []

# define original function
def f(x):
    return exp(4*sin(x))

# define first derivetive 
def df(x):
    return 4*cos(x)*exp(4*sin(x))

# define second derivetive
def ddf(x):
    return -4*exp(4*sin(x))*(sin(x)-4*cos(x)*cos(x))

# equation one
def eq_1(x,h):
    return (f(x-h)-2*f(x)+f(x+h))/(h**2)

# equation two
def eq_2(x,h):
    return (2*f(x-h)-4*f(x)+2*f(x+h))/(h**2) + (df(x-h)-df(x+h))/(2*h)


# calculate error
ddf = ddf(x)
for i in range(k+1):
    h_i = h(i)
    E_1 = abs(ddf-eq_1(x,h_i))
    E_2 = abs(ddf-eq_2(x,h_i))
    print(h_i, E_1, E_2)
    abs_err_1.append(E_1)
    abs_err_2.append(E_2)
    h_ls.append(h_i)


# linear regression fit
def linear_fun(x):
    return slope * x + intercept

slope, intercept, r, p, std_err = stats.linregress(np.log(h_ls[:dis_dom]), np.log(abs_err_1[:dis_dom]))

mymodel_1 = list(map(linear_fun, np.log(h_ls[:dis_dom])))

def linear_fun_2(x):
    return slope_2 * x + intercept_2

slope_2, intercept_2, r_2, p_2, std_err_2 = stats.linregress(np.log(h_ls[:dis_dom_2]), np.log(abs_err_2[:dis_dom_2]))

mymodel_2 = list(map(linear_fun_2, np.log(h_ls[:dis_dom_2])))

print(slope, intercept)
print(slope_2, intercept_2)
plt.xscale('log')
plt.yscale('log')
plt.scatter(h_ls, abs_err_1)
plt.scatter(h_ls, abs_err_2)
plt.plot(h_ls[:dis_dom], np.exp(mymodel_1))
plt.plot(h_ls[:dis_dom_2], np.exp(mymodel_2))
plt.legend(['E_1','E_2'])
plt.show()
