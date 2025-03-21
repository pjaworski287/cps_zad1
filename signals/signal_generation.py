import numpy as np
from scipy import signal

# Generuje szum o rozkładzie jednostajnym w zadanym zakresie czasu
# Param: Amplituda szumu, Czas początkowy, Czas trwania, Częstotliwość próbkowania w Hz
# Return: Tablica czasu (wektor czasów próbkowania), Tablica wartości szumu (o losowych wartościach w zakresie amplitudy)
def generate_uniform_noise(amplitude, t_start, duration, sampling_rate=1000):
    t = np.linspace(t_start, t_start + duration, int(sampling_rate * duration))
    signal = np.random.uniform(-amplitude, amplitude, len(t))
    return t, signal

# Generowanie przebiegu sinusoidalnego o zadanej amplitudzie i częstotliwości.
# Param: Amplituda szumu, Częstotliwość sinusoidy, Czas początkowy, Czas trwania, Częstotliwość próbkowania w Hz
# Return: Tablica czasu (wektor czasów próbkowania), Tablica wartości szumu (o losowych wartościach w zakresie amplitudy)
def generate_sine_wave(amplitude, frequency, t_start, duration, sampling_rate=1000):
    t = np.linspace(t_start, t_start + duration, int(sampling_rate * duration))
    signal = amplitude * np.sin(2 * np.pi * frequency * t)
    return t, signal

# Generuje szum o rozkładzie normalnym (Gaussa) z zadanym poziomem amplitudy.
# Param: Amplituda szumu, Czas początkowy, Czas trwania, Częstotliwość próbkowania w Hz
# Return: Tablica czasu (wektor czasów próbkowania), Tablica wartości szumu (o losowych wartościach w zakresie amplitudy)
def generate_gaussian_noise(amplitude, t_start, duration, sampling_rate=1000):
    t = np.linspace(t_start, t_start + duration, int(sampling_rate * duration))
    signal = amplitude * np.random.normal(0, 1, len(t))  # Średnia = 0, odchylenie standardowe = 1
    return t, signal

# Generuje sygnał sinusoidalny wyprostowany jednopołówkowo.
# Param: Amplituda szumu, Częstotliwość sinusoidy, Czas początkowy, Czas trwania, Częstotliwość próbkowania w Hz
# Return: Tablica czasu (wektor czasów próbkowania), Tablica wartości szumu (o losowych wartościach w zakresie amplitudy)
def generate_half_rectified_sine(amplitude, frequency, t_start, duration, sampling_rate=1000):
    t = np.linspace(t_start, t_start + duration, int(sampling_rate * duration))
    signal = amplitude * np.sin(2 * np.pi * frequency * t)
    signal = np.maximum(signal, 0)  # Wyprostowanie jednopołówkowe
    return t, signal

# Generuje sygnał sinusoidalny wyprostowany dwupołówkowo.
# Param: Amplituda szumu, Częstotliwość sinusoidy, Czas początkowy, Czas trwania, Częstotliwość próbkowania w Hz
# Return: Tablica czasu (wektor czasów próbkowania), Tablica wartości szumu (o losowych wartościach w zakresie amplitudy)
def generate_full_rectified_sine(amplitude, frequency, t_start, duration, sampling_rate=1000):
    t = np.linspace(t_start, t_start + duration, int(sampling_rate * duration))
    signal = amplitude * np.abs(np.sin(2 * np.pi * frequency * t))  # Wyprostowanie dwupołówkowe
    return t, signal

# Generuje przebieg prostokątny o zadanej częstotliwości i współczynniku wypełnienia.
# Param: Amplituda szumu, Częstotliwość sinusoidy, Współczynnik wypełnienia, Czas początkowy, Czas trwania, Częstotliwość próbkowania w Hz
# Return: Tablica czasu (wektor czasów próbkowania), Tablica wartości szumu (o losowych wartościach w zakresie amplitudy)
def generate_square_wave(amplitude, frequency, duty_cycle, t_start, duration, sampling_rate=1000):
    t = np.linspace(t_start, t_start + duration, int(sampling_rate * duration))
    signal = amplitude * (signal.square(2 * np.pi * frequency * t, duty_cycle))
    return t, signal

# Generuje przebieg trójkątny o zadanej amplitudzie i częstotliwości.
# Param: Amplituda szumu, Częstotliwość sinusoidy, Czas początkowy, Czas trwania, Częstotliwość próbkowania w Hz
# Return: Tablica czasu (wektor czasów próbkowania), Tablica wartości szumu (o losowych wartościach w zakresie amplitudy)
def generate_triangle_wave(amplitude, frequency, t_start, duration, sampling_rate=1000):
    t = np.linspace(t_start, t_start + duration, int(sampling_rate * duration))
    signal = amplitude * signal.sawtooth(2 * np.pi * frequency * t, 0.5)  # Współczynnik wypełnienia = 0.5
    return t, signal

# Generuje sygnał skokowy (ang. step signal).
# Param: Amplituda szumu, Czas początkowy, Czas wystąpienia skoku, Czas trwania, Częstotliwość próbkowania w Hz
# Return: Tablica czasu (wektor czasów próbkowania), Tablica wartości szumu (o losowych wartościach w zakresie amplitudy)
def generate_step_signal(amplitude, t_start, step_time, duration, sampling_rate=1000):
    t = np.linspace(t_start, t_start + duration, int(sampling_rate * duration))
    signal = np.zeros(len(t))
    signal[t >= step_time] = amplitude
    return t, signal

# Generuje sygnał impulsowy (pojedynczy impuls w określonym czasie).
# Param: Amplituda szumu, Moment wystąpienia impulsu, Czas trwania, Częstotliwość próbkowania w Hz
# Return: Tablica czasu (wektor czasów próbkowania), Tablica wartości szumu (o losowych wartościach w zakresie amplitudy)
def generate_impulse_signal(amplitude, impulse_time, duration, sampling_rate=1000):
    t = np.linspace(0, duration, int(sampling_rate * duration))
    signal = np.zeros(len(t))
    idx = int(impulse_time * sampling_rate)
    signal[idx] = amplitude
    return t, signal

# Generuje sygnał szumu impulsowego o zadanej amplitudzie i prawdopodobieństwie impulsów.
# Param: Amplituda szumu, Prawdopodobieństwo wystąpienia impulsu w danej próbce, Czas początkowy sygnału, Czas trwania, Częstotliwość próbkowania w Hz
# Return: Tablica czasu (wektor czasów próbkowania), Tablica wartości szumu (o losowych wartościach w zakresie amplitudy)
def generate_impulse_noise(amplitude, probability, t_start, duration, sampling_rate=1000):
    t = np.linspace(t_start, t_start + duration, int(sampling_rate * duration))
    signal = amplitude * (np.random.rand(len(t)) < probability).astype(float)  # Impulsy z prawdopodobieństwem
    return t, signal
