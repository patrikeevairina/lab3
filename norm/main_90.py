import math
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import pylab as p
import scipy.stats
from numpy import random
from matplotlib import ticker
from scipy import integrate

num = 200


def hystogram(sel, a, dens):
    fig, ax = plt.subplots()
    ax.hist(sel, bins=a, density=True, color="White", edgecolor="Black", linewidth=0.5)
    ax.plot(sel, dens, 'r', linewidth=1.0)
    plt.show()


# Выборка
# print("---------------Выборка неупорядоченная---------------")
selection = [2.85397, 2.37323, 2.05933, 3.50381, 0.60270, -0.31749, 3.95850, 2.64085, -0.06291, 1.71309,
             2.58855, 1.97461, 2.70808, 1.10317, 2.01549, -0.48773, 1.24560, 0.25226, 1.15219, 2.56066,
             2.60455, -0.04832, 1.86912, 1.77340, 0.74580, 3.34646, 0.97515, 1.98221, 0.97328, 2.91043,
             3.18748, 2.05108, 3.00256, 2.34554, 2.41797, 0.16714, 0.74951, -0.28248, 0.60404, 3.31635,
             0.74749, 2.70222, 2.18985, 0.57537, 2.31556, -0.07918, -0.12104, 1.33749, 1.53116, -1.36772,
             3.29303, 1.90528, 1.93921, 3.29845, 1.72000, 0.65568, 2.73176, 1.81693, 2.66178, 3.26696,
             2.52038, 1.89866, 3.26182, 1.18897, 1.06964, 2.64742, 0.86416, 0.57852, 3.26049, 3.25476,
             2.22634, 1.26632, 0.76487, 4.31656, 2.43143, 2.89045, 2.47143, 1.76269, 1.64656, 2.15037,
             0.76000, 1.38459, 2.90757, 0.23092, 1.22529, 1.58364, 2.18585, 1.58386, 1.11629, 4.40912,
             1.04998, -0.92038, 4.06823, 4.19048, 3.01300, 1.72806, 1.27623, 2.40547, 1.38687, 1.50537,
             2.01720, 0.15191, 1.97756, 1.04116, 1.57357, 1.00086, 3.08390, 2.38637, -0.10446, 1.61458,
             1.78219, 2.56470, 0.71198, 1.56823, 2.63619, 1.18525, 2.59103, 2.51285, 0.66703, 1.88535,
             1.44893, 1.68706, 1.29875, 3.44083, 1.49943, 4.11534, 1.25441, 3.91058, 1.69337, 3.08455,
             1.34811, 3.13572, 2.60041, 2.81589, 1.39792, 1.59448, 3.43495, 2.03728, 2.56587, -1.77722,
             2.08805, 2.24951, 1.15487, 2.47368, 1.39587, 1.92450, 2.49351, 0.60060, 0.88763, 1.57470,
             1.65682, 1.74637, -1.03051, 3.62761, 0.82896, 1.87646, 1.03217, 0.82269, 3.26264, -0.61998,
             1.81375, -0.81399, 2.72902, 2.63225, 2.46307, 1.83702, 2.61439, 2.05891, 1.99692, 2.57300,
             1.77296, 3.40733, 0.90601, 3.83700, 3.91178, 3.45405, 3.39082, 3.80414, -0.23596, 1.66418,
             -1.15813, 4.48815, 2.54047, 2.29067, 4.57762, 0.95589, 1.97124, 0.65874, 1.93356, 0.71028,
             2.92388, 2.35139, 0.28417, 1.49938, 2.03030, 1.64345, 2.57725, 1.46309, 0.94162, 2.57283]
print(selection)

print("---------------Выборка упорядоченная---------------")
selection.sort()
print(selection)

# Группированная выборка, таблица 3.1
# Число интервалов по формуле Стерджеса
m = 1 + int(math.log2(num))

# Шаг
h = (selection[199] - selection[0]) / m

# a_i
a = [i for i in range(m + 1)]
a[0] = min(selection)
for i in range(1, m + 1):
    a[i] = a[i - 1] + h
for i in range(m + 1):
    a[i] = round(a[i], 5)

# x*
x_star = [round(a[i + 1] - h / 2, 5) for i in range(m)]

# n_i
n = [0 for i in range(m)]
i = 0
while a[0] <= selection[i] <= a[1] and i < num:
    n[0] += 1
    i += 1
for i in range(1, m):
    for j in range(num):
        if a[i] < selection[j] <= a[i + 1]:
            n[i] += 1

# w
w = [n[i] / num for i in range(m)]

