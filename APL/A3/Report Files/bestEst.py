JCol = []
for i in time:
    JCol = JCol + [sp.jn(2, i)]
M = c_[JCol, time]
solution = []
for i in data:
    solution = solution + [lg.lstsq(M, i)[0]]
solution = array(solution)
print('Best Estimate of A and B =')
print(solution)
