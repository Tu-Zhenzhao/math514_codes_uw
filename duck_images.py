import numpy as np
from skimage.io import imread, imshow, show
import numpy.linalg as LA

# initial the data
n =3
s = 0

for i in range(n):
    duck = imread("duck_photos/single/light{}.jpg".format(i))
    s += duck

# reshape MN3 arrary as vector
M, N, D = s.shape
s.shape=(D*M*N)

# get 1-norm, 2-nrom and inf-norm
s_1 = LA.norm(s, 1)
s_2 = LA.norm(s, 2)
s_inf = LA.norm(s, np.inf)
print(s_1, s_2, s_inf)

# define the "S"
S = s/ s_inf
print(S)

# reshape back to image array for S
S.shape=(M,N,D)

imshow(S)
show()




