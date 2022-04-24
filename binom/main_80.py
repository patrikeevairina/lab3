import math
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import scipy.stats
from numpy import random
from matplotlib import ticker


def math_exp(x_i, w_i):
    M = 0.0
    for i in range(len(x_i)):
        M += x_i[i] * w_i[i]
    print(round(M, 6), " экспериментальное среднее")


def print_polygons(x_i, w_i, n, p):
    fig, ox = plt.subplots()
    ox.plot(x_i, w_i, 'b')
    ox.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
    ox.xaxis.set_major_locator(ticker.MultipleLocator(1))

    teor_w_i = np.zeros(len(x_i))
    for i in range(len(x_i)):
        teor_w_i[i] = (math.comb(n, x_i[i]) * (p ** x_i[i]) * ((1 - p) ** (n - x_i[i])))
    ox.plot(x_i, teor_w_i, 'r')
    plt.title("Полигон относительных частот")
    plt.grid()

    plt.show()


# Выборка
# print("---------------Выборка неупорядоченная---------------")
_n = 6
selection = [3, 3, 2, 1, 1, 2, 3, 2, 4, 2,
             3, 2, 1, 4, 2, 2, 6, 2, 2, 4,
             4, 2, 3, 2, 3, 3, 2, 3, 4, 1,
             4, 2, 4, 4, 3, 5, 2, 1, 1, 5,
             3, 4, 1, 3, 3, 2, 2, 2, 4, 4,
             3, 3, 3, 2, 3, 1, 2, 3, 3, 4,
             2, 2, 3, 2, 3, 3, 5, 3, 4, 3,
             2, 3, 4, 2, 4, 4, 5, 2, 1, 4,
             5, 3, 5, 3, 4, 0, 3, 2, 2, 4,
             5, 2, 2, 1, 5, 4, 2, 2, 1, 4,
             2, 4, 3, 4, 1, 5, 2, 3, 4, 4,
             5, 3, 2, 2, 3, 3, 2, 3, 2, 5,
             1, 2, 1, 5, 1, 3, 4, 2, 4, 1,
             3, 2, 3, 2, 1, 2, 2, 2, 2, 4,
             1, 0, 4, 2, 4, 1, 1, 5, 4, 3,
             4, 5, 3, 2, 4, 2, 3, 3, 3, 4,
             2, 3, 4, 3, 2, 3, 3, 3, 4, 1,
             4, 1, 3, 1, 2, 3, 3, 3, 5, 3,
             2, 2, 4, 3, 0, 4, 2, 5, 3, 5,
             4, 2, 3, 2, 1, 3, 2, 3, 3, 3]
print(selection)

print("---------------Выборка упорядоченная---------------")
selection.sort()
print(selection)

print("Table 1.1")
# x -- значения без повторений
x = list(np.unique(selection))
print("x", x)

# n -- количество различных значений
count = Counter(selection)
n = list(count.values())
print("n", n, "sum n", sum(n))

# w -- относительные частоты
w = [0 for i in range(len(count))]
for i in range(len(count)):
    w[i] = n[i] / 200.0
print("w", w, "sum w", round(sum(w), 5))

# Мат ожидание
_m = 0.0
for i in range(len(x)):
    _m += x[i] * w[i]
# print("M", _m)

# оценка параметра р
# насколько я поняла, вывелось из M=n*p => p = M/n
_p = _m / _n
# print("оценка параметра р", _p)

# отрисовка полигонов по отн частотам и по вероятности p и параметру n
print_polygons(x, w, _n, _p)

# таблица 1.2
print("Table 1.2")
print("x", x)
print("w", w, "sum w", round(sum(w), 5))
# p*
teor_p_i = np.zeros(len(x))
for i in range(len(x)):
    teor_p_i[i] = round((math.comb(_n, x[i]) * (_p ** x[i]) * ((1 - _p) ** (_n - x[i]))), 5)
print("p*", teor_p_i, "sum", round(sum(teor_p_i), 5))

# |w_i - p*_i|
print("|w_i - p*_i|", abs(teor_p_i - w), "max", round(max(abs(teor_p_i - w)), 5))

# N(p*-w)^2:p*
num = 200
Npw2p = [0 for i in range(len(x))]
for i in range(len(x)):
    Npw2p[i] = round((num * (teor_p_i[i] - w[i]) ** 2) / teor_p_i[i], 5)
print("N(p*-w)^2:p*", Npw2p, "sum", round(sum(Npw2p), 5))

# Число интервалов по формуле Стерджеса
m = 1 + int(math.log2(num))

# Шаг
h = (selection[199] - selection[0]) / m

# проверка с помощью критерия хи-квадрат

hi_sq = round(sum(Npw2p), 5)
print("хи-квадрат ", hi_sq)

# число степеней свободы l
l = m - 2
alpha = 0.05  # уровень значимости

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

# print(crit_meaning_hi)

if hi_sq <= crit_meaning_hi:
    print(f"{hi_sq} <= {crit_meaning_hi} Гипотеза НЕ ПРОТИВОРЕЧИТ экспериментальным данным")
else:
    print(f"{hi_sq} > {crit_meaning_hi} Гипотеза ПРОТИВОРЕЧИТ экспериментальным данным")
