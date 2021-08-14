# Q2
vi = np.sin(2000*pi*t)+np.cos(2e6*pi*t)  # Given Input
time, Vo_HP, svec = lsim(H, vi, t)  # Vo_HP is the output (Filtered Output)
plot(t, vi, label='Input Signal')
plot(t, Vo_HP, label='Filtered Signal')
title('Output to the given Signal')
xlabel('Time')
ylabel('Output/Input')
legend()
xlim(0, 1e-3)
show()
