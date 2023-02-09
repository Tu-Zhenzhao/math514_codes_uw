from math import exp,cos
from linear_eq import *


def f(x):
    return exp(x)-x-4

a = 0
b=2

while b-a>1e-10:
    print("[",a,",",b,"]")
    eq_list = lin_eq((a,f(a)), (b,f(b)))
    m = eq_list[0]
    cst= eq_list[1]

    d = -cst/m
    if f(d)*f(a)<0:
        c = (a+d)/2
        # New interval is [a,c]
        a=c
        b=d
    else:
        c = (b+d)/2
        # New interval is [d,c]
        a=d
        b=c

# Print the approximation to the root, and evaluate the function there
x=0.5*(a+b)
print("\nRoot at x =",x,"\nf(x) =",f(x))

