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
title('Magnitude of Z component of Magnetic Field')
show()
print('Decay Rate = ', end='')
print(b)
