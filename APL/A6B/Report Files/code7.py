t = arange(0,30e-6,1e-7) #Large Time Scale
u = cos((1e3)*t)-cos((1e6)*t)
outputPlotter(H,u,t,'Output Plot (Small time scale)')