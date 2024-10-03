import numpy as np

def lms_filter(desired_signal, reference_input, filter_coeff, step_sizes, num_iterations=1001):
    """
    LMS (Least Mean Squares) adaptive filter implementation.

    LMS (Least Mean Squares): Ein einfacher adaptiver Filter, der die Filterkoeffizienten auf Basis des Fehlers zwischen dem gewünschten und dem geschätzten Signal aktualisiert.
    
    Args:
    - desired_signal: Desired output signal (d)
    - reference_input: Input reference signal (u)
    - filter_coeff: Initial filter coefficients (f)
    - step_sizes: List of step sizes to evaluate
    - num_iterations: Number of iterations for adaptive filtering

    Returns:
    - f_adaptive: Adapted filter coefficients
    - best_step_size: Best step size with the least error
    """
    M = len(reference_input)
    e_final = float('inf')
    f_adaptive = filter_coeff
    best_step_size = step_sizes[0]

    for step_size in step_sizes:
        e = np.zeros(len(reference_input))
        f_adaptive_temp = np.zeros_like(filter_coeff)

        # Iterate through the signal and update filter
        for l in range(len(filter_coeff), M):
            u_block = reference_input[l:l - len(filter_coeff):-1]
            y = np.dot(f_adaptive_temp, u_block)
            e[l] = desired_signal[l] - y
            # Update filter coefficients
            f_adaptive_temp += step_size * e[l] * u_block

        # Calculate total error
        total_error = np.sum(np.abs(e)**2)
        if total_error < e_final:
            e_final = total_error
            f_adaptive = f_adaptive_temp
            best_step_size = step_size

    return f_adaptive, best_step_size

# Beispiel-Test: Zufallsdaten für den LMS-Filter
desired_signal = np.random.randn(1000)  # Beispiel: gewünschtes Signal
reference_input = np.random.randn(1000)  # Beispiel: Referenzeingang
filter_coeff = np.random.randn(10)  # Anfangswerte für Filterkoeffizienten
step_sizes = [0.001, 0.01, 0.1, 1]  # Verschiedene Schrittgrößen

# Aufruf der LMS-Funktion
f_adaptive, best_step_size = lms_filter(desired_signal, reference_input, filter_coeff, step_sizes)

f_adaptive, best_step_size
