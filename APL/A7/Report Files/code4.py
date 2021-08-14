# Q4
Vi1 = np.sin(1e3*pi*t)*np.exp(-1e2*t)  # Low Frequency Input signal
Vi2 = np.sin(1e6*pi*t)*np.exp(-1e4*t)  # High Frequency Input Signal
time, Vo1, svec = lsim(H, Vi1, t)  # Output to the Low Freq
time, Vo2, svec = lsim(H, Vi2, t)  # Output to the High Freq
plot(t, Vi1, label='Input Signal')
plot(time, Vo1, label='Filtered Signal')
xlabel('Time')
ylabel('Output/Input')
xlim(0, 1e-2)
legend()
show()
plot(t, Vi2, label='Input Signal')
plot(time, Vo2, label='Filtered Signal')
xlabel('Time')
ylabel('Output/Input')
legend()
xlim(0, 0.4*1e-4)
show()
