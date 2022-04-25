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
selection = [2.69313, 2.58120, 1.65158, -0.13676, 0.73879, 3.12903, 1.24891, 1.65969, 1.67673, 0.31233,
             2.84346, 1.38789, 2.20853, 2.01193, 1.60222, 2.03934, -0.25607, 0.51361, 1.80986, 1.43246,
             1.92215, 0.79266, 0.97779, 3.17598, 1.72724, 3.10132, -1.08952, 1.15506, 2.08532, 1.24363,
             2.41664, -0.80582, 0.92461, 0.74331, 0.72599, 3.64545, 1.33097, 2.47967, 1.53104, 1.05968,
             2.09533, 1.36383, 3.84179, 1.44353, 1.27075, 0.41050, 2.61679, 1.97747, 2.16984, 3.06051,
             1.08923, 2.85596, 0.53417, 2.26648, 0.70592, 1.92161, 2.05596, 3.50340, 1.82912, 0.79804,
             2.34303, 2.67661, 2.24360, 3.55402, 0.19313, 2.94669, 2.01861, 1.94206, 1.61611, 3.57585,
             1.51093, 1.96852, 0.84607, 0.64167, 3.13217, 2.06708, 0.42632, 0.69439, 3.16171, 0.34244,
             2.71914, 2.94773, 0.75377, -0.18781, 3.10358, 0.98482, 2.13977, 1.19443, 2.06028, 1.19757,
             1.07916, 2.31470, 3.41765, 1.42679, 0.69600, 0.99766, 1.49135, 3.13415, 1.14803, 1.67345,
             0.67041, 2.16885, 2.31975, 2.51700, 2.03438, 1.78206, 4.05507, 2.88808, 0.86060, 2.36700,
             0.67884, 1.14831, 1.39630, 1.31568, 4.45068, 0.92709, 0.71126, 2.57154, 2.07517, 1.38259,
             1.04161, 0.68571, 1.63723, 1.50849, 2.14899, 0.00171, 3.01567, 0.72523, 3.51621, 0.65437,
             2.80248, 0.44416, 1.78276, 1.29491, 1.84611, 2.39493, 2.54815, 2.96554, 1.86823, 2.89017,
             0.56701, 0.49632, 0.07590, 2.03472, 0.71523, 1.68091, 1.77303, 1.80197, 1.67275, 0.84066,
             2.58562, 4.40465, 0.61977, 1.64639, 1.79333, 2.51389, 2.41748, 4.37734, 0.11893, 1.79018,
             2.38307, 1.57555, 0.77407, -0.13859, 3.28975, 2.36910, 1.93435, 1.38173, 1.09129, 0.84755,
             1.74445, 0.36601, 2.79856, 0.56996, 2.32588, -0.08825, 4.71731, 2.09959, 0.81078, 0.76911,
             2.88010, 1.51335, 1.81708, 5.09559, 1.51215, 4.13606, 0.95363, 1.08529, 0.69827, 1.42450,
             2.11128, 1.69972, 2.12422, 1.61286, 1.29775, 2.85780, 0.01386, 3.21493, 2.08895, 3.75099]
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
print("p*", p_star, "sum p*", sum(p_star))

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
print("sum w", sum(w), "sum p*", sum(p_star), "max |w_i - p*_i|", max(deviation), "sum N(p*-w)^2:p*", round(sum(Npw2p), 5))

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
