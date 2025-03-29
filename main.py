from signals import signal_generation as sg     # Generowanie sygnałów i szumów
from signals import signal_analysis as sa       # Analiza sygnałów
from operations import signal_operations as so  # Operacje na sygnałach
from file_io import file_handler as fh          # Zapis/odczyt plików
from visualization import plot                  # Generowanie wykresów
import numpy as np

# [0] Obsługa programu
def main():
    print("=== Cyfrowe Przetwarzanie Sygnałów ===")
    print("Witaj! Wybierz co chcesz zrealizować:")
    print("Aby prowadzić operacje na wybranych sygnałach, po wygenerowaniu zapisz je!:")
    print("[1] Generowanie sygnału")
    print("[2] Operacje na sygnałach (dodawanie, odejmowanie, mnożenie, dzielenie)")
    print("[3] Analiza sygnału (średnia, RMS, wariancja itp.)")
    print("[4] Wizualizacja sygnału (wykres, histogram)")
    print("[5] Zapis/Wczytanie sygnału do/z pliku")
    print("[0] Wyjście")

    while True:
        try:
            choice = int(input("Wybierz opcję (0-5): "))
        except ValueError:
            print("Błąd: Wprowadź poprawną liczbę!")
            continue

        if choice == 0:
            print("Dziękujemy za skorzystanie z programu!")
            break

        elif choice == 1:
            print("--- Generowanie Sygnału ---")
            print("[1] Szum o rozkładzie jednostajnym")
            print("[2] Szum gaussowski")
            print("[3] Sygnał sinusoidalny")
            print("[4] Sygnał sinusoidalny wyprostowany jednopołówkowo")
            print("[5] Sygnał sinusoidalny wyprostowany dwupołówkowo")
            print("[6] Sygnał prostokątny")
            print("[7] Sygnał prostokątny symetryczny")
            print("[8] Sygnał trójkątny")
            print("[9] Sygnał skokowy")
            print("[10] Impuls jednostkowy")
            print("[11] Szum impulsowy")
            signal_type = int(input("Wybierz typ sygnału (1-11): "))

            if signal_type == 1:
                A = float(input("Podaj amplitudę (A): "))
                t_start = float(input("Podaj czas początkowy (t1): "))
                duration = float(input("Podaj czas trwania (d): "))
                sr = int(input("Podaj częstotliwość próbkowania (Hz): "))
                t, signal = sg.generate_uniform_noise(A, t_start, duration, sr)
                print("Szum o rozkładzie jednostajnym wygenerowany.")

            elif signal_type == 2:
                A = float(input("Podaj amplitudę (A): "))
                t_start = float(input("Podaj czas początkowy (t1): "))
                duration = float(input("Podaj czas trwania (d): "))
                sr = int(input("Podaj częstotliwość próbkowania (Hz): "))
                t, signal = sg.generate_gaussian_noise(A, t_start, duration, sr)
                print("Szum gaussowski wygenerowany.")

            elif signal_type == 3:
                A = float(input("Podaj amplitudę (A): "))
                T = float(input("Podaj okres podstawowy (T): "))
                t_start = float(input("Podaj czas początkowy (t1): "))
                duration = float(input("Podaj czas trwania (d): "))
                sr = int(input("Podaj częstotliwość próbkowania (Hz): "))
                t, signal = sg.generate_sine_wave(A, T, t_start, duration, sr)
                print("Sygnał sinusoidalny wygenerowany.")

            elif signal_type == 4:
                A = float(input("Podaj amplitudę (A): "))
                T = float(input("Podaj okres podstawowy (T): "))
                t_start = float(input("Podaj czas początkowy (t1): "))
                duration = float(input("Podaj czas trwania (d): "))
                sr = int(input("Podaj częstotliwość próbkowania (Hz): "))
                t, signal = sg.generate_half_rectified_sine(A, T, t_start, duration, sr)
                print("Sygnał sinusoidalny wyprostowany jednopołówkowo wygenerowany.")

            elif signal_type == 5:
                A = float(input("Podaj amplitudę (A): "))
                T = float(input("Podaj okres podstawowy (T): "))
                t_start = float(input("Podaj czas początkowy (t1): "))
                duration = float(input("Podaj czas trwania (d): "))
                sr = int(input("Podaj częstotliwość próbkowania (Hz): "))
                t, signal = sg.generate_full_rectified_sine(A, T, t_start, duration, sr)
                print("Sygnał sinusoidalny wyprostowany dwupołówkowo wygenerowany.")

            elif signal_type == 6:
                A = float(input("Podaj amplitudę (A): "))
                T = float(input("Podaj okres podstawowy (T): "))
                kw = float(input("Podaj współczynnik wypełnienia (kw): "))
                t_start = float(input("Podaj czas początkowy (t1): "))
                duration = float(input("Podaj czas trwania (d): "))
                sr = int(input("Podaj częstotliwość próbkowania (Hz): "))
                t, signal = sg.generate_square_wave(A, T, kw, t_start, duration, sr)
                print("Sygnał prostokątny wygenerowany.")

            elif signal_type == 7:
                A = float(input("Podaj amplitudę (A): "))
                T = float(input("Podaj okres podstawowy (T): "))
                kw = float(input("Podaj współczynnik wypełnienia (kw): "))
                t_start = float(input("Podaj czas początkowy (t1): "))
                duration = float(input("Podaj czas trwania (d): "))
                sr = int(input("Podaj częstotliwość próbkowania (Hz): "))
                t, signal = sg.generate_symmetric_square_wave(A, T, kw, t_start, duration, sr)
                print("Sygnał prostokątny symetryczny wygenerowany.")

            elif signal_type == 8:
                A = float(input("Podaj amplitudę (A): "))
                T = float(input("Podaj okres podstawowy (T): "))
                kw = float(input("Podaj współczynnik wypełnienia (kw): "))
                t_start = float(input("Podaj czas początkowy (t1): "))
                duration = float(input("Podaj czas trwania (d): "))
                sr = int(input("Podaj częstotliwość próbkowania (Hz): "))
                t, signal = sg.generate_triangle_wave(A, T, kw, t_start, duration, sr)
                print("Sygnał trójkątny wygenerowany.")

            elif signal_type == 9:
                A = float(input("Podaj amplitudę (A): "))
                ts = float(input("Podaj moment skoku (ts): "))
                t_start = float(input("Podaj czas początkowy (t1): "))
                duration = float(input("Podaj czas trwania (d): "))
                sr = int(input("Podaj częstotliwość próbkowania (Hz): "))
                t, signal = sg.generate_step_signal(A, ts, t_start, duration, sr)
                print("Sygnał skokowy wygenerowany.")

            elif signal_type == 10:
                A = float(input("Podaj amplitudę (A): "))
                ns = float(input("Podaj numer próbki skoku amplitudy (ns): "))
                n1 = float(input("Podaj numer pierwszej próbki (n1): "))
                l = float(input("Podaj liczbę próbek skoku (l): "))
                sr = int(input("Podaj częstotliwość próbkowania (Hz): "))
                t, signal = sg.generate_unit_impulse(A, ns, n1, l, sr)
                print("Impuls jednostkowy wygenerowany.")

            elif signal_type == 11:
                A = float(input("Podaj amplitudę (A): "))
                p = float(input("Podaj prawdopodobieństwo (p): "))
                t_start = float(input("Podaj czas początkowy (t1): "))
                duration = float(input("Podaj czas trwania (d): "))
                sr = int(input("Podaj częstotliwość próbkowania (Hz): "))
                t, signal = sg.generate_impulse_noise(A, p, t_start, duration, sr)
                print("Szum impulsowy wygenerowany.")

            else:
                print("Błędna opcja!.")

        elif choice == 2:
            print("--- Operacje na Sygnałach ---")
            print("[1] Dodawanie sygnałów")
            print("[2] Odejmowanie sygnałów")
            print("[3] Mnożenie sygnałów")
            print("[4] Dzielenie sygnałów")
            operation = int(input("Wybierz operację: "))

            print("Najpierw wybierz pierwszy sygnał.")
            # Wczytanie sygnału z pliku
            file1 = input("Podaj nazwę pliku z sygnałem 1: ")
            sr1, signal1 = fh.load_from_binary(file1)

            print("Teraz wybierz drugi sygnał.")
            # Wczytanie sygnału z pliku
            file2 = input("Podaj nazwę pliku z sygnałem 2: ")
            sr2, signal2 = fh.load_from_binary(file2)

            if operation == 1:
                result = so.add_signals(signal1, signal2)
                print("Sygnały zostały dodane.")
            elif operation == 2:
                result = so.subtract_signals(signal1, signal2)
                print("Sygnały zostały odjęte.")
            elif operation == 3:
                result = so.multiply_signals(signal1, signal2)
                print("Sygnały zostały pomnożone.")
            elif operation == 4:
                result = so.divide_signals(signal1, signal2)
                print("Sygnały zostały podzielone.")
            else:
                print("Nieprawidłowy wybór operacji.")

        elif choice == 3:
            print("--- Analiza Sygnału ---")
            file_name = input("Podaj nazwę pliku z sygnałem: ")
            sr, signal = fh.load_from_binary(file_name)
            print(f"Średnia: {sa.calculate_mean(signal)}")
            print(f"Wartość RMS: {sa.calculate_rms(signal)}")
            print(f"Wariancja: {sa.calculate_variance(signal)}")
            print(f"Moc średnia: {sa.calculate_power(signal)}")

        elif choice == 4:
            print("--- Wizualizacja ---")
            file_name = input("Podaj nazwę pliku z sygnałem: ")
            sr, signal = fh.load_from_binary(file_name)
            plot.plot_signal(np.arange(len(signal)) / sr, signal, title="Wykres sygnału")
            plot.plot_histogram(signal, bins=10, title="Histogram sygnału")

        elif choice == 5:
            print("--- Zapis/Wczytanie Sygnału ---")
            action = input("[1] Zapis do pliku\n"
                           "[2] Wczytanie z pliku\n"
                           "Wybierz: ")

            if action == "1":
                file_name = input("Podaj nazwę pliku do zapisu: ")
                fh.save_to_binary(file_name, signal)
                print(f"Sygnał zapisano do pliku {file_name}.")

            elif action == "2":
                file_name = input("Podaj nazwę pliku do odczytu: ")
                sr, signal = fh.load_from_binary(file_name)
                print(f"Sygnał wczytano z pliku {file_name}.")

            else:
                print("Nieprawidłowy wybór.")

        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()
