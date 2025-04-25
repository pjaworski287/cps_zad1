import numpy as np

# Zapis do pliku
def save_to_binary(file_name, t, signal, sampling_rate, is_complex=False, is_result=False):
    t_start = t[0] if len(t) > 0 else 0         # Czas początkowy
    length = len(signal)                        # Liczba próbek
    type_flag = 1 if is_complex else 0          # 0 - rzeczywisty,  1 - zespolony
    result_flag = 1 if is_result else 0         # 0 - oryginalny,   1 - wynik operacji

    with open(file_name, "wb") as f:
        np.array([t_start],         dtype=np.float64).tofile(f)
        np.array([sampling_rate],   dtype=np.float64).tofile(f)
        np.array([length],          dtype=np.int32).tofile(f)
        np.array([type_flag],       dtype=np.int32).tofile(f)   # Informacja o typie sygnału
        np.array([result_flag],     dtype=np.int32).tofile(f)   # Informacja o pochodzeniu sygnału

        if is_complex:
            signal_real = np.real(signal).astype(np.float64)
            signal_imag = np.imag(signal).astype(np.float64)
            signal_real.tofile(f)
            signal_imag.tofile(f)
        else:
            signal.astype(np.float64).tofile(f)

    print(f"Sygnał zapisano do pliku {file_name}.")

# Odczyt z pliku
def load_from_binary(file_name):
    with open(file_name, "rb") as f:
        t_start =       np.fromfile(f, dtype=np.float64,    count=1)[0]
        sampling_rate = np.fromfile(f, dtype=np.float64,    count=1)[0]
        length =        np.fromfile(f, dtype=np.int32,      count=1)[0]
        type_flag =     np.fromfile(f, dtype=np.int32,      count=1)[0]
        result_flag =   np.fromfile(f, dtype=np.int32,      count=1)[0]

        is_complex = type_flag == 1
        is_result = result_flag == 1

        if is_complex:
            signal_real = np.fromfile(f, dtype=np.float64, count=length)
            signal_imag = np.fromfile(f, dtype=np.float64, count=length)
            signal = signal_real + 1j * signal_imag
        else:
            signal = np.fromfile(f, dtype=np.float64, count=length)

    t = np.linspace(t_start, t_start + (length - 1) / sampling_rate, length)

    print(f"Sygnał wczytano z pliku {file_name}.")
    return t, signal, sampling_rate, is_complex, is_result
