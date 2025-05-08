import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
from lms import lms_filter  # Assuming lms_filter_safe is implemented in the lms module

def normalize_signal(signal):
    """
    Normalize the signal to the range of int16 values.
    Args:
    - signal: Input signal to normalize

    Returns:
    - normalized_signal: Signal normalized between -32768 and 32767 (int16 range)
    """
    # Remove NaN values and clip the signal to avoid overflow
    signal = np.nan_to_num(signal)
    max_val = np.max(np.abs(signal))
    
    # Normalize to int16 range if needed
    if max_val > 0:
        signal = signal / max_val * 32767

    return np.clip(signal, -32768, 32767).astype(np.int16)

def process_wav_file(input_wav_path, output_wav_path):
    """
    Process a WAV file for Acoustic Echo Cancellation using LMS filtering.
    
    Args:
    - input_wav_path: Path to the input WAV file
    - output_wav_path: Path to save the processed WAV file
    """
    # Load the WAV file
    fs, audio_data = audio_data.astype(np.float32)  # Int16 -> Float32 wav.read(input_wav_path)
    
    # If stereo, convert to mono by averaging the channels
    if len(audio_data.shape) > 1:
        audio_data = audio_data.astype(np.float32)  # Int16 -> Float32 np.mean(audio_data, axis=1)
    
    # Apply LMS filter for Acoustic Echo Cancellation
    filter_coeff = np.random.randn(10)  # Initial filter coefficients
    step_sizes = [0.001, 0.01, 0.1, 1]  # Possible step sizes
    
    filtered_signal, best_step_size = lms_filter_safe(audio_data, audio_data, filter_coeff, step_sizes)
    
    # Normalize the filtered signal
    normalized_filtered_signal = normalize_signal(filtered_signal)
    
    # Save the filtered and normalized signal as a new WAV file
    wav.write(output_wav_path, fs, normalized_filtered_signal)
    
    # Return the original and filtered signals for plotting
    return audio_data, normalized_filtered_signal, fs

def plot_signals(original_signal, filtered_signal, fs):
    """
    Plot the original and filtered signals for comparison.
    
    Args:
    - original_signal: The original audio signal
    - filtered_signal: The filtered audio signal
    - fs: Sample rate of the signals
    """
    plt.figure(figsize=(12, 6))
    plt.plot(original_signal, label='Original Signal')
    plt.plot(filtered_signal, label='Filtered Signal', alpha=0.7)
    plt.title('Original vs. Filtered Signal (Acoustic Echo Cancellation)')
    plt.xlabel('Samples')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # File paths
    input_wav_path = 'input_audio.wav'  # Path to the input WAV file
    output_wav_path = 'filtered_audio.wav'  # Path to save the filtered WAV file
    
    # Process the WAV file
    original_signal, filtered_signal, fs = process_wav_file(input_wav_path, output_wav_path)
    
    # Plot the signals for comparison
    plot_signals(original_signal, filtered_signal, fs)
    
    print(f'Filtered audio saved to {output_wav_path}')
