from numpy import arange, arctan2, array, c_, cos, pi, sin, sqrt
from numpy.lib.arraysetops import intersect1d
from numpy.lib.function_base import angle, meshgrid
from numpy.lib.shape_base import array_split
from numpy.ma.core import where
from pylab import *
from scipy.linalg import lstsq
import mpl_toolkits.mplot3d.axes3d as p3


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
spectrum(y, 4, True, True, 4,  'With Hamming Window')
y = cos(0.86*t)**3
spectrum(y, 4, False, True, 4, 'Without Hamming Window')
spectrum(y, 4, True, True, 4,  'With Hamming Window')


def estimate(y):
    N = len(y)
    vec = y.copy()
    y = fftshift(y)
    t = linspace(-N * pi / 64, N * pi / 64, N + 1)
    t = t[:-1]
    dt = t[1] - t[0]
    fmax = 1 / dt
    y[0] = 0
    Y = fftshift(fft(fftshift(y))) / float(N)
    w = linspace(-pi * fmax, pi * fmax, N + 1)
    w = w[:-1]
    i = intersect1d(where(w >= 0), where(abs(Y) > 0.1))
    freq = sum(w[i] * abs(Y[i]**2)) / sum(abs(Y[i]**2))
    A, B = lstsq(c_[cos(freq * t), sin(freq * t)], vec)[0]
    delta = arctan2(-B, A)
    while delta < 0:
        delta += pi
    while delta > pi:
        delta -= pi
    return freq, delta


t = linspace(-2 * pi, 2 * pi, 129)
t = t[:-1]
print('Estimate without Noise ', end='')
print(estimate(cos(1.2*t+1)))
print('Estimate with added Noise ', end='')
print(estimate(0.1*rand(128)+cos(1.2*t+1)))
t = linspace(-pi, pi, 1025)
t = t[:-1]
y = cos(24 * t + 8 * t * t / pi)
spectrum(y, 1, False, True, 32, None)
dt = t[1] - t[0]
fmax = 1 / dt
w = linspace(0, pi * fmax, 9)[:-1]
Y, X = meshgrid(w, linspace(-pi, pi, 65)[:-1])

Freq = []
for x in array_split(t, 64):
    y = cos(24 * x + 8 * x * x / pi)
    Freq = Freq + [spectrum(y, 1, False, False, None, None)]

Freq = array(Freq)
ax = p3.Axes3D(figure(4))
surf = ax.plot_surface(Y, X, abs(Freq), rstride=1, cstride=1,
                       cmap=cm.jet, linewidth=0, antialiased=True)
show()
