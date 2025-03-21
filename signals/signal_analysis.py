import numpy as np

def calculate_mean(signal):
    return np.mean(signal)

def calculate_rms(signal):
    return np.sqrt(np.mean(np.square(signal)))

def calculate_variance(signal):
    return np.var(signal)

def calculate_power(signal):
    return np.mean(np.square(signal))

def subtract_signals(signal1, signal2):
    return signal1 - signal2

def divide_signals(signal1, signal2):
    return np.divide(signal1, signal2, out=np.zeros_like(signal1), where=(signal2 != 0))

def calculate_absolute_mean(signal):
    return np.mean(np.abs(signal))

def trim_to_full_periods(signal, sampling_rate, frequency):
    period_samples = int(sampling_rate / frequency)  # Liczba próbek w jednym okresie
    total_periods = len(signal) // period_samples    # Liczba pełnych okresów
    return signal[:total_periods * period_samples]  # Przycięcie sygnału

def calculate_complex_power(signal):
    return np.mean(np.abs(signal) ** 2)  # Moc dla zespolonych
