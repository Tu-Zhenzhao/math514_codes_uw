from math import exp,cos,sin,log
from linear_eq import *
import matplotlib.pyplot as plt


# Function to perform root-finding on
def f(x):
    return sin(x)**3-0.3

#def f(x):
#    return x**30-0.01

# Initial bracket, assuming f(a)<0 and f(b)>0
a=0
b=1

#the lists of output
bis_list=[]
impr_bis_list =[]

# iteration number 
it=20

# exactly root
x_ect = 0.7334452040086035
#x_ect=0.8576958985486272

# Perform the bisection search
for i in range(it):
    print("[",a,",",b,"]")
    c=0.5*(a+b)
    error_bis=abs(x_ect-c)
    bis_list.append(log(error_bis))
    if f(c)<0:
        
        # New interval is [c,b]
        a=c
    else:

        # New interval is [a,c]
        b=c

# Print the approximation to the root, and evaluate the function there
x=0.5*(a+b)
print("\nRoot at x =",x,"\nf(x) =",f(x), "This is bisection!!")

# initial for improved bisection
a=0
b=1


# this is improved bisection method
for i in range(it):
    print("[",a,",",b,"]")
    eq_list = lin_eq((a,f(a)), (b,f(b)))
    
    m = eq_list[0]
    cst= eq_list[1]
   

    d = -cst/m
    error_impr_bis=abs(d-x_ect)
    impr_bis_list.append(log(error_impr_bis))
    if f(d)*f(a)<0:
        c = (a+d)/2
        # New interval is [a,c]
        if f(c)*f(d)<0:
            a=c
            b=d
        else:
            a=a
            b=c
    else:
        c = (b+d)/2
        # New interval is [d,c]
        if f(c)*f(d)<0:
            a=d
            b=c
        else:
            a=c
            b=b

# Print the approximation to the root, and evaluate the function there
x=0.5*(a+b)
print("\nRoot at x =",x,"\nf(x) =",f(x),"This is improved bisection!!")


plt.scatter([range(20)], bis_list)
plt.scatter([range(20)], impr_bis_list)
plt.legend(["bisection", "improved_bisection"])
plt.show()







