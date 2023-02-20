#!/usr/bin/python3
from math import exp, log, e
import sys
import matplotlib.pyplot as plt


# Function to consider
def f(x):
    return e**x-x-4
    #return log(0.5*x+1)**2

# Derivative of the function
def df(x):
    return e**x-1
    #return (log(1+0.5*x))/(1+0.5*x)
# Starting guess
x=1.5

# exactly root
x_ect = 6.093651116281923e-16

# lists
x_list = []

# Perform ten steps of the Newton iteration
n=50
for i in range(n):
    x_list.append(log(x))
    # Take Newton step
    fv=f(x)
    print(i,x,fv)
    x-=fv/df(x)

# Print solution on the final iteration
#print(n,x,f(x))

plt.scatter([range(n)], x_list)
plt.show()
