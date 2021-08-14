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
legend()
show()
