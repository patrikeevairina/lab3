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
selection = [2.60585, 1.05992, 2.25916, 2.77867, 3.87064, 3.11569, 2.29362, 1.03198, 1.34448, 0.79606,
1.97487, 2.54213, 1.85558, 1.81515, 3.84493, 0.94916, 2.42179, 1.00064, 2.65424, 3.23593,
2.66450, -1.40894, 2.84607, -1.68149, 1.45782, 1.47007, 2.51015, 1.64685, 2.07957, 1.10848,
1.38015, -0.19910, 1.42072, 2.46951, 1.44064, 0.51260, 0.56642, 1.60624, 3.13935, 2.08686,
2.33293, 1.45356, 3.84454, 2.24727, 0.85469, 3.08892, 2.58435, 2.36683, 0.23879, 2.98495,
2.13770, 1.91611, 2.42612, 3.11925, 2.25104, 0.27640, 3.50754, -0.29898, 2.33473, 2.22604,
2.88520, 2.25389, 0.48842, 3.01316, 0.02701, 2.76775, 0.24626, 2.64225, 1.25533, 3.37128,
3.29037, 1.27520, 3.40249, 2.00660, 2.22509, 1.68096, 1.59331, -0.30690, 4.32453, 2.02376,
2.98231, 1.84188, 1.92726, 1.34700, 2.74348, 3.70148, 2.28058, 4.15097, 1.60436, 2.02691,
2.23991, 4.07072, 2.96681, 1.60333, 1.33561, 2.60021, 1.66375, 0.82960, 0.82705, 1.62860,
1.93093, 0.82282, 1.59680, 2.03236, 2.12343, 1.39131, 1.67864, 4.08267, 2.56348, 2.56023,
3.32717, 1.02812, 1.50522, 1.27206, 1.67724, 2.84229, 1.51958, 2.28252, 2.20620, 1.49458,
1.89467, 0.13379, 1.84906, 1.90881, 2.12558, 3.02229, 3.08252, 0.57145, 3.06677, 0.66263,
0.03449, -1.59235, 1.50066, 2.13225, 1.22408, 1.72769, 1.51347, 1.26659, 0.61027, -0.35698,
2.45378, 1.14200, 2.63302, 4.37462, 2.16861, 0.43753, 0.70451, 1.58465, 1.86787, 2.79281,
0.12505, 1.57748, 2.52445, -1.35221, 0.57127, 3.63065, 1.43877, 2.22290, 0.70897, 2.80593,
2.73367, 2.37474, 1.60972, 3.45548, 2.19237, 1.23672, 0.86269, 2.93679, 0.67714, 1.54390,
0.41098, 0.54285, 2.99861, 1.51301, 1.32048, 2.95348, 4.06014, 0.58498, 1.31266, 4.22740,
2.38107, 1.56282, 0.06471, 0.61270, 1.83151, 4.78596, 0.88802, 1.96230, 0.85957, 2.19184,
2.20107, 2.77390, 3.20820, 0.82178, 2.77317, 0.79014, 2.25538, 0.72067, 2.50575, 0.50733]
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
for i in range(m+1):
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
    density.append(round(pow(math.e, (-1) * pow((i-math_exp)/sigma, 2) / 2) / (sigma * pow(2 * math.pi, 0.5)), 5))
hystogram(selection, a, density)

# таблица 3.3

#|w_i - p*_i|
deviation = [round(abs(p_star[i] - w[i]), 5) for i in range(m)]
#print("|w_i - p*_i|", deviation, "max", max(deviation))

# N(p*-w)^2:p*
Npw2p = [round((num * deviation[i] ** 2) / p_star[i], 5) for i in range(m)]
#print("N(p*-w)^2:p*", Npw2p, "sum", round(sum(Npw2p), 5))

print("Table 3.3")
for i in range(m):
    if i == 0:
        print(i + 1, ".", "Интервал", "[", round(a[i], 5), ",", round(a[i + 1], 5), "]", f"w_{i + 1} =", w[i],
              f"p_{i + 1}* =", p_star[i], f"|w_{i + 1}",  "-", f"p_{i + 1}*|", " = ", deviation[i],
              f"N(p_{i + 1}*-w_{i + 1})^2:p_{i + 1}*", Npw2p[i])
    else:
        print(i + 1, ".", "Интервал", "(", round(a[i], 5), ",", round(a[i + 1], 5), "]", f"w_{i + 1} =", w[i],
              f"p_{i + 1}* =", p_star[i], f"|w_{i + 1}",  "-", f"p_{i + 1}*|", " = ", deviation[i],
              f"N(p_{i + 1}*-w_{i + 1})^2:p_{i + 1}*", Npw2p[i])
print("sum w", sum(w), "sum p*", sum(p_star), "max |w_i - p*_i|", max(deviation), "sum N(p*-w)^2:p*", sum(Npw2p))

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
