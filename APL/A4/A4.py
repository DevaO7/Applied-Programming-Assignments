import math as m
import numpy as np
from matplotlib.pyplot import *
from numpy.core.function_base import linspace
from numpy.core.shape_base import vstack
import scipy as sp
from scipy.integrate.quadpack import quad


def vecCoscos(space):
    vecCoscos = []
    for i in space:
        vecCoscos = vecCoscos + [m.cos(m.cos(i))]
    return np.array(vecCoscos)


def vecExp(space):
    vecExp = []
    for i in space:
        vecExp = vecExp + [m.exp(i)]
    return np.array(vecExp)


def genCoefexp():
    a1 = []
    b1 = []
    a2 = []
    b2 = []
    def f1(x): return m.exp(x)
    def f2(x, k): return m.exp(x)*m.cos(x*k)
    def f3(x, k): return m.exp(x)*m.sin(x*k)
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


def genCoefcoscos():
    a1 = []
    b1 = []
    a2 = []
    b2 = []
    def f1(x): return m.cos(m.cos(x))
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


def loglogPlotter(x1, a2, label1, color1, title1, xlabel1, ylabel1):
    loglog(x1, a2, 'r.', label=label1, color=color1)
    title(title1)
    xlabel(xlabel1)
    ylabel(ylabel1)
    legend()


def semilogyPlotter(x1, a2, label1, color1, title1, xlabel1, ylabel1):
    semilogy(x1, a2, 'r.', label=label1, color=color1)
    title(title1)
    xlabel(xlabel1)
    ylabel(ylabel1)
    legend()


def genCoeffbyLstsq(func):
    x = linspace(0, 2*m.pi, 401)
    x = x[:-1]  # drop last term to have a proper periodic integral
    A = np.zeros((400, 51))  # allocate space for A
    if func == 1:
        b = vecExp(x)
    if func == 2:
        b = vecCoscos(x)
    A[:, 0] = 1  # col 1 is all ones
    for k in range(1, 26):
        A[:, k] = np.cos(k*x)  # cos(kx) column
        A[:, k+25] = np.sin(k*x)  # sin(kx) column
    c1 = sp.linalg.lstsq(A, b)[0]
    a1 = c1[:26]
    b1 = c1[26:]
    b2 = []
    a2 = []
    for i in a1:
        a2 = a2+[abs(i)]
    for i in b1:
        b2 = b2+[abs(i)]
    return a1, b1, a2, b2, c1, A


print('1 - To Plot the function over the interval 0 to 2*pi')
print('2 - SemiLog and Loglog plots of the Coeffecients for exp(x)')
print('3 - SemiLog and Loglog plots of the Coeffecients for coscos(x)')
print('4 - Plot for the coeffecients obtained using Least Squares - exp(x)')
print('5 - Plot for the coeffecients obtained using Least Squares - coscos(x)')
print('6 - To print the deviation, Maximum Deviation for exp(x)')
print('7 - To print the deviation, Maximum Deviation for coscos(x)')
print('8 - To plot exp(x), reconstructed exp(x) using fourier series obtained from both Integ and lstsq')
print('9 - To plot coscos(x), reconstructed coscos(x) using fourier series obtained from both Integ and lstsq')
print('')
print('Input Based on Requirement. You could give multiple keys, for example the input can be "1,4,7,8". Should be seperated by Commas')
abs_aexp, abs_bexp, aexp, bexp = genCoefexp()
abs_acos, abs_bcos, acos, bcos = genCoefcoscos()
lst_aexp, lst_bexp, lst_abs_aexp, lst_abs_bexp, cMatrixExp, A = genCoeffbyLstsq(
    1)
lst_acos, lst_bcos, lst_abs_acos, lst_abs_bcos, cMatrixCos, A = genCoeffbyLstsq(
    2)
