'''
    Set up the environment in Python
    python -m venv speech_env
    source speech_env/bin/activate  # On Windows use `speech_env\Scripts\activate`
'''

import librosa
import os
import numpy as np
import matplotlib.pyplot as plt

# Path to the dataset directory
dataset_path = 'path_to_extracted_dataset'

# Load an audio file
file_path = os.path.join(dataset_path, 'yes/0a7c2a8d_nohash_0.wav')
audio, sample_rate = librosa.load(file_path, sr=None)

# Plot the waveform
plt.figure(figsize=(12, 4))
plt.plot(np.linspace(0, len(audio) / sample_rate, num=len(audio)), audio)
plt.title('Waveform')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()