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
first = [8.98916, 12.74455, 7.54412, 7.14413, 5.67097, 11.95328,
         8.65550, 7.89505, 12.72736, 13.46213, 8.66133, 6.77688,
         9.73556, 15.18698, 4.38339, 11.76695]
# second ksi
second = [12.11567, 9.91673, 7.23929, 12.86704, 7.02257, 9.00369,
          4.69718, 12.07695, 7.30159, 4.80794, 12.67437, 8.61648,
          6.82806, 11.53224, 11.06643, 2.19140]
# third ksi
third = [1.62073, 6.44220, 6.21874, 11.27553, 9.41593, 12.11049,
         12.98772, 7.60639, 10.80071, 10.35897, 9.74924, 11.85632,
         11.94754, 8.48395, 7.89188, 6.74048]

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
