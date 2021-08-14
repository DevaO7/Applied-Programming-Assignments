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
