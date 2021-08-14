# Question 7 - Calculating the Vector Potential
A_x = 0  # Intializing
A_y = 0
for i in range(100):
    Ax, Ay = calc(i)
    A_x += Ax
    A_y += Ay
