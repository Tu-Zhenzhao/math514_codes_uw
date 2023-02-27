import numpy as np
from skimage.io import imread, imshow, show
import numpy.linalg as LA

# initial the data
n =7
L= np.zeros((n,778752))
P=294
b_ij = np.zeros((P, n))

# create L_array
for i in range(n):
    duck = imread("duck_photos/single/light{}.jpg".format(i))
    M, N, D = duck.shape
    duck.shape=(D*M*N)
    L[i] = duck
L_trans = np.transpose(L)

# find the vector when p=0 which is the first image named as 'msg000.jpg'
p_0=imread("duck_photos/message/msg000.jpg")
p_M, p_N,p_D=p_0.shape
p_0.shape=(p_M*p_N*p_D)


# for a fixed i value i=0, we got b_00 to b_06 by solving linear least squares
b = LA.lstsq(L_trans, p_0, rcond=None)[0].tolist()


#--------------------------------------------
# Compte the b_ij for all i=0,1,...,P-1

for i in range(P):
    if i//10 == 0:
        p=imread("duck_photos/message/msg00{}.jpg".format(i))
        p_M, p_N,p_D=p.shape
        p.shape=(p_M*p_N*p_D)
        b_i= LA.lstsq(L_trans, p, rcond=None)[0].tolist()
        b_ij[i] = b_i
    elif i//10 >= 1 and i//10 <= 9:
        p=imread("duck_photos/message/msg0{}.jpg".format(i))
        p_M, p_N,p_D=p.shape
        p.shape=(p_M*p_N*p_D)
        b_i= LA.lstsq(L_trans, p, rcond=None)[0].tolist()
        b_ij[i] = b_i
    else:
        p=imread("duck_photos/message/msg{}.jpg".format(i))
        p_M, p_N,p_D=p.shape
        p.shape=(p_M*p_N*p_D)
        b_i= LA.lstsq(L_trans, p, rcond=None)[0].tolist()
        b_ij[i] = b_i

b_ij_ls = b_ij.tolist()

# define d_ij
d_ij = np.zeros((P, n))

# loop every b_ij to determine the d_ij
for idx_b_i, b_i in enumerate(b_ij):
    M = max(b_i)*0.335
    for idx_b, b in enumerate(b_i):
        if b > M:
            d_ij[idx_b_i][idx_b]=1
        else:
            d_ij[idx_b_i][idx_b]=0



# convert d_ij to N_i 
N = np.zeros(P)

for idx_d_i, d_i in enumerate(d_ij):
    N_sum =0
    for idx_d, d in enumerate(d_i):
        N_sum += d_ij[idx_d_i][idx_d]*2**idx_d
        N[idx_d_i]= N_sum

msg = [chr(int(i)) for i in N]

print(''.join(msg))
