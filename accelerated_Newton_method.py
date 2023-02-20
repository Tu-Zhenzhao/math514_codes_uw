#!/usr/bin/python3
from math import exp, log, e, sqrt
import sys
import matplotlib.pyplot as plt


# Function to consider
def f(x):
    #return e**x-x-4
    #return x**2*(x-2)*(x-5)
    if x>=0:
        return x**(1/3.)
    else:
        return -(-x)**(1/3.)

# Derivative of the function
def df(x):
    #return e**x-1
    #return 4*x**3-21*x**2+20*
    #return 1/(3*abs(x)**(2/3))
    if x>= 0:
        return 1/(3*(x)**(2/3))
    else:
        return 1/(3*(-x)**(2/3))


# double derivative of the funtion
def ddf(x):
    #return  e**x
    #return 12*x**2-42*x+20
    if x>=0:
        return -2/(9*x**(5/3))
    else:
        return -2/(9*(-x)**(5/3))

# determinter how many roots f has
def root_test(x):
    if ddf(x) == 0:
        return None
    else:
        return (df(x)**2/(2*ddf(x)))

# Delta function
def delta(x):
    return df(x)**2-2*f(x)*ddf(x)

# Starting guess
x=-1

# exactly root
x_ect = 6.093651116281923e-16

# lists
x_list = []

# Perform ten steps of the accelerated Newton iteration
count=0
n=20
#while abs(f(x)) > 1e-14:
for i in range(n):
    # counting iterations
    count+=1

    #add x to list
    x_list.append(log(abs(x)))
    #x_list.append(abs(x))
    # Take Newton step
    r_t = root_test(x)
    fv = f(x)

    if delta(x) > 0:
        x_left = (ddf(x)*x-df(x)-sqrt(delta(x)))/ddf(x)
        x_right =  (ddf(x)*x-df(x)+sqrt(delta(x)))/ddf(x)
        if abs(x-x_left) < abs(x-x_right):
            x = x_left
            print(count,x,fv)
        else:
            x = x_right
            print(count,x,fv)

    else:
        x-=df(x)/ddf(x)
        #print(count,x,fv)
        print(count, x, fv)

    #else:
    #    print('second-order might be 0!')
    #    break

plt.scatter([range(n)], x_list)
plt.show()






