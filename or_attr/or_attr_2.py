import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# initialzed the data
a= 0.2
b= 0.2
c=5.7
state_0 = [3, 0, 0]
t_span = np.linspace(0,600, 10000)



# define the ODE system
def f(state, time, a, b, c):
    x = state[0]
    y = state[1]
    z = state[2]
    return [-y-z, x+a*y, b+z*(x-c)]


# Solve the ODE system numerically, passing a, b, and c as additional arguments to rossler
solution = odeint(f, state_0, t_span, args=(a, b, c))

# Find the indices of the solution where 300 ≤ t ≤ 600
idx = np.logical_and(t_span >= 300, t_span <= 600)

# Plot the x and y coordinates of the solution over the specified time range
fig = plt.figure()
plt.plot(solution[idx, 0], solution[idx, 1])
plt.xlabel('x')
plt.ylabel('y')
plt.title('c = {}'.format(c))
plt.show()


