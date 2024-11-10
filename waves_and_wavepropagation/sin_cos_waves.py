import matplotlib.pyplot as plt
import numpy as np

# Define constants
amplitude_E = 1  # Maximum amplitude of the electric field
amplitude_B = 1  # Maximum amplitude of the magnetic field
frequency = 1  # Frequency of the wave (Hz)
phase_E = 0  # Phase of the electric field (radians)
phase_B = np.pi/2  # Phase of the magnetic field (radians)
time_range = (-1, 1)  # Time range to plot the wave (s)

# Generate time array
t = np.linspace(time_range[0], time_range[1], 1000)

# Calculate electric and magnetic field values
E = amplitude_E * np.sin(2 * np.pi * frequency * t + phase_E)
B = amplitude_B * np.sin(2 * np.pi * frequency * t + phase_B)

# Create plot
plt.figure(figsize=(10, 5))

# Plot electric field
plt.subplot(2, 1, 1)
plt.plot(t, E, label='Electric Field (E)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Electric and Magnetic Fields of an Electromagnetic Wave')
plt.legend()

# Plot magnetic field
plt.subplot(2, 1, 2)
plt.plot(t, B, label='Magnetic Field (B)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

# Layout so plots do not overlap
plt.tight_layout()

# Show plot
plt.show()
