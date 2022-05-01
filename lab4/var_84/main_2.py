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
first = [11.62084, 6.84302, 8.25088, 12.45885, 9.24030, 8.52812, 5.51490,
         10.08981, 9.23398, 5.64812, 8.40212, 8.85134, 8.85888, 11.69726,
         5.71799, 10.58310]
# second ksi
second = [7.54233, 9.63132, 13.30971, 6.04009, 9.54650, 5.19554, 9.30450,
          12.93261, 5.08283, 10.35184, 9.17455, 6.73624, 8.15137, 10.53550,
          10.49489, 10.24960]
# third ksi
third = [7.72909, 9.64423, 8.08131, 10.19118, 3.30469, 4.25265, 9.58360,
         7.41564, 10.78318, 8.79014, 8.51658, 7.88441, 10.68688, 7.17759,
         9.30146, 10.11943]

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
