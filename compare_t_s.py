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

# Generate 1025 linearly spaced points over the interval [-1, 1]
x_values_1025 = np.linspace(-1, 1, 1025)

# Compute f(x), s(x), and t(x) for the generated x values
f_values_1025 = f(x_values_1025)
s_values_1025 = s(x_values_1025)
t_values_1025 = t(x_values_1025)

# Compute the absolute errors for both approximations
abs_error_s = np.abs(f_values_1025 - s_values_1025)
abs_error_t = np.abs(f_values_1025 - t_values_1025)

# Find the maximum absolute errors (approximations for the infinity norms)
fs_infinity_norm = np.max(abs_error_s)
ft_infinity_norm = np.max(abs_error_t)

print("Approximation for ||f-s||_infinity:", fs_infinity_norm)
print("Approximation for ||f-t||_infinity:", ft_infinity_norm)

# Determine which approximation is better
if fs_infinity_norm < ft_infinity_norm:
    print("s(x) is a better approximation.")
else:
    print("t(x) is a better approximation.")

# Generate x values in the interval [-1, 1]
x_values = np.linspace(-1, 1, 1000)

# Compute f(x), s(x), and t(x) for the generated x values
f_values = f(x_values)
s_values = s(x_values)
t_values = t(x_values)

# Compute the errors for the original x_values
error_s = f_values - s_values
error_t = f_values - t_values

# Plot the error functions on the same graph
plt.plot(x_values, error_s, label='$f(x) - s(x)$', linestyle='--', linewidth=2)
plt.plot(x_values, error_t, label='$f(x) - t(x)$', linestyle=':', linewidth=2)

# Add labels and legend
plt.xlabel('x')
plt.ylabel('Error')
plt.title('Errors for $f(x) - s(x)$ and $f(x) - t(x)$')
plt.legend()

# Display the plot
plt.show()

