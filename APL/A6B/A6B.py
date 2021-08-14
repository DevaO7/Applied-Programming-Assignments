from numpy import poly1d
from pylab import *
from numpy import *
import scipy.signal as sp
import matplotlib.pyplot as plt

def outputPlotter(H,u,t,title):
    t,y,svec = sp.lsim(H,u,t)
    plt.plot(t,y)
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Output')
    plt.show()

def impulseResponsePlot(H,title):
    t,x = sp.impulse(H,None,linspace(0,50,5001))
    plt.plot(t,x)
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('x')
    plt.show()

#Q1
p1 = poly1d([1,0.5])
p2 = polymul([1,1,2.5],[1,0,2.25])
H = sp.lti(list(p1),list(p2))
impulseResponsePlot(H,'x(t) Plot for decay = 0.5')

#Q2
p1 = poly1d([1,0.05])
p2 = polymul([1,0.1,2.2525],[1,0,2.25])
H = sp.lti(list(p1),list(p2))
impulseResponsePlot(H,'x(t) Plot for decay = 0.05')

#Q3
H = sp.lti(1,[1,0,2.25])
t = linspace(0,100,5001)
for f in arange(1.4,1.65,0.05):
    u = cos(f*t)*exp(-0.05*t)
    t,y,svec = sp.lsim(H,u,t)
    plt.plot(t,y)
plt.legend(['freq=1.4','freq=1.45','freq=1.5','freq=1.55','freq=1.6'])
plt.title('Output Responses for Input of different Frequencies')
plt.xlabel('Time')
plt.ylabel('Output')
plt.show()

#Q4
X = sp.lti([1,0,2],[1,0,3,0])
t,x = sp.impulse(X,None,linspace(0,20,5001))
plt.plot(t,x,label = 'x(t)')
Y = sp.lti(2,[1,0,3,0])
t,y = sp.impulse(Y,None,linspace(0,20,5001))
plt.plot(t,y,label = 'y(t)',color = 'y')
plt.legend()
plt.xlabel('Time')
plt.ylabel('x(t)/y(t)')
plt.title('Solution of the Coupled Spring Problem')
plt.show()

#Q5
R = 100
L = 1e-6
C = 1e-6
H = sp.lti([1],[L*C,C*R,1])
w,S,phi = H.bode()
plt.subplot(2,1,1)
plt.title('Bode Plot for the RLC series circuit')
plt.semilogx(w,S)
plt.xlabel('Frequency')
plt.ylabel('Magnitude in Db scale')
plt.subplot(2,1,2)
plt.semilogx(w,phi)
plt.xlabel('Frequency')
plt.ylabel('Phase')
plt.show()

#Q6
t = arange(0,3e-2,1e-7)
u = cos((1e3)*t)-cos((1e6)*t)
outputPlotter(H,u,t,'Output plot (Large time scale)')

t = arange(0,30e-6,1e-7)
u = cos((1e3)*t)-cos((1e6)*t)
outputPlotter(H,u,t,'Output Plot (Small time scale)')







