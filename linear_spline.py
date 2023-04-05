import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x) = e^x
def f(x):
    return np.exp(x)

# Define the spline s(x) from the previous solution
def s(x):
    a1 = 1 / (np.exp(2) + 1)
    a2 = np.exp(2) / (np.exp(2) - 1)
    a3 = (np.exp(4) - np.exp(2)) / (np.exp(2) - 1)**2
    return 1 + a1 * x + a2 * x**2 + a3 * x**3

# Define the Taylor series t(x) for n = 3
def t(x):
    return 1 + x + x**2 / 2 + x**3 / 6

# Generate x values in the interval [-1, 1]
x_values = np.linspace(-1, 1, 1000)

# Compute f(x), s(x), and t(x) for the generated x values
f_values = f(x_values)
s_values = s(x_values)
t_values = t(x_values)

# Plot the functions on the same graph
plt.plot(x_values, f_values, label='$f(x) = e^x$', linewidth=2)
plt.plot(x_values, s_values, label='$s(x)$', linestyle='--', linewidth=2)
plt.plot(x_values, t_values, label='$t(x)$', linestyle=':', linewidth=2)

# Add labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparison of $f(x)$, $s(x)$, and $t(x)$')
plt.legend()

# Display the plot
plt.show()

