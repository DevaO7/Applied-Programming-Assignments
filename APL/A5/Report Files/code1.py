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

# Surface Plot for the potential
fig1 = figure(4)  # open a new figure
ax = p3.Axes3D(fig1)  # Axes3D is the means to do a surface plot
title('The 3-D surface plot of the potential')
surf = ax.plot_surface(X, Y, phi1.T, rstride=1, cstride=1, cmap=cm.jet)
show()
