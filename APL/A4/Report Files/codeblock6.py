deviaA = []
deviaB = []
print('Deviation in "a" Coeffecients,')
for i in range(26):
    print('a{} = {}'.format(i, abs(abs_aexp[i]-lst_abs_aexp[i])))
    deviaA = deviaA + [abs(abs_aexp[i]-lst_abs_aexp[i])]
print('Deviation in "b" Coeffecients,')
for i in range(25):
    print('b{} = {}'.format(i+1, abs(abs_bexp[i]-lst_abs_bexp[i])))
    deviaB = deviaB + [abs(abs_bexp[i]-lst_abs_bexp[i])]
print('Maximum Deviation = {}'.format(max([max(deviaA), max(deviaB)])))
