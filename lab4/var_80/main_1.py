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
    #print(x, " sample aver")
    return x


# выборочная несмещенная дисперсия
def unbiased_variance(sel):
    x2 = 0
    for i in range(N):
        x2 += sel[i]**2
    x2 = round(x2 / N, 5)
    #print(x2, " variance")
    return x2


# S**2
def s2(sel):
    x = sample_average(sel)
    x2 = unbiased_variance(sel)
    return round(N * (x2 - x**2) / (N - 1), 5)


# критерий T_n,m
def crit_t(sel_1, sel_2):
    l = N + N - 2
    x = sample_average(sel_1)
    y = sample_average(sel_2)
    crit = (x - y) * pow(l * N**2, 0.5) / pow((N - 1) * (N + N) * (s2(sel_1) + s2(sel_2)), 0.5)
    #print(crit, " T_nm")
    return round(crit, 5)


# задание 4.1
print("столбцы      x       y       x**2      y**2      S**2_x      S**2_y     T_nn")
print("(1,2) ", sample_average(first), " ", sample_average(second), " ", unbiased_variance(first), " ", unbiased_variance(second), " ", s2(first), " ", s2(second), " ", crit_t(first, second))
print("(1,3) ", sample_average(first), " ", sample_average(third), " ", unbiased_variance(first), " ", unbiased_variance(third), " ", s2(first), " ", s2(third), " ", crit_t(first, third))
print("(2,3) ", sample_average(second), " ", sample_average(third), " ", unbiased_variance(second), " ", unbiased_variance(third), " ", s2(second), " ", s2(third), " ", crit_t(second, third))

crit_x = 0.975
crit_n = 2 * N - 2
critical_value = round(scipy.stats.t.ppf(crit_x, crit_n), 5)

# проверка выборок 1 и 2
if crit_t(first, second) <= critical_value:
    result_1_2 = " Верна"
else:
    result_1_2 = " Неверна"

# проверка выборок 1 и 3
if crit_t(first, third) <= critical_value:
    result_1_3 = " Верна"
else:
    result_1_3 = " Неверна"

# проверка выборок 2 и 3
if crit_t(second, third) <= critical_value:
    result_2_3 = " Верна"
else:
    result_2_3 = " Неверна"

print("\nстолбцы    |T_nn|    t_кр_а    Вывод")
print("(1,2)    ", abs(crit_t(first, second)), " ", critical_value, result_1_2)
print("(1,3)    ", abs(crit_t(first, third)), " ", critical_value, result_1_3)
print("(2,3)    ", abs(crit_t(second, third)), " ", critical_value, result_2_3)


