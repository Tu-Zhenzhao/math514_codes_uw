import numpy as np
import numpy.linalg as LA


n=10

for i in range(n):
    A =np.random.rand(2,2)
    B= np.random.rand(2,2)

    A_iv = LA.inv(A)
    B_iv=LA.inv(B)
    AB_iv=LA.inv(A+B)

    cond_A = LA.norm(A)*LA.norm(A_iv)
    cond_B = LA.norm(B)*LA.norm(B_iv)

    cond_AB =  LA.norm(A+B)*LA.norm(AB_iv)

    if cond_AB > cond_A + cond_B:
        print(cond_A)
        print(cond_B)
        print(cond_AB)
        print(A)
        print("==========")
        print(B)
        print("==========")
        print(A+B)



