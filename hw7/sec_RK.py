import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return -y + np.sin(x**2 / 2) + x * np.cos(x**2 / 2)

def exact_solution(x):
    return np.sin(x**2 / 2)

def second_order_rk(f, x0, y0, h, N):
    x = np.zeros(N + 1)
    y = np.zeros(N + 1)
    x[0], y[0] = x0, y0

    for i in range(N):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h, y[i] + h * k1)
        y[i + 1] = y[i] + (h / 2) * (k1 + k2)
        x[i + 1] = x[i] + h

    return x, y

def main():
    x0, y0 = 0, 0
    L = 6 * np.sqrt(np.pi)
    N = 240
    h = L / N

    x, y = second_order_rk(f, x0, y0, h, N)
    
    plt.subplot(1, 2, 1)
    plt.plot(x, y, label='Numerical Solution')
    plt.plot(x, exact_solution(x), label='Exact Solution', linestyle='dashed')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title("Second-Order Runge-Kutta Method")

    plt.subplot(1, 2, 2)
    error = np.abs(y - exact_solution(x))
    plt.plot(x, error, label='Error')
    plt.xlabel('x')
    plt.ylabel('Error')
    plt.title("Error between Exact and Numerical Solutions")

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()

