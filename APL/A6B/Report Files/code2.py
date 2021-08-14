#Q2
p1 = poly1d([1,0.05])
p2 = polymul([1,0.1,2.2525],[1,0,2.25])
H = sp.lti(list(p1),list(p2)) #X(s)
impulseResponsePlot(H,'x(t) Plot for decay = 0.05')