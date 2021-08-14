
from numpy import arange, array, c_, loadtxt, multiply, subtract
from matplotlib.pyplot import *
from scipy.sparse.construct import vstack
import scipy.special as sp
import scipy.linalg as lg
from pylab import *


def g(t, a, b):
    return a*sp.jn(2, t)+b*t


print('')
print('Input Based On requirement')
print('Multiple Inputs are allowed, Should be separated by ","')
print('For Example, "3,4,5"\n')

print('3 - To Display All the Plots of f(t), but having different noises, along with the Exact Function')
print('6 - Computing M*p and compare with it with Column Vector g(t,A0,B0)')
print('7 - Contour Plot')
print('9 - Prints the Best Approximation')
print('10 - Plot of error in Estimating')
print('11 - loglog plot of error in estimating\n')


reqPlots = input('Input =')
reqPlots = reqPlots.split(',')

'#2 Loading the Data into the Program'
data = transpose(loadtxt('fitting.dat'))
time = data[0]
data = data[1:]
scl = logspace(-1, -3, 9)
realV = []
for i in time:
    realV = realV + [g(i, 1.05, -0.105)]
data = vstack((data, realV))


if '3' in reqPlots:
    for i in range(1, 10):  # Plotting the Data against time
        plot(time, data[i], label=scl[i-1])  # Plotted using matplotlib.pyplot
    # Plotting the Real Value, i.e without any noise
    plot(time, realV, 'black', label='True Value')

    title('Plotting the Data')  # Z axis Label
    legend()
    show()
if '5' in reqPlots:
    plot(time, data[1], label=scl[0])  # Plot for first Column
    plot(time, realV, label='True Value')  # PLotting the Exact Curve
    # PLacing the error bars in the graph
    errorbar(time[::5], data[1][::5], scl[0], fmt='ro', label='Error Bar')
    xlabel('Time')  # X axis Label
    ylabel('f(t)+Noise')  # Y axis Label
    title('With ErrorBar')
    legend()
    show()
if '6' in reqPlots:
    JCol = []
    for i in time:
        JCol = JCol + [sp.jn(2, i)]
    M = c_[JCol, time]  # M matrix is created
    b = array([1.05, -0.105])  # A0 and B0
    print('M = ', end='')
    print(M)
    print('b = ', end='')
    print(b)
    print("Sum of squared differences = ", end='')
    # Computing the sum of square differences
    Error = ((dot(M, b) - realV)**2).sum()
    print(((dot(M, b) - realV)**2).sum())
    if Error == 0:  # Verification
        print('Verified they are Equal')
if '7' in reqPlots:
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
if '9' in reqPlots or '10' in reqPlots or '11' in reqPlots:
    JCol = []
    for i in time:
        JCol = JCol + [sp.jn(2, i)]
    M = c_[JCol, time]
    solution = []
    for i in data:
        solution = solution + [lg.lstsq(M, i)[0]]
    solution = array(solution)
    print('Best Estimate of A and B =')
    print(solution)
    error = []
    for i in solution[:-1]:
        error = error + [array([(i[0]-1.05)**2, (i[1]+0.105)**2])]
    error = array(error)
    if '10' in reqPlots:
        plot(scl, error[:, 0], 'o', linestyle='dashed', label='Error in A')
        plot(scl, error[:, 1], 'o', linestyle='dashed', label='Error in B')
        xlabel('Noise Standard Deviation')
        ylabel('Error')
        legend()
        title('Variation of Error With Noise')
        show()
    if '11' in reqPlots:
        loglog(scl, error[:, 0], 'o', linestyle='dashed',
               label='Aerr', markersize='4')
        loglog(scl, error[:, 1], 'o', linestyle='dashed',
               label='Berr', markersize='4')
        xlabel('Noise Standard Deviation')
        ylabel('Error')
        legend()
        title('loglog error vs stdev')
        show()
