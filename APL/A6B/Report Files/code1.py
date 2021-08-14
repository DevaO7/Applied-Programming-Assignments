def impulseResponsePlot(H,title):
    t,x = sp.impulse(H,None,linspace(0,50,5001)) #Computes x(t)
    plt.plot(t,x)
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('x')
    plt.show()

#Q1
p1 = poly1d([1,0.5])
p2 = polymul([1,1,2.5],[1,0,2.25])
H = sp.lti(list(p1),list(p2)) # X(s)
impulseResponsePlot(H,'x(t) Plot for decay = 0.5')