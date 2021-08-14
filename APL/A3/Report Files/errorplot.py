error = []
for i in solution[:-1]:
    error = error + [array([(i[0]-1.05)**2, (i[1]+0.105)**2])]
error = array(error)
if '10' in reqPlots:
    plot(scl, error[:, 0], 'o', linestyle='dashed', label='A')
    plot(scl, error[:, 1], 'o', linestyle='dashed', label='B')
    xlabel('Noise Standard Deviation')
    ylabel('Error')
    legend()
    title('Variation of Error With Noise')
    show()
