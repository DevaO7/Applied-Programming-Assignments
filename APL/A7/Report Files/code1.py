def lowpass(R1, R2, C1, C2, G, Vi):
    s = sy.symbols('s')
    A = Matrix([[0, 0, 1, -1/G], [-1/(1+s*R2*C2), 1, 0, 0],
                [0, -G, G, 1], [-1/R1-1/R2-s*C1, 1/R2, 0, s*C1]])
    B = Matrix([0, 0, 0, -Vi/R1])  # Source Vetor
    V = A.inv()*B
    return A, B, V


def tranferfuncConverter(Vo):
    n, d = fraction(Vo)
    n = Poly(n, s)
    d = Poly(d, s)
    nCoeff = n.all_coeffs()
    dCoeff = d.all_coeffs()
    nCoeff = [float(i) for i in nCoeff]
    dCoeff = [float(i) for i in dCoeff]
    H = lti(nCoeff, dCoeff)
    return H


s = symbols('s')  # Intializing
# Vi is the matrix containg the expressiosn of the Node voltages
A, B, Vi = lowpass(10e3, 10e3, 1e-9, 1e-9, 1.586, 1)
t = np.arange(0, 0.1, 1e-7)
Vo = Vi[3]  # Transfer Function
# Q1
H = tranferfuncConverter(Vo)  # H is the Transfer Function
time, voStep = sp.step(H, None, linspace(0, 0.001, 10**4))
plot(time, voStep)
title('Step Response of the LPF')
xlabel('Time')
ylabel('Output')
show()
