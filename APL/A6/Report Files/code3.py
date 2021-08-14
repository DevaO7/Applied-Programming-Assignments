# histogram for light intensity
figure(0)
pops, bins, temp = hist(I, bins=np.arange(
    0, n+1, 1), edgecolor='white', rwidth=1, color='black')  # draw histogram
xpos = 0.5*(bins[0:-1] + bins[1:])
title("Light Intensity")
xlabel(r'Position$\rightarrow$')
ylabel(r'Intensity$\rightarrow$')
show()
