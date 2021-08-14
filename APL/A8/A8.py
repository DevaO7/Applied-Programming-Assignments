from numpy import cos, exp, pi, sin, sqrt, where
from numpy.lib.function_base import angle
from pylab import *
t = linspace(-4*pi, 4*pi, 513)
t = t[:-1]


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
dftPlotter(sin(t)**3, 15, 'Spectrum of (sin(t))^3')
dftPlotter(cos(t)**3, 15, 'Spectrum of (cos(t))^3')
dftPlotter(cos(20*t+5*cos(t)), 35, 'Spectrum of 20t+5*cos(t))')


def estimate(N, T):
    t = linspace(- T / 2, T / 2, N + 1)[:-1]
    w = linspace(- N * pi / T, N * pi / T, N + 1)[:-1]
    y = exp(-0.5 * t**2)
    Y_true = exp(-0.5 * w**2) / sqrt(2 * pi)
    Y = fftshift(fft(ifftshift(y))) * T / (2 * pi * N)
    return sum(abs(Y - Y_true)), w, Y, Y_true


i = 1
while estimate(N=512, T=i * pi)[0] > 1e-6:
    i += 1

print('Time range for accurate spectrum : ' + str(i) + 'pi')
print('Error : ' + str(estimate(N=512, T=i * pi)[0]))

w, Y, Y_true = estimate(N=512, T=i * pi)[1:]

xLim = 5
subplot(2, 1, 1)
plot(w, abs(Y), lw=2)
title('Spectrum of exp(-(t^2)/2)')
ylabel(r"$|Y|$", size=16)
xlim([-xLim, xLim])
grid(True)
subplot(2, 1, 2)
plot(w, angle(Y), 'bo', lw=1, markersize='4')
ylabel(r"Phase of $Y$", size=16)
xlabel(r"$\omega$", size=16)
ii = where(abs(Y) > 1e-3)
plot(w[ii], angle(Y[ii]), 'ro', lw=2)
xlim([-xLim, xLim])
grid(True)
show()
