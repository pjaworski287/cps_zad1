import numpy as np

### Podstawowe działania na sygnałach ###

# (D1) - Dodawanie sygnałów do siebie
def add_signals(signal1, signal2):
    return signal1 + signal2

# (D2) - Odejmowanie sygnałów od siebie
def subtract_signals(signal1, signal2):
    return signal1 - signal2

# (D3) - Mnożenie sygnałów przez siebie
def multiply_signals(signal1, signal2):
    # Dopasowanie długości poprzez przycięcie do długości krótszego sygnału
    min_length = min(len(signal1), len(signal2))
    trimmed_signal1 = signal1[:min_length]
    trimmed_signal2 = signal2[:min_length]
    # Mnożenie sygnałów
    return trimmed_signal1 * trimmed_signal2


# (D4) - DZielenie sygnałów przez siebie
def divide_signals(signal1, signal2):
    return np.divide(signal1, signal2, out=np.zeros_like(signal1), where=(signal2 != 0))
