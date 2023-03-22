def poly_product(b, c):
    m = len(b) - 1
    n = len(c) - 1
    d = [0] * (m + n + 1)
    for i in range(m + 1):
        for j in range(n + 1):
            d[i+j] += b[i] * c[j]
    return d


b = [1, 2, 3]
c = [1, 0, -3, 0, 9]
d = poly_product(b, c)
print(d)

def integral(b, s, r):
    n = len(b) - 1
    reslut = [0] * (n+1)
    for i in range(n+1):
        reslut[i] = (b[i]/(i+1))*(s**(i+1) - r**(i+1))
        print(reslut)
    return sum(reslut)

k = integral(b, 1,0)
print(k)