realexpCoeff = np.array(aexp+bexp)
realcosCoeff = np.array(acos+bcos)
reqQues = input('Input =').split(',')
if '1' in reqQues:
    space = np.linspace(0, m.pi*2, 401)
    # The fucntion takes in a vector and returns a coscos() of the vector
    f1x = vecCoscos(space)
    plot(space, f1x)  # Plot for coscos()
    title('cos(cos(x)) - Orginal Plot')
    xlabel('x')
    ylabel('cos(cos(x))')
    grid()
    show()
    # The fucntion takes in a vector and returns a exp() of the vector
    f2x = vecExp(space)
    semilogy(space, f2x)  # Semilogy plot for exp()
    title('exp(x) - Orginal Plot')
    xlabel('x')
    ylabel('exp(x)')
    grid()
    show()
if '2' in reqQues:
    x = np.arange(26)
    loglogPlotter(x, abs_aexp, 'a', 'red',
                  'Loglog plot of the Coeffecients for exp(x)', 'n', 'Mag of Coeffecient')
    loglogPlotter(x[1:], abs_bexp, 'b', 'blue',
                  'Loglog plot of the Coeffecients for exp(x)', 'n', 'Mag of Coeffecient')
    show()
    semilogyPlotter(x, abs_aexp, 'a', 'red',
                    'Semilogy plot of the Coeffecients for exp(x)', 'n', 'Mag of Coeffecient')
    semilogyPlotter(x[1:], abs_bexp, 'b', 'blue',
                    'Semilogy plot of the Coeffecients for exp(x)', 'n', 'Mag of Coeffecient')
    show()
if '3' in reqQues:
    x = np.arange(26)
    loglogPlotter(x, abs_acos, 'a', 'red',
                  'Loglog plot of the Coeffecients for coscos(x)', 'n', 'Mag of Coeffecient')
    loglogPlotter(x[1:], abs_bcos, 'b', 'blue',
                  'Loglog plot of the Coeffecients for coscos(x)', 'n', 'Mag of Coeffecient')
    show()
    semilogyPlotter(x, abs_acos, 'a', 'red',
                    'Semilogy plot of the Coeffecients for coscos(x)', 'n', 'Mag of Coeffecient')
    semilogyPlotter(x[1:], abs_bcos, 'b', 'blue',
                    'Semilogy plot of the Coeffecients for coscos(x)', 'n', 'Mag of Coeffecient')
    show()
if '4' in reqQues:
    x = np.arange(26)
    loglogPlotter(x, lst_abs_aexp, 'a - lstsq', 'green',
                  'Loglog plot of the Coeffecients for exp(x)', 'n', 'Mag of Coeffecient')
    loglogPlotter(x[1:], lst_abs_bexp, 'b - lstsq', 'lightgreen',
                  'Loglog plot of the Coeffecients for exp(x)', 'n', 'Mag of Coeffecient')
    loglogPlotter(x, abs_aexp, 'a - integ', 'red',
                  'Loglog plot of the Coeffecients for exp(x)', 'n', 'Mag of Coeffecient')
    loglogPlotter(x[1:], abs_bexp, 'b - integ', 'darkred',
                  'Loglog plot of the Coeffecients for exp(x)', 'n', 'Mag of Coeffecient')
    show()
    semilogyPlotter(x, lst_abs_aexp, 'a - lstsq', 'green',
                    'Semilog plot of the Coeffecients for exp(x)', 'n', 'Mag of Coeffecient')
    semilogyPlotter(x[1:], lst_abs_bexp, 'b - lstsq', 'lightgreen',
                    'Semilog plot of the Coeffecients for exp(x)', 'n', 'Mag of Coeffecient')
    semilogyPlotter(x, abs_aexp, 'a - integ', 'red',
                    'Semilog plot of the Coeffecients for exp(x)', 'n', 'Mag of Coeffecient')
    semilogyPlotter(x[1:], abs_bexp, 'b - integ', 'darkred',
                    'Semilog plot of the Coeffecients for exp(x)', 'n', 'Mag of Coeffecient')
    show()
