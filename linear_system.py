__author__ = 'alexpashevich'

import numpy as np
import matplotlib.pyplot as plt


def create_x1(size):
    return [np.sin(2 * np.pi * k / 100) for k in range(size)]


def create_x2(size):
    return [4 * np.exp((-1. / 300) * (k - 150) ** 2) - np.exp((-1. / 2500) * (k - 150) ** 2) for k in range(size)]


def create_x3(size):
    x = []
    for k in range(size):
        val = 0
        if k >= 240 and k < 300:
            val = 1
        if k >= 300 and k < 380:
            val = -2
        x.append(val)
    return x


def create_x4(size, mu=0, sigma=1.0):
    return np.random.normal(mu, sigma, size)


def show_plot(x, y, title="Plot", x_name="x", y_name="y"):
    plt.figure()
    plt.plot(x, y)
    plt.grid()
    plt.title(title)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.show()

size = 500
x1 = create_x1(size)
x2 = create_x2(size)
x3 = create_x3(size)
x4 = create_x4(size, sigma=0.2)

sum_of_3 = [x1[i] + x2[i] + x3[i] for i in range(size)]

# print len(x1+x2+x4)

show_plot(range(size), sum_of_3, "Sum of three signals", "k", "x1 + x2 + x3")
show_plot(range(size), map(sum, zip(sum_of_3, x4)), "Sum of four signals", "k", "x1 + x2 + x3 + x4")

plt.plot([1,2,3,4,5], [5,5,5,5,5], '--', marker='h', linewidth=2)
plt.show()