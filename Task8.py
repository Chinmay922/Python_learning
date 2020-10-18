# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 03:53:09 2020

@author: crath
"""

from matplotlib import pyplot as plt
import numpy as np 
from scipy import fftpack

#Frequency in terms of Hertz
fre  = 5 
#Sample rate
fre_samp = 50
t = np.linspace(0, 2, 2 * fre_samp, endpoint = False )
a = np.sin(fre  * 2 * np.pi * t)
figure, axis = plt.subplots()
axis.plot(t, a)
plt.title('Without DFT')
axis.set_xlabel ('Time (s)')
axis.set_ylabel ('Signal amplitude')
plt.show()

aa = fftpack.fft(a)
fft = fftpack.fftfreq(len(a)) * fre_samp

figure, axis = plt.subplots()
axis.plot(fft, np.abs(aa))
plt.title('Applied DFT')
axis.set_xlabel ('Frequency (HZ)')
axis.set_ylabel ('Frequency Magnitude')
plt.show()


