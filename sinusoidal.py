import numpy as np

def SinusoidalModelGenerator(fs, amps, freqs, init_rad):
    theta = init_rad
    amps = iter(amps)
    freqs = iter(freqs)
    while True:
        amp = next(amps)
        freq = next(freqs)
        theta += (freq*1. / fs) * 2*np.pi
        yield amp * np.cos(theta) 

class SinusoidalModel(object):
    @staticmethod
    def gen_signal(fs, amps, freqs, init_rad=0.):
        taxis = np.arange(len(amps)) * 1. / fs
        values = np.zeros(len(amps))
        g = SinusoidalModelGenerator(fs=fs, amps=amps, freqs=freqs, init_rad=init_rad)
        for i in range(len(amps)):
            values[i] = next(g)

        return taxis, values
