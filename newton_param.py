from math import exp, log, sin, cos, pi
import sys
import matplotlib.pyplot as plt
import numpy as np

# parametric function
def x(t):
    return sin(t)-0.35*sin(4*t)+0.25*sin(6*t)

def dx(t):
    return cos(t)-0.35*4*cos(4*t)+0.25*6*cos(6*t)

# Derivative of parametric function
def y(t):
    return cos(t) + 0.35*cos(4*t)+0.25*cos(6*t)

def dy(t):
    return -sin(t)-0.35*4*sin(4*t)-0.25*6*sin(6*t)

# Function to consider
def f(t, k):
    return (x(t)-x(t_vals[k]))**2 + (y(t)-y(t_vals[k]))**2 - 0.24**2

# Derivative of the function
def df(t, k):
    return 2*dx(t)*(x(t)-x(t_vals[k])) + 2*dy(t)*(y(t)-y(t_vals[k]))

# Starting guess
t_vals = [0]

# lists
x_list = []
y_list = []
# Perform ten steps of the Newton iteration
n=54
step=10
for i in range(1,n):
    
    init = t_vals[-1] + (2*pi*0.24)/(13.62)
    
    x_list.append(x(init))
    y_list.append(y(init))

    for itr in range(step):
        fv=f(init, i-1)
        # print(i,t_1,fv)
        init -= fv/df(init, i-1)

    t_vals.append(init)

# This is same function but using for ploting cruve

n=100
t = np.linspace(0, 2*pi, n)    
x_cv=np.sin(t)-0.35*np.sin(4*t)+0.25*np.sin(6*t)
y_cv=np.cos(t) + 0.35*np.cos(4*t)+0.25*np.cos(6*t)

   

plt.scatter(x_list, y_list)
plt.plot(x_cv, y_cv, color='r')
plt.show()



    

