__author__ = 'alexpashevich'

import numpy as np
import matplotlib.pyplot as plt
from linear_system import show_plot


def myConvolution1D(x, h):
    # function assumes that that len(h) < len(x)
    conv = []
    for k in range(len(x) + len(h) - 1):
        print k
        val = 0
        if k < len(h):
            for i in range(k + 1):
                val += x[i] * h[k - i]
        if k >= len(h) and k < len(x):
            for i in range(k - len(h) + 1, k + 1):
                val += x[i] * h[k - i]
        if k >= len(x):
            for i in range(k - len(h) + 1, len(x)):
                val += x[i] * h[k - i]
        conv.append(val)
    return conv


x = [1,0,2,3,2,1,-1,-2,-1,0,2,3,3,2,1,1]
h = [2,2,-1,-1,3]
conv = myConvolution1D(x, h)

# question 2.2
show_plot(range(len(x)), x, 'Input', 'k', 'x')
show_plot(range(len(h)), h, 'Kernel', 'k', 'h')
show_plot(range(len(conv)), conv, 'Convolution', 'k', 'x*h')