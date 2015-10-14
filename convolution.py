__author__ = 'alexpashevich'

from linear_system import show_arr


def myConvolution1D(x, h):
    # function assumes that that len(h) < len(x)
    conv = []
    for k in range(len(x) + len(h) - 1):
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

def myMovingAverage(x, M):
    if M % 2 == 0:
        print("Error, M is not odd!")
        return []
    y = []
    h = [1. / M] * M
    z = myConvolution1D(x, h)
    for i in range(len(z) - M + 1):
        y.append(z[i + (M - 1) / 2])
    return y

if __name__ == "__main__":
    x = [1,0,2,3,2,1,-1,-2,-1,0,2,3,3,2,1,1]
    h = [2,2,-1,-1,3]
    conv = myConvolution1D(x, h)


    # question 2.2
    show_arr(x, 'Input', 'k', 'x')
    show_arr(h, 'Kernel', 'k', 'h')
    show_arr(conv, 'Convolution', 'k', 'x*h')

    # question 2.5, 2.6 and 2.7 are in linear_system.py