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
