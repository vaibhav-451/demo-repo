import numpy as np
import matplotlib.pyplot as plt

def generate_exponential_signal(duration, decay_factor):
    time = np.linspace(0, duration, num=1000)
    amplitude = np.exp(-decay_factor * time)
    return time, amplitude

duration = 5  # Duration of the signal
decay_factor = 0.5  # Adjust this value to control the decay rate

time, amplitude = generate_exponential_signal(duration, decay_factor)

plt.plot(time, amplitude)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Exponential Signal with Decreasing Amplitude')
plt.grid(True)
plt.show()