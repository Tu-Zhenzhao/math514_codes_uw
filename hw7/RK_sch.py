import numpy as np
import matplotlib.pyplot as plt

def f(x, y, z):
    return z

def g(x, y, z):
    return 2 + 2*x - 16*z**4

def runge_kutta(x, y, z, h, g0):
    z[0] = g0
    for i in range(len(x) - 1):
        k1_y = h * f(x[i], y[i], z[i])
        k1_z = h * g(x[i], y[i], z[i])
        
        k2_y = h * f(x[i] + 2/3*h, y[i] + 2/3*k1_y, z[i] + 2/3*k1_z)
        k2_z = h * g(x[i] + 2/3*h, y[i] + 2/3*k1_y, z[i] + 2/3*k1_z)

        k3_y = h * f(x[i] + 1/2*h, y[i] + 1/2*k2_y, z[i] + 1/2*k2_z)
        k3_z = h * g(x[i] + 1/2*h, y[i] + 1/2*k2_y, z[i] + 1/2*k2_z)
        
        y[i + 1] = y[i] + k3_y
        z[i + 1] = z[i] + k3_z

    return y, z

def bisection(func, a, b, tol):
    c = a
    while (b - a) >= tol:
        c = (a + b) / 2
        if func(c) == 0.0:
            break
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
    return c

def y_at_1(g):
    y, z = runge_kutta(x, y0, z0, h, g)
    return y[-1]

N = 1000
h = 1/N
x = np.linspace(0, 1, N+1)
y0 = np.zeros(N+1)
z0 = np.zeros(N+1)

g_lower = -0.6044
g_upper = 1

g_tol = 1e-6
g_optimal = bisection(y_at_1, g_lower, g_upper, g_tol)

y_final, z_final = runge_kutta(x, y0, z0, h, g_optimal)

plt.plot(x, y_final, label='y(x)')
plt.plot(x, z_final, label="y'(x)")
plt.xlabel('x')
plt.ylabel('y, y\'')
plt.legend()
plt.show()

