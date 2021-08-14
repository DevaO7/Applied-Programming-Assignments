   for i in range(1, 10):  # Plotting the Data against time
        plot(time, data[i], label=scl[i-1])  # Plotted using matplotlib.pyplot
    # Plotting the Real Value, i.e without any noise
    plot(time, realV, 'black', label='True Value')
    xlabel('Time')  # X axis Label
    ylabel('f(t)+Noise')  # Y axis Label
    title('Plotting the Data')  # Z axis Label
    legend()
    show()
