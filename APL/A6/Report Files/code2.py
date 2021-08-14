for k in range(1, nk+1):
    ii = where(xx > 0)
    dx[ii] = u[ii]+0.5  # Displacement the electron travels
    xx[ii] = xx[ii] + dx[ii]  # Recording the New Positions
    u[ii] = u[ii]+1  # New Speed of the electron
    jj = where(xx >= n)
    xx[jj] = 0  # Ejecting the Electrons
    u[jj] = 0
    dx[jj] = 0
    kk = where(u >= u0)  # Finding Electrons that has sufficient Energy
    # Probability of That Collision Emitting Light
    ll = where(rand(len(kk[0])) <= p)
    kl = kk[0][ll]
    u[kl] = 0
    rho = rand(len(kl))
    xx[kl] = xx[kl]-dx[kl]*rho
    I.extend(xx[kl].tolist())  # Recording the Intensity
    m = int(rand()*Msig+M)
    empty = where(xx == 0)
    t = (min(len(empty), m))
    xx[empty[:t]] = 1
    u[empty[0][:t]] = 0
    dx[empty[0][:t]] = 0
    X.extend(xx.tolist())  # Recording the Electron Density
    V.extend(u.tolist())  # Velocity of Electrons
