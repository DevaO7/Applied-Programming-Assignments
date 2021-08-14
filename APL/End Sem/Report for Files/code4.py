# Question 5 and 6 - Calc(l) function
def calc(l):
    Rx = xx-ones(1000)*10*cos(theta[l])  # X component of Rijk
    Ry = yy-ones(1000)*10*sin(theta[l])  # Y compoennt of Rijk
    Rl = (Rx**2+Ry**2+zz**2)**0.5  # Mod of Rijk
    Ax = (cos(theta[l])*numpy.exp(-0.1j*Rl)*-1*sin(theta[l]))/Rl
    Ay = (cos(theta[l])*numpy.exp(-0.1j*Rl)*cos(theta[l]))/Rl
    return Ax, Ay
