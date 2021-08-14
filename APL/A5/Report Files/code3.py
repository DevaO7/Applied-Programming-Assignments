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
