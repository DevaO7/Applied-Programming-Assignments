from math import pi
from mpmath.functions.functions import re
from numpy.core.function_base import logspace
import scipy.signal as sp
from scipy.signal.ltisys import lsim, lti
import sympy as sy
import numpy as np
from matplotlib.pyplot import *
from sympy.core.symbol import symbols
from sympy.matrices import Matrix
from sympy.plotting.textplot import linspace
from sympy.polys.polytools import Poly
from sympy.simplify.radsimp import fraction
from sympy.utilities.lambdify import lambdify


def lowpass(R1, R2, C1, C2, G, Vi):
    s = sy.symbols('s')
    A = Matrix([[0, 0, 1, -1/G], [-1/(1+s*R2*C2), 1, 0, 0],
                [0, -G, G, 1], [-1/R1-1/R2-s*C1, 1/R2, 0, s*C1]])
    B = Matrix([0, 0, 0, -Vi/R1])  # Source Vetor
    V = A.inv()*B
    return A, B, V


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

# Q2

vi = np.sin(2000*pi*t)+np.cos(2e6*pi*t)  # Given Input
time, Vo_HP, svec = lsim(H, vi, t)  # Vo_HP is the output (Filtered Output)
plot(t, vi, label='Input Signal')
plot(t, Vo_HP, label='Filtered Signal')
title('Output to the given Signal')
xlabel('Time')
ylabel('Output/Input')
legend()
xlim(0, 1e-3)
show()

# Q3
A, B, V = highpass(10e3, 10e3, 1e-9, 1e-9, 1.586, 1)  # V is the Unknown Vector
Vo = V[3]  # Transfer Function for the HPF
H = tranferfuncConverter(Vo)  # Converting the Expression
w = logspace(0, 8, 801)
ss = 1j*w
f = lambdify(s, Vo, 'numpy')
loglog(w, abs(f(ss)), lw=2)  # Plotting the Maginute vs Frequency plot
title('Magnitude Plot for HPF(Logscale)')
xlabel('Frequency')
ylabel('Magnitude')
show()

# Q4
Vi1 = np.sin(1e3*pi*t)*np.exp(-1e2*t)  # Low Frequency Input signal
Vi2 = np.sin(1e6*pi*t)*np.exp(-1e4*t)  # High Frequency Input Signal
time, Vo1, svec = lsim(H, Vi1, t)  # Output to the Low Freq
time, Vo2, svec = lsim(H, Vi2, t)  # Output to the High Freq
plot(t, Vi1, label='Input Signal')
plot(time, Vo1, label='Filtered Signal')
xlabel('Time')
ylabel('Output/Input')
title('Low Frequency Damped Sinusoid Response')
xlim(0, 1e-2)
legend()
show()
plot(t, Vi2, label='Input Signal')
plot(time, Vo2, label='Filtered Signal')
xlabel('Time')
ylabel('Output/Input')
title('High Frequency Damped Sinusoid Response')
legend()
xlim(0, 0.4*1e-4)
show()

# Q5
time, voStep = sp.step(H, None, linspace(0, 0.001, 10**4))
plot(time, voStep)
title('Step Response for the HPF')
xlabel('Time')
ylabel('Output')
show()
