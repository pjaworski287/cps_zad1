import matplotlib.pyplot as plt

def plot_signal(t, signal, title="Signal"):
    plt.figure()
    plt.plot(t, signal)
    plt.title(title)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.show()

def plot_histogram(signal, bins=10, title="Histogram"):
    plt.figure()
    plt.hist(signal, bins=bins)
    plt.title(title)
    plt.xlabel("Amplitude")
    plt.ylabel("Frequency")
    plt.grid()
    plt.show()
