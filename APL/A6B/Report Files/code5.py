#Q5
R = 100
L = 1e-6
C = 1e-6
H = sp.lti([1],[L*C,C*R,1]) # Transfer Function of the Two Port Network
w,S,phi = H.bode() # Computes the Value of Mag and phase
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