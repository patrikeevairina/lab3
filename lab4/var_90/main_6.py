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
