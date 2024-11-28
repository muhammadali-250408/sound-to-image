import numpy as np
from scipy.io.wavfile import read
def get_amplitude(file_name):
    # Load the audio file
    fs, amplitude = read(file_name)

    # Convert to mono if the audio is stereo
    if amplitude.ndim > 1:
        amplitude = amplitude.mean(axis=1)

    # Calculate the number of samples corresponding to 10 ms
    samples_per_10ms = int(fs * 0.01)

    # Collect amplitude values at every 10 ms
    amplitude_10ms = [str(int(amplitude[i])) for i in range(0, len(amplitude), samples_per_10ms)]

    # Print the resulting amplitude values every 10 ms
    print("Amplitude values every 10 ms:", amplitude_10ms)
    return amplitude_10ms
