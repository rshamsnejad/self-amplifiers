import numpy as np
import matplotlib.pyplot as plt

# Parameters for the sine wave
frequency = 1000  # 1 kHz frequency
duration = 1.0    # Duration in seconds
sampling_rate = 10000  # Sampling rate (44.1 kHz is standard for audio)

# Time array
t = np.linspace(0.0, duration, int(sampling_rate * duration), endpoint=False)

# Generate the sine wave
amplitude = 1  # Amplitude of the sine wave (0.5 for 0 to 1 range)
sine_wave = amplitude * np.sin(2 * np.pi * frequency * t)

# Compute the FFT (Fast Fourier Transform)
fft_output = np.fft.fft(sine_wave)
#fft_magnitude = fft_output
fft_magnitude = np.abs(fft_output) / len(t)

# Frequencies corresponding to the FFT output
frequencies = np.fft.fftfreq(len(fft_output), 1.0 / sampling_rate)

# Plot the time-domain sine wave
plt.subplot(2, 1, 1)
plt.plot(t, sine_wave)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('1 kHz Sine Wave')
plt.grid()

# Plot the frequency-domain FFT
plt.subplot(2, 1, 2)
plt.plot(frequencies, fft_magnitude)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('FFT of 1 kHz Sine Wave')
plt.grid()

plt.tight_layout()
plt.show()