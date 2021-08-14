# Question 2 - Breaking the Volume into 3 by 3 by 1000 Mesh
x = arange(-1, 2, 1)
y = arange(-1, 2, 1)
z = arange(1, 1001, 1)
xx, yy, zz = meshgrid(x, y, z)  # Components of rijk
