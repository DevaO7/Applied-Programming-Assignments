def loglogPlotter(x1, a2, label1, color1, title1, xlabel1, ylabel1):
    loglog(x1, a2, 'r.', label=label1, color=color1)
    title(title1)
    xlabel(xlabel1)
    ylabel(ylabel1)
    legend()


def semilogyPlotter(x1, a2, label1, color1, title1, xlabel1, ylabel1):
    semilogy(x1, a2, 'r.', label=label1, color=color1)
    title(title1)
    xlabel(xlabel1)
    ylabel(ylabel1)
    legend()


# For exp()
x = np.arange(26)
loglogPlotter(x, abs_aexp, 'a', 'red',
              'Loglog plot of the Coeffecients for exp(x)', 'n', 'Mag of Coeffecient')
loglogPlotter(x[1:], abs_bexp, 'b', 'blue',
              'Loglog plot of the Coeffecients for exp(x)', 'n', 'Mag of Coeffecient')
show()
semilogyPlotter(x, abs_aexp, 'a', 'red',
                'Semilogy plot of the Coeffecients for exp(x)', 'n', 'Mag of Coeffecient')
semilogyPlotter(x[1:], abs_bexp, 'b', 'blue',
                'Semilogy plot of the Coeffecients for exp(x)', 'n', 'Mag of Coeffecient')
show()
# For coscos(x)
loglogPlotter(x, abs_acos, 'a', 'red',
              'Loglog plot of the Coeffecients for coscos(x)', 'n', 'Mag of Coeffecient')
loglogPlotter(x[1:], abs_bcos, 'b', 'blue',
              'Loglog plot of the Coeffecients for coscos(x)', 'n', 'Mag of Coeffecient')
show()
semilogyPlotter(x, abs_acos, 'a', 'red',
                'Semilogy plot of the Coeffecients for coscos(x)', 'n', 'Mag of Coeffecient')
semilogyPlotter(x[1:], abs_bcos, 'b', 'blue',
                'Semilogy plot of the Coeffecients for coscos(x)', 'n', 'Mag of Coeffecient')
show()
