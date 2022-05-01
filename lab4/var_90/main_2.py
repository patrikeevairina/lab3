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
first = [12.17702, 14.01000, 12.09198, 11.18424, 11.82169, 12.18678, 9.17935,
         10.65043, 7.17028, 10.84520, 8.46016, 8.84723, 9.28104, 8.58507,
         8.56640, 7.99559]
# second ksi
second = [5.93275, 9.89971, 9.91496, 6.28285, 10.52099, 12.62202, 12.55684,
          7.37434, 6.93578, 15.83671, 12.01177, 9.66646, 4.43970, 11.35868,
          8.32329, 10.09010]
# third ksi
third = [9.84826, 5.14551, 12.46817, 11.83668, 11.19952, 5.17841, 10.08253,
         14.44858, 10.13184, 6.25333, 11.63221, 5.40682, 9.21548, 12.85413,
         9.21191, 7.85235]

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
    f.append(round(f[-2] / f[-1], 5))
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
