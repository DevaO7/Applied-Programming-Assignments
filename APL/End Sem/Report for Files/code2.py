# Question 3 - Current Elements in XY Plane
mu0 = 4*pi*1e-7
theta = linspace(0, 2*pi, 100)  # Dividing the loop into 100 sections
I = (4*pi)/mu0*cos(theta)  # Mag of I at each section of the loop
rx = 10*cos(theta)
ry = 10*sin(theta)
dirX = I*-1*sin(theta)  # Direction of the Current in x Direction
dirY = I*cos(theta)  # Direction of the Current in y Direction

fig, ax = plt.subplots()  # Quiver plot for the current
ax.quiver(rx, ry, dirX, dirY, color='black')
grid()
xlabel('X axis')
ylabel('Y axis')
title('Current Elements of the Loop')
show()
