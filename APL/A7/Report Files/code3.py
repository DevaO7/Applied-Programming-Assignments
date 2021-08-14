def highpass(R1, R3, C1, C2, G, Vi):
    s = sy.symbols('s')
    A = Matrix([[0, -1, 0, 1/G],
                [s*C2*R3/(s*C2*R3+1), 0, -1, 0],
                [0, G, -G, 1],
                [(-1*s*C2)-(1/R1)-(s*C1), 0, s*C2, 1/R1]])

    B = Matrix([0,
                0,
                0,
                -Vi*s*C1])
    V = A.inv()*B
    return A, B, V


# Q3
A, B, V = highpass(10e3, 10e3, 1e-9, 1e-9, 1.586, 1)  # V is the Unknown Vector
Vo = V[3]  # Transfer Function for the HPF
H = tranferfuncConverter(Vo)  # Converting the Expression
w = logspace(0, 8, 801)
ss = 1j*w
f = lambdify(s, Vo, 'numpy')
loglog(w, abs(f(ss)), lw=2)  # Plotting the Maginute vs Frequency plot
title('Bode Magnitude Plot for HPF(Logscale)')
xlabel('Frequency')
ylabel('Magnitude')
show()
