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
selection = [1.51415, 1.38381, 1.74510, 2.00048, 2.37344, 0.64218, 1.34853, 2.18434, -1.04574, 0.94475,
             1.23294, 2.89430, -0.25046, 1.51965, 1.03693, 1.72351, 2.02739, 2.26819, 3.70217, 1.66864,
             0.56624, 1.64397, 1.96839, -0.42597, 1.98972, 0.61845, 0.29097, 3.08841, 2.19951, 2.71257,
             2.64996, 0.79693, 4.46100, 0.64779, 1.18465, 2.55723, 1.63040, 3.19211, 1.03938, 2.47442,
             1.96552, 1.94308, 1.96141, 1.85860, 1.08047, -0.37193, 4.65703, 3.00518, 2.70550, 1.51399,
             3.11221, 3.20807, 3.86560, 1.18308, 3.44864, 1.24791, 2.51077, 0.86411, 2.10694, 2.46329,
             1.71520, 3.67355, 1.90298, 2.15837, 2.01753, 0.75154, 0.77797, 1.92075, 2.61277, 2.68394,
             2.47239, 0.31114, 1.52813, 2.73092, 1.65135, 3.00695, 1.01369, 2.70408, -0.64102, 3.54505,
             2.03344, 2.99750, 3.77503, 1.34392, 4.15018, 2.23287, 3.47121, -0.43593, 0.59192, 1.34212,
             1.53832, 3.36488, 1.92168, 2.67356, 2.71051, -1.84003, 3.69703, 2.33997, 2.87124, 0.22575,
             2.87676, 0.95820, 1.85876, 3.17320, 0.68574, 0.46750, -0.41867, 0.80309, 1.11283, 1.59880,
             3.14174, 1.47396, 2.03771, 3.56859, 1.85821, 2.28074, 1.69116, 3.79629, 2.03841, -0.49004,
             2.52321, 2.51805, 2.61800, 2.93988, 2.11005, 1.97056, 2.10303, 0.46147, -1.36063, 1.76149,
             2.62210, 0.71071, 0.17786, 3.73813, 1.94181, -0.03063, 2.51752, 2.53458, 1.67018, 2.06693,
             4.49946, 1.92430, 0.56661, 1.20467, 3.85477, 2.20305, 2.63188, 2.49402, 2.76084, 2.43290,
             1.37467, 2.02449, 3.38272, 1.70014, 4.12541, 0.43854, -0.17093, 1.33111, 1.43691, 1.24383,
             1.29140, 1.91162, -0.25772, 3.26739, 1.39063, 0.90997, 0.47049, 2.62385, 1.83202, 3.11487,
             2.08170, 2.81063, 1.10868, 3.25054, 1.15227, 4.07026, 2.31916, 0.82815, 1.77403, 2.94461,
             2.30381, 1.86547, -1.96805, 1.76994, 2.61052, 1.65493, 0.09136, 1.47463, 3.37358, 0.70737,
             1.26216, -0.20962, 2.49411, 0.08870, 1.55492, 0.45697, 1.09720, 0.26971, 1.69327, 1.07738]
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
