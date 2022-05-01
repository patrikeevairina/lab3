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
