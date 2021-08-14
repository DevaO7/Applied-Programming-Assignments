for i in time:
    realV = realV + [g(i, 1.05, -0.105)]
data = vstack((data, realV))
JCol = []
for i in time:
    JCol = JCol + [sp.jn(2, i)]
M = c_[JCol, time]  # M matrix is created
b = array([1.05, -0.105])  # A0 and B0
print('M = ', end='')
print(M)
print('b = ', end='')
print(b)
print("Sum of squared differences = ", end='')
# Computing the sum of square differences
Error = ((dot(M, b) - realV)**2).sum()
print(((dot(M, b) - realV)**2).sum())
if Error == 0:  # Verification
    print('Verified they are Equal')
