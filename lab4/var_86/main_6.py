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

# N = M = 16 (кол-во строк)
N = 16


# выборочное среднее
def sample_average(sel):
    x = 0
    for i in range(N):
        x += sel[i]
    x = round(x / N, 5)
    return x


# выборочная несмещенная дисперсия
def unbiased_variance(sel):
    x2 = 0
    for i in range(N):
        x2 += sel[i]**2
    x2 = round(x2 / N, 5)
    return x2


# S**2
def s2(sel):
    x = sample_average(sel)
    x2 = unbiased_variance(sel)
    return round(N * (x2 - x**2) / (N - 1), 5)


def crit_f(sel_1, sel_2):
    sx = s2(sel_1)
    sy = s2(sel_2)
    return round(max(sx, sy) / min(sx, sy), 5)


k = N - 1

# table 1
print("столбцы  S2_1    S2_2    k1  k2  F_NM")
print("(1,2) ", s2(first), " ", s2(second), " ", k, " ", k, " ", crit_f(first, second))
print("(1,3) ", s2(first), " ", s2(third), " ", k, " ", k, " ", crit_f(first, third))
print("(2,3) ", s2(second), " ", s2(third), " ", k, " ", k, " ", crit_f(second, third))

critical_x = 0.975
critical_value = round(scipy.stats.f.ppf(critical_x, k, k), 5)

# проверка выборок 1 и 2
if crit_f(first, second) <= critical_value:
    result_1_2 = " Верна"
else:
    result_1_2 = " Неверна"

# проверка выборок 1 и 3
if crit_f(first, third) <= critical_value:
    result_1_3 = " Верна"
else:
    result_1_3 = " Неверна"

# проверка выборок 2 и 3
if crit_f(second, third) <= critical_value:
    result_2_3 = " Верна"
else:
    result_2_3 = " Неверна"

print("\nстолбцы    F_NM       z_a    Вывод")
print("(1,2)    ", crit_f(first, second), " ", critical_value, result_1_2)
print("(1,3)    ", crit_f(first, third), " ", critical_value, result_1_3)
print("(2,3)    ", crit_f(second, third), " ", critical_value, result_2_3)
