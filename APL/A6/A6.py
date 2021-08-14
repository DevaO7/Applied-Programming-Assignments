
from numpy import where, zeros
from numpy.core.numeric import ones
from numpy.random import rand
from numpy import where, zeros
from pylab import *
import sys
# Intiatializing the Values
n = 100  # spatial grid size.
M = 5  # number of electrons injected per turn.
nk = 500  # number of turns to simulate.
u0 = 5  # threshold velocity.
p = 0.25  # probability that ionization will occur
Msig = 2  # Standard Deviation
xx = zeros(n*M)  # Electron Postion Vector
u = zeros(n*M)  # ELectron Velocity Vector
dx = zeros(n*M)  # DIsplacement in current turn
I = []  # Intensity of Emitted Light
X = []  # Electron Position
V = []  # DIsplacement in current turn dx

# Getting input from Command Line Arguments
if(len(sys.argv) != 7):
    print("Default Paramereters are used")
    print('')
    print('For Specific Parameters, input the parameter value at the corresponding argument position as given below')
    print('')
    print('Arg1 - Spatial Grid Size(n)')
    print('Arg2 - Number of electrons injected per turn(M)')
    print('Arg3 - Number of turns to simulate(nk)')
    print('Arg4 - Threshold Velocity(u0)')
    print('Arg5 - Probability of Ionization(p)')
    print('Arg6 - Deviation of electrons injected per turn(Msig)')
    print('')


else:
    n = int(sys.argv[1])  # spatial grid size.
    M = int(sys.argv[2])  # number of electrons injected per turn.
    nk = int(sys.argv[3])  # number of turns to simulate.
    u0 = float(sys.argv[4])  # threshold velocity.
    p = float(sys.argv[5])  # probability that ionization will occur
    Msig = float(sys.argv[6])  # deviation of elctrons injected per turn


for k in range(1, nk+1):
    ii = where(xx > 0)
    dx[ii] = u[ii]+0.5  # Displacement the electron travels
    xx[ii] = xx[ii] + dx[ii]  # Recording the New Positions
    u[ii] = u[ii]+1  # New Speed of the electron
    jj = where(xx >= n)
    xx[jj] = 0  # Ejecting the Electrons
    u[jj] = 0
    dx[jj] = 0
    kk = where(u >= u0)  # Finding Electrons that has sufficient Energy
    # Probability of That Collision Emitting Light
    ll = where(rand(len(kk[0])) <= p)
    kl = kk[0][ll]
    u[kl] = 0
    rho = rand(len(kl))
    xx[kl] = xx[kl]-dx[kl]*rho
    I.extend(xx[kl].tolist())  # Recording the Intensity
    m = int(rand()*Msig+M)
    empty = where(xx == 0)
    t = (min(len(empty), m))
    xx[empty[:t]] = 1
    u[empty[0][:t]] = 0
    dx[empty[0][:t]] = 0
    X.extend(xx.tolist())  # Recording the Electron Density
    V.extend(u.tolist())  # Velocity of Electrons


# histogram for light intensity
figure(0)
pops, bins, temp = hist(I, bins=np.arange(
    0, n+1, 1), edgecolor='white', rwidth=1, color='red')  # draw histogram
xpos = 0.5*(bins[0:-1] + bins[1:])
title("Light Intensity")
xlabel(r'Position$\rightarrow$')
ylabel(r'Intensity$\rightarrow$')
show()

# Tabulate results
print("Intensity data:")
print("position     count")
for i in range(len(pops)):
    print(str(xpos[i]) + "   " + str(pops[i]))

# histogram for electron density
figure(1)
hist(X, bins=np.arange(0, n + 1, 1), edgecolor='white', rwidth=1, color='red')
title("Electron Density")
xlabel(r'Position$\rightarrow$')
ylabel(r'Number of Electrons$\rightarrow$')
show()

# phase space diagram
figure(2)
plot(X, V, 'o', color='red')
title("Electron Phase Space")
xlabel(r'Position$\rightarrow$')
ylabel(r'Velocity$\rightarrow$')
show()
