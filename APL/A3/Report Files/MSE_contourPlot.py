A = arange(0, 2, 0.1)
B = arange(-0.2, 0, 0.01)
f = data[1]
gcol = []
k = 0
E = []
for i in A:
    temp1 = []
    for j in B:
        gcol = []
        for k in time:
            gcol = gcol + [g(k, i, j)]
        temp = subtract(f, gcol)
        temp = multiply(temp, temp)
        temp = sum(temp)/101
        temp1 = temp1 + [temp]
    E = E + [temp1]
clabel(contour(A, B, E, levels=20))
xlabel('A')
ylabel('B')
title('Contour of Error ij')
show()
