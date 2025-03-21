from signals.signal_generation  import generate_sine_wave,  generate_uniform_noise
from signals.signal_analysis    import calculate_mean,      calculate_rms
from file_io.file_handler       import save_to_binary,      load_from_binary
from visualization.plot         import plot_signal,         plot_histogram

# Generowanie sygnału
t, sine_wave = generate_sine_wave(amplitude=5, frequency=1, t_start=0, duration=2)
t, noise = generate_uniform_noise(amplitude=2, t_start=0, duration=2)

# Analiza
mean_value = calculate_mean(sine_wave)
rms_value = calculate_rms(sine_wave)

# Wizualizacja
plot_signal(t, sine_wave, title="Sine Wave")
plot_histogram(sine_wave, bins=10, title="Sine Wave Histogram")

# Zapis i odczyt
save_to_binary("sine_wave.bin", sine_wave)
sampling_rate, loaded_signal = load_from_binary("sine_wave.bin")

