def genCoeffbyLstsq(func):
    x = linspace(0, 2*m.pi, 401)
    x = x[:-1]  # drop last term to have a proper periodic integral
    A = np.zeros((400, 51))  # allocate space for A
    if func == 1:
        b = vecExp(x)
    if func == 2:
        b = vecCoscos(x)
    A[:, 0] = 1  # col 1 is all ones
    for k in range(1, 26):
        A[:, k] = np.cos(k*x)  # cos(kx) column
        A[:, k+25] = np.sin(k*x)  # sin(kx) column
    c1 = sp.linalg.lstsq(A, b)[0]  # Coeffiecents obtained from Lst Sq
    a1 = c1[:26]
    b1 = c1[26:]
    b2 = []
    a2 = []
    for i in a1:
        a2 = a2+[abs(i)]
    for i in b1:
        b2 = b2+[abs(i)]
    return a1, b1, a2, b2, c1, A
    # a1,b1 - Coeffiecnts
    # a2,b2 - Absolute value of coeffiecnts
    # c1 - [a0 ... a26 b1 .... b25]
    # A is the M matrix
