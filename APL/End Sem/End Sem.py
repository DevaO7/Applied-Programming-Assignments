from math import exp, log
from matplotlib.pyplot import grid, legend, loglog, plot, show, title, xlabel, ylabel
from numpy import arange, c_, cos, pi, sin, zeros
import matplotlib.pyplot as plt
import numpy
from numpy.core.fromnumeric import shape, transpose
from numpy.core.function_base import linspace
from numpy.core.numeric import ones
from numpy.core.records import array
from numpy.lib.function_base import meshgrid
import scipy.linalg as lg


# Question 2 - Breaking the Volume into 3 by 3 by 1000 Mesh
x = arange(-1, 2, 1)
y = arange(-1, 2, 1)
z = arange(1, 1001, 1)
xx, yy, zz = meshgrid(x, y, z)  # Components of rijk


# Question 3 - Current Elements in XY Plane
mu0 = 4*pi*1e-7
theta = linspace(0, 2*pi, 100)  # Dividing the loop into 100 sections
I = (4*pi)/mu0*cos(theta)  # Mag of I at each section of the loop
rx = 10*cos(theta)
ry = 10*sin(theta)
dirX = I*-1*sin(theta)  # Direction of the Current in x Direction
dirY = I*cos(theta)  # Direction of the Current in y Direction

fig, ax = plt.subplots(figsize=(5, 5))  # Quiver plot for the current
ax.quiver(rx, ry, dirX, dirY, color='black')
grid()
xlabel('X axis')
ylabel('Y axis')
title('Current Elements of the Loop')
show()

# Question 4 -  The Vectors rl' and dl
r1ijk = [rx, ry, zeros(1000)]  # Rx and Ry are already computed
dlijk = [-1*sin(theta), cos(theta), zeros(1000)]  # Tangential Direction


# Question 5 and 6 - Calc(l) function
def calc(l):
    Rx = xx-ones(1000)*10*cos(theta[l])  # X component of Rijk
    Ry = yy-ones(1000)*10*sin(theta[l])  # Y compoennt of Rijk
    Rl = (Rx**2+Ry**2+zz**2)**0.5  # Mod of Rijk
    Ax = (cos(theta[l])*numpy.exp(-0.1j*Rl)*-1*sin(theta[l]))/Rl
    Ay = (cos(theta[l])*numpy.exp(-0.1j*Rl)*cos(theta[l]))/Rl
    return Ax, Ay


# Question 7 - Calculating the Vector Potential
A_x = 0  # Intializing
A_y = 0
for i in range(100):
    Ax, Ay = calc(i)
    A_x += Ax
    A_y += Ay

# Question 8 - Computing the Magnetic Field along z axis
B = (A_y[1, 2, :] - A_x[1, 1, :] - A_y[1, 0, :] + A_x[2, 1, :])/4

# Question 9 -  Plotting the Magnetic Field
loglog(z, abs(B))
grid()
xlabel('Z')
ylabel('|B(z)|')
title('Magnitude of Z component of Magnetic Field')
show()

# Question 10  - Fitting data to the given Model.
X = numpy.log(abs(B))
M = c_[ones(1000), numpy.log(z)]
sol = lg.lstsq(M, X)[0]
A = sol[0]
b = sol[1]
c = numpy.exp(A)
BFit = c*(z**b)
loglog(z, BFit, label='Fitted')
loglog(z, abs(B), color='r', label='Original')
legend()
xlabel('Z')
ylabel('|B(z)|')
grid()
title('Magnitude of Z component of Magnetic Field')
show()
print('Decay Rate = ', end='')
print(b)
