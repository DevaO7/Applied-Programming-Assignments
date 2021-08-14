def dftPlotter(y, xLim, Title):
    Y = fftshift(fft(y))/512
    w = linspace(-64, 64, 513)
    w = w[:-1]
    subplot(2, 1, 1)
    plot(w, abs(Y), lw=2)
    ylabel(r"$|Y|$", size=16)
    title(Title)
    xlim(-xLim, xLim)
    grid(True)
    subplot(2, 1, 2)
    plot(w, angle(Y), 'bo', lw=1, markersize='4')
    ii = where(abs(Y) > 1e-3)
    plot(w[ii], angle(Y[ii]), 'ro', lw=1)
    xlim([-xLim, xLim])
    ylabel(r"Phase of $Y$", size=16)
    xlabel(r"$\omega$", size=16)
    grid(True)
    show()


dftPlotter(sin(5*t), 10, 'Spectrum of sin(5t)')  # Example
dftPlotter((1+0.1*cos(t))*cos(10*t), 15,
           'Spectrum of 1+0.1*cos(t))*cos(10t) ')  # Example
