import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# initialzed the data
a= 0.2
b= 0.2
c=5.7
state_0 = [-2, 0, 0]
t_span = np.linspace(0,10, 10000)
state_vals = [-9, -8, -7, -6, -5, -4, -3, -2]
ys = []

# define the ODE system
def f(state, time, a, b, c):
    x = state[0]
    y = state[1]
    z = state[2]
    return [-y-z, x+a*y, b+z*(x-c)]



for state in state_vals:


    # Solve the ODE system numerically, passing a, b, and c as additional arguments to rossler
    solution = odeint(f, [state, 0, 0], t_span, args=(a, b, c))


    # determine when is the first time y goes to 0 which is y1

    # choose the the point between -0.1 and 0.1
    count = 0
    for idx, ls in enumerate(solution):
        if np.sign(ls[1]) != np.sign(solution[idx+1][1]):
            if count == 2:
                y1=ls
                ys.append(y1[0])
                print("y1 is:", ls)
                break
            else:
                count +=1
    # Plot the x and y coordinates of the solution over the specified time range
    fig = plt.figure()
    plt.plot(solution[:, 0], solution[:, 1])
    plt.plot(y1[0],y1[1], 'ro')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('x_0 = {}'.format(state))
    plt.show()

plt.scatter(state_vals, ys)
plt.xlabel('x_0')
plt.ylabel('x_1')
plt.show()
