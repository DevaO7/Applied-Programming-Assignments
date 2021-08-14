plot(time, data[1], label=scl[0])  # Plot for first Column
plot(time, realV, label='True Value')  # PLotting the Exact Curve
# PLacing the error bars in the graph
errorbar(time[::5], data[1][::5], scl[0], fmt='ro', label='Error Bar')
xlabel('Time')  # X axis Label
ylabel('f(t)+Noise')  # Y axis Label
title('With ErrorBar')
legend()
show()
