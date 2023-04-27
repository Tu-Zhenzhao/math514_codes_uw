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



def fixed_step_rk(f, x0, y0, h, L):
    N = int((L - x0) / h)
    x, y = [x0], [y0]

    for _ in range(N):
        y_next = second_order_rk_step(f, x[-1], y[-1], h)
        x.append(x[-1] + h)
        y.append(y_next)

    return np.array(x), np.array(y)

def main():
    x0, y0 = 0, 0
    L = 6 * np.sqrt(np.pi)
    h = 1e-4
    T_thresh = 0.1

    fixed_step_N = [2**i for i in range(6, 20)]
    adaptive_T_thresh = [4**(-i) for i in range(1, 15)]

    fixed_step_errors = []
    fixed_step_evals = []

    for N in fixed_step_N:
        h = L / N
        x, y = fixed_step_rk(f, x0, y0, h, L)
        error = np.abs(y[-1] - exact_solution(x[-1]))
        fixed_step_errors.append(error)
        fixed_step_evals.append(N)

    adaptive_step_errors = []
    adaptive_step_evals = []

    for T_thresh in adaptive_T_thresh:
        x, y = adaptive_rk(f, x0, y0, h, L, T_thresh)
        error = np.abs(y[-1] - exact_solution(x[-1]))
        adaptive_step_errors.append(error)
        adaptive_step_evals.append(len(x) - 1)

    plt.figure()
    plt.loglog(fixed_step_errors, fixed_step_evals, 'o-', label="Fixed Step Integrator")
    plt.loglog(adaptive_step_errors, adaptive_step_evals, 's-', label="Adaptive Step Integrator")
    plt.xlabel("Magnitude of Absolute Error at x=L")
    plt.ylabel("Total Number of Evaluations of f")
    plt.legend()
    plt.title("Log-Log Plot: Number of Evaluations vs Error")
    plt.show()

if __name__ == '__main__':
    main()

