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


