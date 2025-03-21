import struct
import numpy as np

def save_to_binary(filename, data, sampling_rate=1000):
    with open(filename, 'wb') as f:
        # Zapisujemy częstotliwość próbkowania
        f.write(struct.pack('d', sampling_rate))
        # Zapisujemy dane sygnału
        for value in data:
            f.write(struct.pack('d', value))

def load_from_binary(filename):
    with open(filename, 'rb') as f:
        sampling_rate = struct.unpack('d', f.read(8))[0]
        signal = []
        while byte := f.read(8):
            signal.append(struct.unpack('d', byte)[0])
    return sampling_rate, np.array(signal)

def save_signal_to_binary(filename, signal, metadata):
    with open(filename, 'wb') as f:
        # Zapisujemy metadane
        for key, value in metadata.items():
            f.write(struct.pack('d', value))
        # Zapisujemy sygnał
        for value in signal:
            f.write(struct.pack('d', value))

def load_signal_from_binary(filename):
    with open(filename, 'rb') as f:
        metadata = {}
        # Przykładowy odczyt metadanych
        metadata['sampling_rate'] = struct.unpack('d', f.read(8))[0]
        # Odczyt sygnału
        signal = []
        while byte := f.read(8):
            signal.append(struct.unpack('d', byte)[0])
    return metadata, np.array(signal)

