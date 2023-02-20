import numpy as np
import sys


sys.setrecursionlimit(1100)
# initialized the data
n=20000

x = np.random.rand(n, 1)
x_db_round=np.round(x,2)
x_test=[x for x in range(1,9)]



# T_(x) method for additaion. k is always be 0 and l =n-1

def T(k,l,x):
    if l-k >2:
        M = (l+k)//2
        return T(k, M,x) + T(M,l,x)
    else:
        if l-k==2:
            return x[k+1]+x[l]
        else:
            return x[k]+x[l]

# S_(x) method for additaion. k = n-1

#def S(k, x):
#    if k != 0:
#        return S(k-1, x) + x[k]
#    else:
#        return x[0]

def S(x):
    s_sum = 0
    for i in x:
        s_sum+=i
    return s_sum

t =T(0,n-1, x_db_round)
s=S(x_db_round)

np.random.shuffle(x_db_round)

t_star =T(0,n-1, x_db_round)
s_star=S(x_db_round)

V_s =s-s_star
V_t =t-t_star


print(V_s)
print(V_t)


