import matplotlib.pyplot as plt

c = 0.4

k  =20
x_0 = 0
x_1 = 1.77
x_2 = -1
x_3 = 1.78

list_of_output_0=[x_0]
list_of_output_1=[x_1]
list_of_output_2=[x_2]
list_of_output_3=[x_3]


# for printing x_0=0
for i in range(2,k+1):
    x_k = 0.5*(x_0**2 + c)
    list_of_output_0.append(x_k)
    #print("[",x_k,"]")
    x_0 = x_k

# for printing x_1=1.77
for i in range(2,k+1):
    x_k = 0.5*(x_1**2 + c)
    list_of_output_1.append(x_k)
    #print("[",x_k,"]")
    x_1 = x_k

# for printing x_2=-1
for i in range(2,k+1):
    x_k = 0.5*(x_2**2 + c)
    list_of_output_2.append(x_k)
    #print("[",x_k,"]")
    x_2 = x_k

# for printing x_3=1.78
#for i in range(2,k+1):
#    x_k = 0.5*(x_3**2 + c)
#    list_of_output_3.append(x_k)
#    print("[",x_k,"]")
#    x_3 = x_k




plt.scatter([range(1,k+1)], list_of_output_0)
plt.scatter([range(1,k+1)], list_of_output_1)
plt.scatter([range(1,k+1)], list_of_output_2)
#plt.scatter([range(1,k+1)], list_of_output_3)

plt.legend(['x_0=0', 'x_0=1.77', 'x_0=-1'])
plt.show()

