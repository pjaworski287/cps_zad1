from signals import signal_generation as sg     # Generowanie sygnałów i szumów
from signals import signal_analysis as sa       # Analiza sygnałów
from operations import signal_operations as so  # Operacje na sygnałach
from file_io import file_handler as fh          # Zapis/odczyt plików
from visualization import plot                  # Generowanie wykresów
import os

# Struktura przechowywania sygnałów
signals = {}  # Klucz: nazwa sygnału, wartość: (t, signal)

# Menu główne programu
def display_menu():
    print("\n=== Cyfrowe Przetwarzanie Sygnałów ===")
    print("[1] Generowanie sygnału")
    print("[2] Operacje na sygnałach")
    print("[3] Analiza sygnału")
    print("[4] Wizualizacja sygnału")
    print("[5] Zapis/Wczytanie sygnału z pliku")
    print("[6] Wyświetl zapisane sygnały na liście programu")
    print("[7] Usuń sygnał z zapisanej listy programu")
    print("[0] Wyjście")

# [1] Menu generowania sygnałów
def generate_signal():
    print("--- Generowanie Sygnału ---")
    print("[1] Szum jednostajny")
    print("[2] Szum gaussowski")
    print("[3] Sygnał sinusoidalny")
    print("[4] Sygnał sinusoidalny wyprostowany jednopołówkowo")
    print("[5] Sygnał sinusoidalny wyprostowany dwupołówkowo")
    print("[6] Sygnał prostokątny")
    print("[7] Sygnał prostokątny symetryczny")
    print("[8] Sygnał trójkątny")
    print("[9] Skok jednostkowy")
    print("[10] Impuls jednostkowy")
    print("[11] Szum impulsowy")
    print("[0] Anuluj")
    choice = int(input("Wybierz typ sygnału (1-11): "))

    if choice == 0 or choice > 11:
        print("Anulowanie.")
        return

    # Podstawowe parametry do generowanych sygnałów
    A =         float(  input("Podaj amplitudę (A): "))                     # AMPLITUDA (A)
    t_start =   float(  input("Podaj czas początkowy (t1): "))              # CZAS POCZĄTKOWY (t1)
    duration =  float(  input("Podaj czas trwania (d): "))                  # CZAS TRWANIA (d)
    sr =        int(    input("Podaj częstotliwość próbkowania (Hz): "))    # CZĘSTOTLIWOŚĆ PRÓBKOWANIA (Hz)

    if choice == 1:
        t, signal = sg.generate_uniform_noise(A, t_start, duration, sr)
    elif choice == 2:
        t, signal = sg.generate_gaussian_noise(A, t_start, duration, sr)
    elif choice == 3:
        period = float(input("Podaj okres podstawowy (T): "))               # OKRES PODSTAWOWY (T)
        t, signal = sg.generate_sine_wave(A, period, t_start, duration, sr)
    elif choice == 4:
        period = float(input("Podaj okres podstawowy (T): "))               # OKRES PODSTAWOWY (T)
        t, signal = sg.generate_half_rectified_sine_wave(A, period, t_start, duration, sr)
    elif choice == 5:
        period = float(input("Podaj okres podstawowy (T): "))               # OKRES PODSTAWOWY (T)
        t, signal = sg.generate_full_rectified_sine_wave(A, period, t_start, duration, sr)
    elif choice == 6:
        period = float(input("Podaj okres podstawowy (T): "))               # OKRES PODSTAWOWY (T)
        kw = float(input("Podaj współczynnik wypełnienia (kw): "))          # WSPÓŁCZYNNIK WYPEŁNIENIA (kw)
        t, signal = sg.generate_square_wave(A, period, kw, t_start, duration, sr)
    elif choice == 7:
        period = float(input("Podaj okres podstawowy (T): "))               # OKRES PODSTAWOWY (T)
        kw = float(input("Podaj współczynnik wypełnienia (kw): "))          # WSPÓŁCZYNNIK WYPEŁNIENIA (kw)
        t, signal = sg.generate_symmetric_square_wave(A, period, kw, t_start, duration, sr)
    elif choice == 8:
        period = float(input("Podaj okres podstawowy (T): "))               # OKRES PODSTAWOWY (T)
        kw = float(input("Podaj współczynnik wypełnienia (kw): "))          # WSPÓŁCZYNNIK WYPEŁNIENIA (kw)
        t, signal = sg.generate_triangle_wave(A, period, kw, t_start, duration, sr)
    elif choice == 9:
        step_time = float(input("Podaj moment skoku (ts): "))               # MOMENT SKOKU (ts)
        t, signal = sg.generate_step_signal(A, step_time, t_start, duration, sr)
    elif choice == 10:
        ns = int(input("Podaj numer próbki skoku (ns): "))                  # NUMER PRÓBKI SKOKU (ns)
        n1 = int(input("Podaj numer pierwszej próbki (n1): "))              # NUMER PIERWSZEJ PRÓBKI (n1)
        l = int(input("Podaj liczbę próbek (l): "))                         # LICZBA PRÓBEK (l)
        t, signal = sg.generate_unit_impulse(A, ns, n1, l, sr)
    elif choice == 11:
        probability = float(input("Podaj prawdopodobieństwo impulsu (p): "))    # PRAWDOPODOBIEŃSTWO IMPULSU (p)
        t, signal = sg.generate_impulse_noise(A, probability, t_start, duration, sr)
    else:
        print("Niepoprawny wybór.")
        return

    signal_name = input("Podaj nazwę dla wygenerowanego sygnału: ")
    signals[signal_name] = (t, signal)
    print(f"Sygnał '{signal_name}' został zapisany na liście.")

