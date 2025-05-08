# Python Acoustic Echo Cancellation Library

![screenshot](https://github.com/Keyvanhardani/Python-Acoustic-Echo-Cancellation-Library/blob/main/logo.png?raw=true)


## Description
This project implements adaptive filter algorithms for **Acoustic Echo Cancellation (AEC)** and general audio processing. The library includes adaptive filtering algorithms such as:
- **LMS (Least Mean Squares)**
- **NLMS (Normalized LMS)**
- **RLS (Recursive Least Squares)**

These filters are crucial for applications in speech processing, **echo suppression**, and **noise reduction**. The adaptive nature of these algorithms allows them to adjust dynamically to incoming signals and reduce unwanted echoes in real-time.

### **What is Acoustic Echo Cancellation?**
Acoustic Echo Cancellation (AEC) is the process of removing the echo that occurs when a microphone picks up audio output from nearby speakers. AEC is commonly used in telecommunication systems, video conferencing, and other audio processing systems to improve clarity and prevent feedback loops.

## Features
- **LMS (Least Mean Squares):** A simple adaptive filter that adjusts coefficients based on the error between the desired and estimated signal.
- **NLMS (Normalized LMS):** An extension of LMS with normalized step size for greater stability and performance across varying signal strengths.
- **RLS (Recursive Least Squares):** A more sophisticated filter using an inverse correlation matrix for fast and precise adaptation.

## Installation
To use the library, clone the repository and install the necessary dependencies:

```bash
pip install numpy scipy matplotlib
```

## Usage
The library provides a set of filters that can be easily applied to audio data for Acoustic Echo Cancellation. Below are examples of how to use the filters:

LMS Filter Example:
```bash
from lms import lms_filter

desired_signal = np.random.randn(1000)  # Desired audio signal
reference_input = np.random.randn(1000)  # Reference signal (could be the echo)
filter_coeff = np.random.randn(10)  # Initial filter coefficients
step_sizes = [0.001, 0.01, 0.1, 1]  # Possible step sizes

f_adaptive, best_step_size = lms_filter(desired_signal, reference_input, filter_coeff, step_sizes)
```
NLMS Filter Example:
```bash
from nlms import nlms_filter

desired_signal = np.random.randn(1000)
reference_input = np.random.randn(1000)
filter_coeff = np.random.randn(10)  # Initial filter coefficients

f_adaptive, error = nlms_filter(desired_signal, reference_input, filter_coeff)

```
RLS Filter Example:
```bash
from rls import rls_filter

desired_signal = np.random.randn(1000)
reference_input = np.random.randn(1000)
filter_coeff = np.random.randn(10)  # Initial filter coefficients
reg_param = 0.1  # Regularization parameter

f_adaptive, error = rls_filter(desired_signal, reference_input, filter_coeff, reg_param)

```
Example: Applying LMS Filter to a WAV File for AEC
```bash
import scipy.io.wavfile as wav
from lms_filter import lms_filter_safe
import numpy as np

# Load audio file
fs, audio_data = wav.read('path_to_audio_file.wav')

# If stereo, convert to mono
if len(audio_data.shape) > 1:
    audio_data = np.mean(audio_data, axis=1)

# Apply LMS filter for Acoustic Echo Cancellation
filter_coeff = np.random.randn(10)
filtered_signal, best_step_size = lms_filter_safe(audio_data, audio_data, filter_coeff, [0.001, 0.01, 0.1])

# Normalize and save the filtered signal
wav.write('filtered_audio_file.wav', fs, np.int16(filtered_signal))

```
## Signal Visualization
Here’s how to visualize the original and filtered signal using matplotlib:

```bash
import matplotlib.pyplot as plt

# Plot the original and filtered signal
plt.figure(figsize=(10, 6))
plt.plot(audio_data, label='Original Signal')
plt.plot(filtered_signal, label='Filtered Signal', alpha=0.7)
plt.title('Original vs. Filtered Signal (AEC)')
plt.xlabel('Samples')
plt.ylabel('Amplitude')
plt.legend()
plt.show()



```bash
# Live‑AEC Demo
pip install sounddevice
python mic_demo.py
```
