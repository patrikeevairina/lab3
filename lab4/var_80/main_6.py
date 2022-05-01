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
         9.56617, 5.73439, 8.50632, 10.53921, 8.79242, 10.09223, 10.09223,
         7.41681, 10.03095]
# second ksi
second = [2.07593, 13.02856, 8.29968, 6.49767, 8.40741, 6.84572, 9.48804,
          8.26982, 9.23229, 10.77608, 6.78528, 9.83676, 9.58789, 8.86324,
          9.15862, 6.99994]
# third ksi
third = [5.05028, 5.62454, 14.79647, 9.90348, 9.11461, 9.17246, 3.82668,
         9.40738, 8.85070, 4.16049, 9.01353, 13.81358, 8.98545, 8.98545,
         5.77914, 9.02385]

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
