def genCoefcoscos():
    a1 = []  # FOr Absolute 'a' coefficients
    b1 = []  # FOr Absolute 'b' coefficients
    a2 = []  # FOr 'a' coefficients
    b2 = []  # FOr 'b' coefficientsos(m.cos(x))
    def f2(x, k): return m.cos(m.cos(x))*m.cos(x*k)
    def f3(x, k): return m.cos(m.cos(x))*m.sin(x*k)
    for i in range(26):
        if i == 0:
            temp = (quad(f1, 0, 2*m.pi)[0])/(m.pi*2)
            a1 = a1 + [abs(temp)]
            a2 = a2 + [temp]
        else:
            temp = (quad(f2, 0, 2*m.pi, args=i)[0])/(m.pi*2)
            temp2 = (quad(f3, 0, 2*m.pi, args=i)[0])/(m.pi*2)
            a1 = a1 + [abs(temp)]
            a2 = a2 + [temp]
            b1 = b1 + [abs(temp2)]
            b2 = b2 + [temp2]
    return a1, b1, a2, b2
