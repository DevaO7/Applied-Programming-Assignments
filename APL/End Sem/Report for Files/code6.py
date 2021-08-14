# Question 8 - Computing the Magnetic Field along z axis
B = (A_y[1, 2, :] - A_x[1, 1, :] - A_y[1, 0, :] + A_x[2, 1, :])/4

# Question 9 -  Plotting the Magnetic Field
loglog(z, abs(B))
grid()
xlabel('Z')
ylabel('|B(z)|')
title('Magnitude of Z component of Magnetic Field')
show()
