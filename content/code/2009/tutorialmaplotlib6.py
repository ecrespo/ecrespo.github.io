#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def f(t): return np.exp(-t) * np.cos(2*np.pi*t)*np.sqrt(np.sin(2*np.pi*t))

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)



plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
plt.title("Graficas")
plt.xlabel("tiempo (seg)")
plt.ylabel("funcion")
plt.subplot(212)
plt.plot(t2, np.sin(3*np.pi*t2), 'r--')
plt.xlabel("tiempo (seg)")
plt.ylabel("funcion")
plt.show()
