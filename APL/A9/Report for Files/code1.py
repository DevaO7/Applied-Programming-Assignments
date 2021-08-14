def spectrum(y, T, window, plot1, xlim1, label1):
    t = linspace(-T*pi, T*pi, len(y)+1)
    t = t[:-1]
    N = len(t)
    dt = t[1]-t[0]
    fmax = 1/dt
    n = arange(N)
    wnd = fftshift(0.54+0.46*cos(2*pi*n/N))
    if window:
        y = y*wnd
    y[0] = 0
    y = fftshift(y)
    Y = fftshift(fft(y))/N
    if plot1:
        w = linspace(-pi*fmax, pi*fmax, N+1)
        w = w[:-1]
        figure()
        subplot(2, 1, 1)
        plot(w, abs(Y), 'b', lw=2, label=label1)
        legend()
        xlim(-xlim1, xlim1)
        ylabel(r"$|Y|$", size=16)
        grid(True)
        subplot(2, 1, 2)
        plot(w, angle(Y), 'bo', lw=2, label=label1)
        ii = where(abs(Y) > 1e-3)
        plot(w[ii], angle(Y[ii]), 'ro', lw=1)
        xlim(-xlim1, xlim1)
        ylabel(r"Phase of $Y$", size=16)
        xlabel(r"$\omega$", size=16)
        grid(True)
        show()
    else:
        return Y[8:]


t = linspace(-4*pi, 4*pi, 257)
t = t[:-1]
y = sin(sqrt(2)*t)
spectrum(y, 4, True, True, 4,  'With Hamming Window')  # Plotting the Spectrum