print("Table 3.1")
print("---------------Группированная выборка---------------")
for i in range(m):
    if i == 0:
        print(i + 1, ".", "Интервал", "[", round(a[i], 5), ",", round(a[i + 1], 5), "]", f"x_{i + 1}* =", x_star[i],
              f"n_{i + 1} =", n[i], f"w_{i + 1} =", w[i])
    else:
        print(i + 1, ".", "Интервал", "(", round(a[i], 5), ",", round(a[i + 1], 5), "]", f"x_{i + 1}* =", x_star[i],
              f"n_{i + 1} =", n[i], f"w_{i + 1} =", w[i])
print("Сумма n_i", sum(n), "Сумма w_i", round(sum(w), 5))

# math exp M
math_exp = round(sum([w[i] * x_star[i] for i in range(m)]), 5)
print("мат ожидание", math_exp)

# dispersion
sigma_2 = round(sum([w[i] * (x_star[i] ** 2) for i in range(m)]), 5)
sigma_2 = sigma_2 - math_exp**2
print("дисперсия", sigma_2)

# вся фигня для таблицы 3.2
sigma = round(sigma_2 ** 0.5, 5)
print("sigma", sigma)

t = []
f = []
bigF = []
p_star = []
for i in range(m + 1):
    t.append(round((a[i] - math_exp) / sigma, 5))
    f.append(round(pow(math.e, (-1) * (t[-1] ** 2) / 2) / (sigma * ((2 * math.pi) ** 0.5)), 5))
    bigF.append(round(scipy.stats.norm.cdf(t[-1]), 5))
    if 0 < i < m:
        if i == 1:
            p_star.append(round(bigF[-1], 5))
        else:
            p_star.append(round(bigF[-1] - bigF[-2], 5))
    if i == m:
        p_star.append(round(1 - bigF[-2], 5))

print("Table 3.2")
print("a", a)
print("t", t)
print("f", f)
print("F", bigF)
print("p*", p_star, "sum p*", round(sum(p_star), 5))

# гистограмма и функция
density = []
for i in selection:
    density.append(round(pow(math.e, (-1) * pow((i - math_exp) / sigma, 2) / 2) / (sigma * pow(2 * math.pi, 0.5)), 5))
hystogram(selection, a, density)

# таблица 3.3

# |w_i - p*_i|
deviation = [round(abs(p_star[i] - w[i]), 5) for i in range(m)]
# print("|w_i - p*_i|", deviation, "max", max(deviation))

# N(p*-w)^2:p*
Npw2p = [round((num * deviation[i] ** 2) / p_star[i], 5) for i in range(m)]
# print("N(p*-w)^2:p*", Npw2p, "sum", round(sum(Npw2p), 5))

print("Table 3.3")
for i in range(m):
    if i == 0:
        print(i + 1, ".", "Интервал", "[", round(a[i], 5), ",", round(a[i + 1], 5), "]", f"w_{i + 1} =", w[i],
              f"p_{i + 1}* =", p_star[i], f"|w_{i + 1}", "-", f"p_{i + 1}*|", " = ", deviation[i],
              f"N(p_{i + 1}*-w_{i + 1})^2:p_{i + 1}*", Npw2p[i])
    else:
        print(i + 1, ".", "Интервал", "(", round(a[i], 5), ",", round(a[i + 1], 5), "]", f"w_{i + 1} =", w[i],
              f"p_{i + 1}* =", p_star[i], f"|w_{i + 1}", "-", f"p_{i + 1}*|", " = ", deviation[i],
              f"N(p_{i + 1}*-w_{i + 1})^2:p_{i + 1}*", Npw2p[i])
print("sum w", sum(w), "sum p*", round(sum(p_star), 5), "max |w_i - p*_i|", max(deviation), "sum N(p*-w)^2:p*",
      round(sum(Npw2p), 5))

l = m - 3  # число степеней свободы
hi_sq = round(sum(Npw2p), 5)
print("хи-квадрат ", hi_sq)
if l == 4:
    crit_meaning_hi = 9.5
if l == 5:
    crit_meaning_hi = 11.1
if l == 6:
    crit_meaning_hi = 12.6
if l == 7:
    crit_meaning_hi = 14.1
if l == 8:
    crit_meaning_hi = 15.5

if hi_sq <= crit_meaning_hi:
    print(f"{hi_sq} <= {crit_meaning_hi} Гипотеза НЕ ПРОТИВОРЕЧИТ экспериментальным данным")
else:
    print(f"{hi_sq} > {crit_meaning_hi} Гипотеза ПРОТИВОРЕЧИТ экспериментальным данным")
