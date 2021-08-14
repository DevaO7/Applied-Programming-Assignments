from numpy import arange, array, dtype, meshgrid, zeros
from numpy.ma.core import dot, where
from pylab import *
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib.pyplot import *
import scipy.linalg as sp

# Defining the Paramters

try:
    Nx = int(sys.argv[1])
except IndexError:
    Nx = 25
try:
    Ny = int(sys.argv[2])
except IndexError:
    Ny = 25
try:
    radius = int(sys.argv[3])
except IndexError:
    radius = 8


try:
    if int(sys.argv[4]) > 2300:
        print('Niter is too high.Niter should be less than 2300')
        exit()
    Niter = int(sys.argv[4])
except IndexError:
    Niter = 1500
else:
    print('Enter Niter less than 2300')
    exit()


# Initializing the Potential Array

phi = zeros([Nx, Ny])
x = arange(-(Nx-1)/2, (Nx+1)/2)
y = arange(-(Ny-1)/2, (Ny+1)/2)
X, Y = meshgrid(x, y)
ii = where(X*X+Y*Y <= radius*radius)
phi[ii] = 1
error = []
# Updating the Potential, Computing the Error , Updating the Boundary Conditions
for i in range(Niter):
    oldphi = phi.copy()
    phi[1:-1, 1:-1] = 0.25 * \
        (phi[1:-1, 0:-2] + phi[1:-1, 2:] + phi[0:-2, 1:-1] + phi[2:, 1:-1])
    phi[:, 0] = phi[:, 1]
    phi[:, -1] = phi[:, -2]
    phi[0, :] = phi[1, :]
    phi[ii] = 1
    error = error+[(abs(phi-oldphi)).max()]
phi1 = phi[::-1]

# Contour plot of the Potential Function
contourf(X, Y, phi1, levels=20)
scatter(ii[0] - (Nx - 1) / 2, ii[1] - (Ny - 1) / 2, color='r', s=20)
xlabel('X axis')
ylabel('Y axis')
title('Contour Plot for the Potential')
show()

# Semilog PLot for Error
x = array(arange(Niter))
semilogy(x, error)
xlabel('Iterartion')
ylabel('Error')
title('Semilog Plot for Error')
show()

# LogLog PLot for Error
loglog(x, error)
xlabel('Iterartion')
ylabel('Error')
title('loglog Plot for Error')
show()

# Fitting the Entire Vector
c = ones([Niter], dtype=float)
Amatrix = transpose(array([x, c]))
yMatrix = log(error)
xMatrix = sp.lstsq(Amatrix, transpose(yMatrix))[0]

# Fitting for the portion after 500th Iter
c = ones([len(error[500:])], dtype=float)
x = array(arange(500, Niter))
Amatrix2 = transpose(array([x, c]))
yMatrix2 = log(error[500:])
xMatrix2 = sp.lstsq(Amatrix2, transpose(yMatrix2))[0]

# Plotting the Fits
x = array(arange(Niter))
y1 = exp(dot(Amatrix, xMatrix))
y2 = exp(dot(Amatrix, xMatrix2))
semilogy(x, y1, label='Fit1')
semilogy(x, y2, label='Fit2')
semilogy(x, error, label='Error')  # X is the real error
xlabel('Iterartion')
ylabel('Error')
title('semilog Plot for Error')
legend()
show()

# Surface Plot for the potential
fig1 = figure(4)  # open a new figure
ax = p3.Axes3D(fig1)  # Axes3D is the means to do a surface plot
surf = ax.plot_surface(X, Y, phi1.T, rstride=1, cstride=1, cmap=cm.jet)
title('The 3-D surface plot of the potential')
show()

# Quiver Plot for the Current

Jx = zeros([Nx, Ny])
Jy = zeros([Nx, Ny])
Jy[1:-1, :] = -0.5 * (phi[:-2, :] - phi[2:, :])
Jx[:, 1:-1] = 0.5 * (phi[:, :-2] - phi[:, 2:])
Jx = Jx[::-1]
Jy = Jy[::-1]
quiver(X, Y, Jx, Jy, scale=5)
scatter(ii[0] - (Nx - 1) / 2, ii[1] - (Ny - 1) / 2, color='r', s=10)
title('Vector Plot for Current')
gca().set_aspect('equal', adjustable='box')
show()
