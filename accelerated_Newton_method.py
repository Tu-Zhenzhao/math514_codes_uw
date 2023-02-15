#!/usr/bin/python3
from math import exp, log, e
import sys
import matplotlib.pyplot as plt


# Function to consider
def f(x):
    return e^x-x-4

# Derivative of the function
def df(x):
    return e^x-1

# double derivative of the funtion
def ddf(x):
    return  e^x

# Starting guess
x=1

# exactly root
x_ect = 6.093651116281923e-16

# lists
x_list = []


