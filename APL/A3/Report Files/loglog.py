error = []
for i in solution[:-1]:
    error = error + [array([(i[0]-1.05)**2, (i[1]+0.105)**2])]
error = array(error)
loglog(scl, error[:, 0], 'o', linestyle='dashed',
       label='Aerr', markersize='4')
loglog(scl, error[:, 1], 'o', linestyle='dashed',
       label='Berr', markersize='4')
xlabel('Noise Standard Deviation')
ylabel('Error')
legend()
title('loglog error vs stdev')
show()
