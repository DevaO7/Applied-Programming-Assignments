#Q3
H = sp.lti(1,[1,0,2.25]) #X(s)/F(s)
t = linspace(0,100,5001)
for f in arange(1.4,1.65,0.05):
    u = cos(f*t)*exp(-0.05*t)
    t,y,svec = sp.lsim(H,u,t) #y is the Output
    plt.plot(t,y)
plt.legend(['freq=1.4','freq=1.45','freq=1.5','freq=1.55','freq=1.6'])
plt.title('Output Responses for Input of different Frequencies')
plt.xlabel('Time')
plt.ylabel('Output')
plt.show()