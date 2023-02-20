import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
from math import sqrt, pi, exp, log

# initialized the points
n=6
x = np.linspace(1,6,n)

# gamma function x_aix
x_range=np.array([1,2,3,4,5,6])

# gamma function y_aix
gamma = np.array([1,1,2,6,24,120])
log_gamma = np.log(gamma)

# define k values
k = 5

abs_er_ls = []

for i_val in range(1,(k+1)):
    # define the Vandermonde matrix
    V = np.vander(x_range[:(i_val+1)])

    # get coeffient by solving Vandermonde matrix
    #coeff = LA.solve(V,gamma[:(i_val+1)])
    coeff = LA.solve(V, log_gamma[:(i_val+1)])

    #polynomial function
    y = np.poly1d(coeff)

    # for y ploting polynomial 
    y_plot = [np.polyval(coeff, i) for i in x_range]

    # absolute error
    #abs_er = abs(y(1.5)-0.5*sqrt(pi))
    abs_er = abs(exp(y(1.5))-0.5*sqrt(pi))
    abs_er_ls.append(abs_er)

    # ploting each polynomial function
    #plt.plot(x, y_plot, label='k={lb}'.format(lb = i_val))


print(coeff, y, abs_er_ls)

# plot all data points in gamma
#plt.scatter(x, gamma)
#plt.scatter(x, log_gamma)

# plot the absolute errors
plt.scatter([range(k)], abs_er_ls)
plt.title("|exp(p_k(1.5))-|gamma(1.5)|")

#plt.legend()
plt.show()
