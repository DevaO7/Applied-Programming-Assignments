x = linspace(0, 2*m.pi, 401)
x = x[:-1]
f = []
freal = vecExp(x)
for i in A:
    f = f + [sum(i*realexpCoeff)]
f2 = []
for i in A:
    f2 = f2 + [sum(i*cMatrixExp)]

# Plots the real Function
semilogyPlotter(x, freal, 'Real Plot', 'blue',
                'Plots for exp(x)', 'x', 'exp(x)')
# Plots the reconstructed function using coeff from Integ Method
semilogyPlotter(x, f, 'From Integ', 'red',
                'Plots for exp(x)', 'x', 'exp(x)')
# Plots the reconstructed function using coeff from Lst Sw Method
semilogyPlotter(x, f2, 'From Lstsq', 'green',
                'Plots for exp(x)', 'x', 'exp(x)')
legend()
show()
