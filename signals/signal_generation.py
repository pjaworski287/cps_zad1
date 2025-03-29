import numpy as np
from scipy import signal

# (S1) - Szum o rokzładzie jednostajnym
# param: (amplituda (A), czas poczatkowy (t1), czas trwania (d), częstotliwość próbkowania (sr))
def generate_uniform_noise(amplitude, t_start, duration, sampling_rate=1000):
    t = np.linspace(t_start, t_start + duration, int(sampling_rate * duration))
    signal = np.random.uniform(-amplitude, amplitude, len(t))
    return t, signal

# (S2) - Szum gaussowski
# param: (amplituda (A), czas poczatkowy (t1), czas trwania (d), częstotliwość próbkowania (sr))
def generate_gaussian_noise(amplitude, t_start, duration, sampling_rate=1000):
    t = np.linspace(t_start, t_start + duration, int(sampling_rate * duration))
    signal = amplitude * np.random.normal(0, 1, len(t))  # Średnia = 0, odchylenie standardowe = 1
    return t, signal

# (S3) - Sygnał sinusoidalny
# param: (amplituda (A), okres podstawowy (T), czas poczatkowy (t1), czas trwania (d), częstotliwość próbkowania (sr))
def generate_sine_wave(amplitude, period, t_start, duration, sampling_rate=1000):
    frequency = 1 / period  # f = 1/T
    t = np.linspace(t_start, t_start + duration, int(sampling_rate * duration))
    signal = amplitude * np.sin(2 * np.pi * frequency * t)
    return t, signal

# (S4) - Sygnał sinusoidalny (wyprostowany jednopołówkowo)
# param: (amplituda (A), okres podstawowy (T), czas poczatkowy (t1), czas trwania (d), częstotliwość próbkowania (sr))
def generate_half_rectified_sine_wave(amplitude, period, t_start, duration, sampling_rate=1000):
    frequency = 1 / period  # f = 1/T
    t = np.linspace(t_start, t_start + duration, int(sampling_rate * duration))
    signal = amplitude * np.sin(2 * np.pi * frequency * t)
    signal = np.maximum(signal, 0)  # Wyprostowanie jednopołówkowe
    return t, signal

# (S5) - Sygnał sinusoidalny (wyprostowany dwupołówkowo)
# param: (amplituda (A), okres podstawowy (T), czas poczatkowy (t1), czas trwania (d), częstotliwość próbkowania (sr))
def generate_full_rectified_sine_wave(amplitude, period, t_start, duration, sampling_rate=1000):
    frequency = 1 / period  # f = 1/T
    t = np.linspace(t_start, t_start + duration, int(sampling_rate * duration))
    signal = amplitude * np.abs(np.sin(2 * np.pi * frequency * t))  # Wyprostowanie dwupołówkowe
    return t, signal

# (S6) - Sygnał prostokątny
# param: (amplituda (A), okres podstawowy (T), współczynnik wypełnienia (kw), czas poczatkowy (t1), czas trwania (d), częstotliwość próbkowania (sr))
def generate_square_wave(amplitude, period, kw, t_start, duration, sampling_rate=1000):
    frequency = 1 / period  # f = 1/T
    t = np.linspace(t_start, t_start + duration, int(sampling_rate * duration), endpoint=False)
    sig = amplitude * signal.square(2 * np.pi * frequency * t, duty=kw)
    return t, sig

# (S7) - Sygnał prostokątny (symetryczny)
# param: (amplituda (A), okres podstawowy (T), współczynnik wypełnienia (kw), czas poczatkowy (t1), czas trwania (d), częstotliwość próbkowania (sr))
def generate_symmetric_square_wave(amplitude, period, kw, t_start, duration, sampling_rate=1000):
    frequency = 1 / period  # f = 1/T
    t = np.linspace(t_start, t_start + duration, int(sampling_rate * duration), endpoint=False)
    sig = amplitude * signal.square(2 * np.pi * frequency * t, duty=kw)
    sig = np.where(sig > 0, amplitude, -amplitude)          # Zmiana wartości 0 -> -amplitude dla sygnału symetrycznego
    return t, sig

# (S8) - Sygnał trójkątny
# param: (amplituda (A), okres podstawowy (T), współczynnik wypełnienia (kw), czas poczatkowy (t1), czas trwania (d), częstotliwość próbkowania (sr))
def generate_triangle_wave(amplitude, period, kw, t_start, duration, sampling_rate=1000):
    frequency = 1 / period  # f = 1/T
    t = np.linspace(t_start, t_start + duration, int(sampling_rate * duration), endpoint=False)
    sig = amplitude * signal.sawtooth(2 * np.pi * frequency * t, width=kw)
    return t, sig

# (S9) - Skok jednostkowy
# param: (amplituda (A), moment skoku (ts), czas poczatkowy (t1), czas trwania (d), częstotliwość próbkowania (sr))
def generate_step_signal(amplitude, step_time, t_start, duration, sampling_rate=1000):
    t = np.linspace(t_start, t_start + duration, int(sampling_rate * duration), endpoint=False)
    signal = np.where(t >= step_time, amplitude, 0)
    return t, signal

# (S10) - Impuls jednostkowy
# param: (amplituda (A), numer próbki skoku amplitudy (ns), numer pierwszej próbki (n1), liczba próbek (l), częstotliwość próbkowania (sr))
def generate_unit_impulse(amplitude, ns, n1, l, sampling_rate=1000):
    # Generowanie osi czasu (od n1 do n1+l-1, próbkowanie na podstawie f)
    t = np.arange(n1, n1 + l) / sampling_rate
    signal = np.zeros(l)
    if n1 <= ns < n1 + l:
        idx = ns - n1  # Pozycja próbki ns względem tablicy
        signal[idx] = amplitude
    return t, signal

# (S11) - Szum impulsowy
# param: (amplituda (A), prawdopodobieństwo impulsu (p), czas poczatkowy (t1), czas trwania (d), częstotliwość próbkowania (sr))
def generate_impulse_noise(amplitude, probability, t_start, duration, sampling_rate=1000):
    t = np.linspace(t_start, t_start + duration, int(sampling_rate * duration), endpoint=False)
    signal = amplitude * (np.random.rand(len(t)) < probability).astype(float)
    return t, signal