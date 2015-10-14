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

def show_arr(y, title="Plot", x_name="x", y_name="y"):
    show_plot(range(len(y)), y, title, x_name, y_name)


def singleLowPassFilter(x):
    y = [0.]
    for k in range(1, len(x)):
        y.append(.05 * x[k] + .95 * y[k-1])
    return y

if __name__ == "__main__":
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

    x_noisy = map(sum, zip(sum_of_3, x4))
    x_noisy_filtered = singleLowPassFilter(x_noisy)

    # question 1.4
    show_arr(sum_of_3, "Sum of three signals", "k", "x1 + x2 + x3")
    show_arr(map(sum, zip(sum_of_3, x4)), "Sum of four signals", "k", "x1 + x2 + x3 + x4")

    # question 1.6
    show_arr(x1, "x1", "k", "x1")
    show_arr(x1_filtered, "x1 filtered", "k", "S(x1)")
    show_arr(x2, "x2", "k", "x2")
    show_arr(x2_filtered, "x2 filtered", "k", "S(x2)")
    show_arr(x3, "x3", "k", "x3")
    show_arr(x3_filtered, "x3 filtered", "k", "S(x3)")

    # question 1.7
    show_arr(sum_of_3, "Sum of three signals", "k", "x1 + x2 + x3")
    show_arr(singleLowPassFilter(sum_of_3), "Sum of three signals filtered", "k", "S(x1+x2+x3)")

    # question 1.8
    show_arr(sum_of_filtered_3, "Sum of three filters", "k", "S(x1)+S(x2)+S(x3)")

    # question 1.10
    show_arr(x_noisy, "x_noisy", "k", "x_noisy")
    show_arr(x_noisy_filtered, "x_noisy filtered", "k", "S(x_noisy)")

    # question 2.5, 2.6, 2.7
    from convolution import myMovingAverage
    x_noisy_mov_average = myMovingAverage(x_noisy, 51)
    show_arr(x_noisy_filtered, 'Moving average on gaussian noise', 'k', 'y')
    show_arr(x_noisy_filtered, "x_noisy filtered", "k", "S(x_noisy)")