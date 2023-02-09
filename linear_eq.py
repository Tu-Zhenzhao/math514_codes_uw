#from numpy import ones,vstack
#from numpy.linalg import lstsq

#def lin_eq(p1, p2):
#    points = [p1,p2]
#    x_coords, y_coords = zip(*points)
#    A = vstack([x_coords,ones(len(x_coords))]).T
#    m, c = lstsq(A, y_coords, rcond=None)[0]
    # print("Line Solution is y = {m}x + {c}".format(m=m,c=c))

#    return [m, c]

def lin_eq(p1, p2):
    k = (p2[1]-p1[1])/(p2[0]-p1[0])
    c= p1[1]-k*p1[0]

    return [k,c]