if '5' in reqQues:
    x = np.arange(26)
    loglogPlotter(x, lst_abs_acos, 'a - lstsq', 'green',
                  'Loglog plot of the Coeffecients for coscos(x)', 'n', 'Mag of Coeffecient')
    loglogPlotter(x[1:], lst_abs_bcos, 'b - lstsq', 'lightgreen',
                  'Loglog plot of the Coeffecients for coscos(x)', 'n', 'Mag of Coeffecient')
    loglogPlotter(x, abs_acos, 'a - integ', 'red',
                  'Loglog plot of the Coeffecients for coscos(x)', 'n', 'Mag of Coeffecient')
    loglogPlotter(x[1:], abs_bcos, 'b - integ', 'darkred',
                  'Loglog plot of the Coeffecients for coscos(x)', 'n', 'Mag of Coeffecient')
    show()
    semilogyPlotter(x, lst_abs_acos, 'a - lstsq', 'green',
                    'Semilog plot of the Coeffecients for coscos(x)', 'n', 'Mag of Coeffecient')
    semilogyPlotter(x[1:], lst_abs_bcos, 'b - lstsq', 'lightgreen',
                    'Semilog plot of the Coeffecients for coscos(x)', 'n', 'Mag of Coeffecient')
    semilogyPlotter(x, abs_acos, 'a - integ', 'red',
                    'Semilog plot of the Coeffecients for coscos(x)', 'n', 'Mag of Coeffecient')
    semilogyPlotter(x[1:], abs_bcos, 'b - integ', 'darkred',
                    'Semilog plot of the Coeffecients for coscos(x)', 'n', 'Mag of Coeffecient')
    show()
if '6' in reqQues:
    deviaA = []
    deviaB = []
    print('Deviation in "a" Coeffecients,')
    for i in range(26):
        print('a{} = {}'.format(i, abs(abs_aexp[i]-lst_abs_aexp[i])))
        deviaA = deviaA + [abs(abs_aexp[i]-lst_abs_aexp[i])]
    print('Deviation in "b" Coeffecients,')
    for i in range(25):
        print('b{} = {}'.format(i+1, abs(abs_bexp[i]-lst_abs_bexp[i])))
        deviaB = deviaB + [abs(abs_bexp[i]-lst_abs_bexp[i])]
    print('Maximum Deviation = {}'.format(max([max(deviaA), max(deviaB)])))
if '7' in reqQues:
    deviaA = []
    deviaB = []
    print('Deviation in "a" Coeffecients,')
    for i in range(26):
        print('a{} = {}'.format(i, abs(abs_acos[i]-lst_abs_acos[i])))
        deviaA = deviaA + [abs(abs_acos[i]-lst_abs_acos[i])]
    print('Deviation in "b" Coeffecients,')
    for i in range(25):
        print('b{} = {}'.format(i+1, abs(abs_bcos[i]-lst_abs_bcos[i])))
        deviaB = deviaB + [abs(abs_bcos[i]-lst_abs_bcos[i])]
    print('Maximum Deviation = {}'.format(max([max(deviaA), max(deviaB)])))
if '8' in reqQues:
    x = linspace(0, 2*m.pi, 401)
    x = x[:-1]
    f = []
    freal = vecExp(x)
    for i in A:
        f = f + [sum(i*realexpCoeff)]
    f2 = []
    for i in A:
        f2 = f2 + [sum(i*cMatrixExp)]

    semilogyPlotter(x, freal, 'Real Plot', 'blue',
                    'Plots for exp(x)', 'x', 'exp(x)')
    semilogyPlotter(x, f, 'From Integ', 'red',
                    'Plots for exp(x)', 'x', 'exp(x)')
    semilogyPlotter(x, f2, 'From Lstsq', 'green',
                    'Plots for exp(x)', 'x', 'exp(x)')
    legend()
    show()
if '9' in reqQues:
    x = linspace(0, 2*m.pi, 401)
    x = x[:-1]
    f = []
    freal = vecCoscos(x)
    for i in A:
        f = f + [sum(i*realcosCoeff)]
    f2 = []
    for i in A:
        f2 = f2 + [sum(i*cMatrixCos)]
    plot(x, f2, 'ro',  label='lst Sq')
    plot(x, f, 'go',  label='Integ')
    plot(x, freal, 'bo', label='real')
    legend()
    show()
