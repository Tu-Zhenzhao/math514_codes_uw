import numpy as np
from matplotlib import pyplot as plt
from math import e, exp, sqrt


def p_1(x):
    return 0.9+1.7*x

def e_x(x):
    return exp(x)

x = [0, 0.5, 1, 0, 0.5, 1]
y = [p_1(0), p_1(0.5), p_1(1), e_x(0), e_x(0.5), e_x(1)]
n=['p(0)','p(1/2)','p(1)','e(0)','e(1/2)','e(1)']
fig, ax = plt.subplots()
ax.scatter(x, y)

for i, txt in enumerate(n):
    ax.annotate(txt, (x[i], y[i]))





ex= np.vectorize(e_x)
x = np.linspace(0, 1, 100)
ax.plot(x, p_1(x))
ax.plot(x, ex(x))
ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)
#ax.spines['bottom'].set_position('zero')
#ax.spines['left'].set_position('zero')
plt.legend(['p_1(x)','exp(x)'])
plt.show()

