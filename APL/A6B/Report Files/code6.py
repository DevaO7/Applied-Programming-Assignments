def outputPlotter(H,u,t,title):
    t,y,svec = sp.lsim(H,u,t)
    plt.plot(t,y)
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Output')
    plt.show()

#Q6
t = arange(0,3e-2,1e-7) #Large Time Scale
u = cos((1e3)*t)-cos((1e6)*t)
outputPlotter(H,u,t,'Output plot (Large time scale)')