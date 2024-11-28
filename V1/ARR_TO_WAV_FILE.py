from COMPRESSOR import compr_amp_arr
from scipy.io.wavfile import write
import numpy as np

# CONVERT ARRAY TO NP
amp_arr = np.array(compr_amp_arr)

# MAKE SURE IT IS WITHIN 16BIT
amp_arr = np.clip(amp_arr, -32768, 32767)  # Clip values to ensure they are within the 16-bit range
amp_arr = amp_arr.astype(np.int16)  # Convert to 16-bit signed integer type

# SAMPLE RATE
SAMPLERATE = 44100

# MAKE FILE
new_file = "new.wav"
write(new_file, SAMPLERATE, amp_arr)