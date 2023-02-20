import numpy as np
import sys
import time

sys.setrecursionlimit(1100)
# initialized the data
n=1024

#x = np.random.rand(n, 1)
#x_db_round=np.round(x,2)
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

# for only compute once 
#t_once =T(0,n-1, x_db_round)
#s_once=S(x_db_round)

print(t_once, s_once)
# instance of x
times = 20000

# start counting CPU time
st = time.time()

#list of random times
var_V_s = [0]*times
var_V_t = [0]*times
#var_V_s = []
#var_V_t = []


# start looping 20000 times 
for i in range(times):
    # create new random x 
    x = np.random.rand(n, 1)
    x_db_round=np.round(x,2)

    t =T(0,n-1, x_db_round)
    s=S(x_db_round)

    np.random.shuffle(x_db_round)

    t_star =T(0,n-1, x_db_round)
    s_star=S(x_db_round)

    V_s =s-s_star
    V_t =t-t_star

    var_V_s[i]=V_s
    var_V_t[i]=V_t

    #var_V_s.append(V_s)
    #var_V_t.append(V_t)
# end counting CPU time
ed=time.time()

process_time = ed - st
print(np.var(var_V_s))
print(np.var(var_V_t))
print(process_time,"s")


