import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return -y + np.sin(x**2 / 2) + x * np.cos(x**2 / 2)

def exact_solution(x):
    return np.sin(x**2 / 2)

def second_order_rk_step(f, x, y, h):
    k1 = f(x, y)
    k2 = f(x + h, y + h * k1)
    y_next = y + (h / 2) * (k1 + k2)
    return y_next

def third_order_rk_step(f, x, y, h):
    k1 = f(x, y)
    k2 = f(x + h, y + h * k1)
    k3 = f(x + h / 2, y + h * (k1 / 4 + k2 / 4))
    y_next = y + (h / 6) * (k1 + 4 * k3 + k2)
    return y_next

def adaptive_rk(f, x0, y0, h, L, T_thresh):
    x, y = [x0], [y0]

    while x[-1] < L:
        h = min(1.1 * h, L - x[-1])

        y_next_2nd_order = second_order_rk_step(f, x[-1], y[-1], h)
        y_next_3rd_order = third_order_rk_step(f, x[-1], y[-1], h)

        T_est = abs(y_next_2nd_order - y_next_3rd_order) / h

        if T_est > T_thresh:
            h /= 2
        else:
            x.append(x[-1] + h)
            y.append(y_next_2nd_order)

    return np.array(x), np.array(y)

def main():
    x0, y0 = 0, 0
    L = 6 * np.sqrt(np.pi)
    h = 1e-4
    T_thresh = 0.1

    x, y = adaptive_rk(f, x0, y0, h, L, T_thresh)

    print(f"Number of steps: {len(x) - 1}")

    plt.subplot(1, 2, 1)
    plt.plot(x, y, label='Numerical Solution')
    plt.plot(x, exact_solution(x), label='Exact Solution', linestyle='dashed')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title("Adaptive Runge-Kutta Method")



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