# [2] Operacje na sygnałach
def perform_operation():
    show_signals()
    if not signals:
        return

    s1 = input("Podaj nazwę pierwszego sygnału: ")
    s2 = input("Podaj nazwę drugiego sygnału: ")

    if s1 in signals and s2 in signals:
        t1, signal1 = signals[s1]
        t2, signal2 = signals[s2]

        print("[1] Dodawanie\n[2] Odejmowanie\n[3] Mnożenie\n[4] Dzielenie")
        operation = int(input("Wybierz operację: "))

        if len(signal1) != len(signal2):
            min_length = min(len(signal1), len(signal2))
            signal1, signal2 = signal1[:min_length], signal2[:min_length]
            t1 = t1[:min_length]

        if operation == 1:
            result = so.add_signals(signal1, signal2)
        elif operation == 2:
            result = so.subtract_signals(signal1, signal2)
        elif operation == 3:
            result = so.multiply_signals(signal1, signal2)
        elif operation == 4:
            result = so.divide_signals(signal1, signal2)
        else:
            print("Niepoprawna operacja.")
            return

        result_name = input("Podaj nazwę dla wynikowego sygnału: ")
        signals[result_name] = (t1, result)
        print(f"Sygnał '{result_name}' zapisany.")

# [3] Analizowanie wybranego sygnału
def analyze_signal():
    show_signals()
    if not signals:
        return

    name = input("Podaj nazwę sygnału do analizy: ")
    if name in signals:
        t, signal = signals[name]
        print(f"Średnia: {sa.calculate_mean(signal)}")          # Średnia sygnału
        print(f"Wartość RMS: {sa.calculate_rms(signal)}")       # Wartość RMS
        print(f"Wariancja: {sa.calculate_variance(signal)}")    # Wariancja
        print(f"Moc średnia: {sa.calculate_power(signal)}")     # Moc średnia
    else:
        print("Niepoprawna nazwa sygnału.")

# [4] Wizualizacja sygnału
def visualize_signal():
    show_signals()
    if not signals:
        return

    name = input("Podaj nazwę sygnału do wizualizacji: ")
    if name in signals:
        t, signal = signals[name]
        plot.plot_signal(t, signal, title=f"Sygnał: {name}")

        bins = int(input("Podaj liczbę przedziałów histogramu (np. 10): "))
        plot.plot_histogram(signal, bins=bins, title=f"Histogram: {name}")
    else:
        print("Niepoprawna nazwa sygnału.")

# [5] Zapis/Wczytanie sygnału z/do pliku
def save_load_signal():
    print("--- Zapis/Wczytanie Sygnału ---")
    action = input("[1] Zapis do pliku\n[2] Wczytanie z pliku\nWybierz: ")

    if action == "1":
        if not signals:
            print("Brak zapisanych sygnałów. Nie można nic zapisać.")
            return

        show_signals()
        name = input("Podaj nazwę sygnału do zapisu: ")
        if name in signals:
            file_name = input("Podaj nazwę pliku: ")
            sampling_rate = float(input("Podaj częstotliwość próbkowania (Hz): "))
            t, signal = signals[name]

            fh.save_to_binary(file_name, t, signal, sampling_rate)
            print(f"Sygnał '{name}' zapisano do pliku {file_name} z częstotliwością {sampling_rate} Hz.")
        else:
            print("Niepoprawna nazwa sygnału.")

    elif action == "2":
        file_name = input("Podaj nazwę pliku do odczytu: ")

        # Sprawdzenie, czy plik istnieje w katalogu z `main.py`
        if not os.path.isfile(file_name):
            print(f"Błąd: Plik '{file_name}' nie istnieje w bieżącym katalogu!")
            return

        t, signal, sampling_rate, is_complex, is_result = fh.load_from_binary(file_name)

        name = input("Podaj nazwę dla wczytanego sygnału: ")
        signals[name] = (t, signal)
        print(f"Sygnał '{name}' został dodany do listy (próbkowanie: {sampling_rate} Hz).")

# [6] Pokazanie sygnałów zapisanych na liście
def show_signals():
    if signals:
        print("Zapisane sygnały:")
        for name in signals.keys():
            print(f"- {name}")
    else:
        print("Brak zapisanych sygnałów.")

# [7] Usuwanie sygnałów zapisanych na liście
def delete_signal():
    if not signals:
        print("Brak zapisanych sygnałów. Nie można nic usunąć.")
        return

    show_signals()
    name = input("Podaj nazwę sygnału do usunięcia: ")

    if name in signals:
        del signals[name]
        print(f"Sygnał '{name}' został usunięty.")
    else:
        print("Niepoprawna nazwa sygnału.")

# PROGRAM
def main():
    while True:
        display_menu()
        choice = int(input("Wybierz opcję: "))

        if choice == 0:
            print("Do widzenia!")
            break
        elif choice == 1:
            generate_signal()
        elif choice == 2:
            perform_operation()
        elif choice == 3:
            analyze_signal()
        elif choice == 4:
            visualize_signal()
        elif choice == 5:
            save_load_signal()
        elif choice == 6:
            show_signals()
        elif choice == 7:
            delete_signal()
        else:
            print("Niepoprawny wybór.")

if __name__ == "__main__":
    main()
