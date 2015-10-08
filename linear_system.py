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


def singleLowPassFilter(x):
    y = [0]
    for k in range(1, len(x)):
        y.append(.05 * x[k] + .95 * y[k-1])
    return y

size = 500
x1 = create_x1(size)
x2 = create_x2(size)
x3 = create_x3(size)
x4 = create_x4(size, sigma=0.2)

x1_filtered = singleLowPassFilter(x1)
x2_filtered = singleLowPassFilter(x2)
x3_filtered = singleLowPassFilter(x3)

sum_of_3 = [x1[i] + x2[i] + x3[i] for i in range(size)]
sum_of_filtered_3 = [x1_filtered[i] + x2_filtered[i] + x3_filtered[i] for i in range(size)]

x_noise = map(sum, zip(sum_of_3, x4))
x_noise_filtered = singleLowPassFilter(x_noise)

# show_plot(range(size), sum_of_3, "Sum of three signals", "k", "x1 + x2 + x3")
# show_plot(range(size), map(sum, zip(sum_of_3, x4)), "Sum of four signals", "k", "x1 + x2 + x3 + x4")

# question 1.6
show_plot(range(size), x1, "x1", "k", "x1")
show_plot(range(size), x1_filtered, "x1 filtered", "k", "S(x1)")
show_plot(range(size), x2, "x2", "k", "x2")
show_plot(range(size), x2_filtered, "x2 filtered", "k", "S(x2)")
show_plot(range(size), x3, "x3", "k", "x3")
show_plot(range(size), x3_filtered, "x3 filtered", "k", "S(x3)")

# question 1.7
show_plot(range(size), sum_of_3, "Sum of three signals", "k", "x1 + x2 + x3")
show_plot(range(size), singleLowPassFilter(sum_of_3), "Sum of three signals filtered", "k", "S(x1+x2+x3)")

# question 1.8
show_plot(range(size), sum_of_filtered_3, "Sum of three filters", "k", "S(x1)+S(x2)+S(x3)")

# question 1.10
show_plot(range(size), x_noise, "x_noise", "k", "x_noise")
show_plot(range(size), x_noise_filtered, "x_noise filtered", "k", "S(x_noise)")