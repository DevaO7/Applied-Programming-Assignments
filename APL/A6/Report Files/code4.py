# histogram for electron density
figure(1)
hist(X, bins=np.arange(0, n + 1, 1), edgecolor='white', rwidth=1, color='red')
title("Electron Density")
xlabel(r'Position$\rightarrow$')
ylabel(r'Number of Electrons$\rightarrow$')
show()
