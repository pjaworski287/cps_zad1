import numpy as np

### Wyliczenia parametrów sygnału ###

# Średnia wartość sygnału
def calculate_mean(signal):
    return np.mean(signal)

# Średnia bezwzględna wartość sygnału
def calculate_absolute_mean(signal):
    return np.mean(np.abs(signal))

# Wartość skuteczna sygnału
def calculate_rms(signal):
    return np.sqrt(np.mean(np.square(signal)))

# Wariancja sygnału
def calculate_variance(signal):
    return np.var(signal)

# Moc średnia sygnału
def calculate_power(signal):
    return np.mean(np.square(signal))

# Moc średnia dla sygnałów zespolonych
def calculate_complex_power(signal):
    return np.mean(np.abs(signal) ** 2)

# Przycięcie sygnału do najbliższej liczby pełnych okresów
def trim_to_full_periods(signal, sampling_rate, frequency):
    if frequency <= 0:
        raise ValueError("Częstotliwość musi być większa od zera.")
    period_samples = int(sampling_rate / frequency)     # Liczba próbek w jednym okresie
    total_periods = len(signal) // period_samples       # Liczba pełnych okresów
    return signal[:total_periods * period_samples]      # Przycięcie sygnału


