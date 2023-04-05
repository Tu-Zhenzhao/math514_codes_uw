import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

# initialzed the data
a= 0.2
b= 0.2
c_values = [1.5, 3.2, 4, 5.7]
state_0 = [3, 0, 0]
t_span = np.linspace(0,600, 10000)



# define the ODE system
def f(state, time, a, b, c):
    x = state[0]
    y = state[1]
    z = state[2]
    return [-y-z, x+a*y, b+z*(x-c)]


# Loop over the different values of c and plot the trajectory
for c in c_values:
    # Solve the ODE system numerically, passing a, b, and c as additional arguments to rossler
    solution = odeint(f, state_0, t_span, args=(a, b, c))

    # Find the indices of the solution where 300 ≤ t ≤ 600
    idx = np.logical_and(t_span >= 300, t_span <= 600)

    # Plot the solution in 3D over the specified time range
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(solution[idx, 0], solution[idx, 1], solution[idx, 2])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('c = {}'.format(c))
    plt.show()
