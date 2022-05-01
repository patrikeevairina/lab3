import math
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import pylab as p
import scipy.stats
from numpy import random
from matplotlib import ticker
from scipy import integrate

# first ksi
first = [6.30334, 8.02645, 12.16487, 5.83584, 7.83086, 8.83664, 11.40085,
         9.56617, 5.73439, 8.50632, 10.53921, 8.79242, 10.09223, 8.11867,
         7.41681, 10.03095]
# second ksi
second = [2.07593, 13.02856, 8.29968, 6.49767, 8.40741, 6.84572, 9.48804,
          8.26982, 9.23229, 10.77608, 6.78528, 9.83676, 9.58789, 8.86324,
          9.15862, 6.99994]
# third ksi
third = [5.05028, 5.62454, 14.79647, 9.90348, 9.11461, 9.17246, 3.82668,
         9.40738, 8.85070, 4.16049, 9.01353, 13.81358, 8.98545, 8.55382,
         5.77914, 9.02385]

sel_2d = [first, second, third]

# N = M = 16 (кол-во строк)
N = 16
m = 3


def sample_average(sel):
    u = 0
    for j in range(m):
        for i in range(N):
            u += sel[j][i]
    u = round(u / (N * m), 5)
    return u


def group_average(sel):
    u = [0 for i in range(m)]
    for j in range(m):
        for i in range(N):
          u[j] += round(sel[j][i] / N, 5)
    return u


def total_sum_sq_dev(sel):
    average = sample_average(sel)
    s = 0
    for j in range(m):
        for i in range(N):
            s += (sel[j][i] - average) ** 2
    return round(s, 5)


def fact_sum_sq_dev(sel):
    u = group_average(sel)
    average = sample_average(sel)
    s = 0
    for j in range(m):
        s += round((u[j] - average) ** 2, 5)
    s = s * N
    return s


def residual_sum_sq_dev(sel):
    return total_sum_sq_dev(sel) - fact_sum_sq_dev(sel)


def crit_f(sel):
    f = []
    f.append(round(fact_sum_sq_dev(sel) / (m - 1), 5))
    f.append(round(residual_sum_sq_dev(sel) / (m * (N - 1)), 5))
    f.append(round(f[-1] / f[-2], 5))
    return f

# задание 4.2
# table 1
print("S_общ        S_факт    S_ост    s^2_fact    s^2_ost  k1  k2    F_nm")
print(total_sum_sq_dev(sel_2d), " ", fact_sum_sq_dev(sel_2d), " ", residual_sum_sq_dev(sel_2d), " ", crit_f(sel_2d)[0], " ", crit_f(sel_2d)[1], " ", m - 1, " ", m * (N - 1), " ", crit_f(sel_2d)[2])

critical_x = 0.95
k1 = m - 1
k2 = m * (N - 1)
critical_value = round(scipy.stats.f.ppf(critical_x, k1, k2), 5)
if crit_f(sel_2d)[2] <= critical_value:
    result = " Верна"
else:
    result = " Неверна"

# table 2
print("\nF_N,m      a     F_кр(k1,k2)    Вывод")
print(crit_f(sel_2d)[2], " ", 0.05, " ", critical_value, "    ", result)
