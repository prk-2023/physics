import matplotlib.pyplot as plt
import numpy as np

def draw_wave(amplitude, frequency, phase, time_range):
    # Generate time array
    t = np.linspace(time_range[0], time_range[1], 1000)

    # Calculate wave values
    wave = amplitude * np.sin(2 * np.pi * frequency * t + phase)

    # Create plot
    plt.plot(t, wave)
    plt.xlabel('Time (s)')
    plt.ylabel('E Amplitude')
    plt.zlabel('B Amplitude')
    plt.title('Wave')
    plt.grid(True)
    plt.show()

# Example usage:
amplitude = 1  # Maximum amplitude of the wave
frequency = 1  # Frequency of the wave (Hz)
phase = 1.0  # Phase of the wave (radians)
time_range = (-1, 1)  # Time range to plot the wave (s)

draw_wave(amplitude, frequency, phase, time_range)


'''
Draw sin wave  with specific amplitude, frequency and phase over the given time range.
To Draw a graph we generate points and plot the curve.

 - t = np.linspace(time_range[0], time_range[1], 1000)
    generates an array of 1000 evenly spaced values over the specified time range.

    np.linspace: is numpy fun to generate a sequence of evenly spaced values.
    time_range[0]: starting value of time range
    time_range[1]: ending value of time range
    1000: number of values to generate in the sequence
    
    resulting value is of shape (1000, ) containing 1000 evenly spaced values.
    between time_range[0] and time_range[1]

- np.sin(2 * np.pi * frequency * t + phase)
    numpy func to Calculate the sine of an array of values.

    2 * np.pi: angular frequency ( in radians/sec )
    frequency : in Hz
    t: array of values that are generated above
    * : element-wise multiplication operator ( freq and time arrays element-wise )
    phase: phase argument to the sine function
'''
