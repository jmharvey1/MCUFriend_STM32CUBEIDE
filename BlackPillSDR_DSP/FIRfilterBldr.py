#Below code is based on example code found Here:
#https://pysdr.org/content/filters.html

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import math


cut_off = 500 # Hz
width = 2000 #Hz
sample_rate = 48840 #48950 #97700 # Hz
#deicmate_taps_length: how many FIR filter taps we need to reach a given transition BW (should be odd, thus the |1)
#    const int decimate_taps_length = (int)(4.0f/(decimate_transition_bw/samp_rate)) | 1; 
num_taps =  (int)(4.0/(width/sample_rate)) #97 # it helps to use an odd number of taps
print("Tap Count: %4d" % num_taps)
# create our low pass filter
h = signal.firwin(num_taps, cut_off, width, window='hamming', fs=sample_rate)

# Shift the filter in frequency by multiplying by exp(j*2*pi*f0*t)
f0 = 750 #0.1##(2000)/2 ##10e3 # amount we will shift
Ts = 1.0/sample_rate # sample period
t = np.arange(0.0, Ts*len(h), Ts) # time vector. args are (start, stop, step)
exponential = np.exp(2j*np.pi*(+f0)*t) # this is essentially a complex sine wave

h_band_pass = h * exponential # do the shift
# Print coefficients in C++ format to be copyable to "filter.h" file
for i in range(0, len(h_band_pass),1):
    print("{%s, %s}," % (h_band_pass[i].real, h_band_pass[i].imag))
    
# plot impulse response
plt.subplot(121)
plt.plot(np.real(h_band_pass), '.-')
plt.plot(np.imag(h_band_pass), '.-')
plt.legend(['real', 'imag'], loc=1)

# plot the frequency response
H = np.abs(np.fft.fft(h_band_pass, 1024)) # take the 1024-point FFT and magnitude
H = np.fft.fftshift(H) # make 0 Hz in the center
# convert FFT mag to db gain
for i in range(0, len(H),1):
    H[i] =  20*math.log(H[i], 10)
    
w = np.linspace(-sample_rate/2, sample_rate/2, len(H)) # x axis
FrqRspns = plt.subplot(122)
#FrqRspns.plot(w, H, linewidth=2.0)
#FrqRspns.set(xlim=(-6000, 6000), xticks=np.arange(-6000, 6000, 1000),
#       ylim=(-120, 10), yticks=np.arange(-120, 10, 10))
#FrqRspns.autoscale(enable=True, axis='both', tight=None)
#FrqRspns.axvspan(+0, +1500, ymin=0, ymax=1, ls = '--', fill =False)

plt.plot(w, H, '.-')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Gain [Db]')
plt.show()
