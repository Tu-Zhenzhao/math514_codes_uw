#!/usr/bin/python3
from math import exp, log, e, sqrt
import sys
import matplotlib.pyplot as plt


# Function to consider
def f(x):
    return e**x-x-4

# Derivative of the function
def df(x):
    return e**x-1

# double derivative of the funtion
def ddf(x):
    return  e**x


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
x=1.5

# exactly root
x_ect = 6.093651116281923e-16

# lists
x_list = []

# Perform ten steps of the accelerated Newton iteration
count=0
while abs(f(x)) > 1e-14:
    # counting iterations
    count+=1

    #add x to list
    #x_list.append(log(x))
    # Take Newton step
    r_t = root_test(x)
    fv = f(x)
    if r_t-fv == 0:
        x-=df(x)/ddf(x)
        print(count,x,fv)
    elif r_t-fv > 0:
        x_left = (ddf(x)*x-df(x)-sqrt(delta(x)))/ddf(x)
        x_right =  (ddf(x)*x-df(x)+sqrt(delta(x)))/ddf(x)
        if abs(x-x_left) < abs(x-x_right):
            x = x_left
            print(count,x,fv)
        else:
            x = x_right
            print(count,x,fv)
    else:
        print('second-order might be 0!')
        break








