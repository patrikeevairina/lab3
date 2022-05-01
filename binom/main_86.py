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
        M += x_i[i]*w_i[i]
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
#print("---------------Выборка неупорядоченная---------------")
_n = 5
selection = [4, 5, 4, 4, 2, 5, 4, 4, 4, 2,
            4, 3, 4, 4, 5, 4, 3, 2, 5, 4,
            4, 4, 4, 3, 4, 4, 3, 3, 4, 4,
            4, 4, 3, 5, 3, 5, 5, 5, 3, 4,
            5, 5, 4, 4, 4, 3, 3, 3, 4, 3,
            5, 3, 4, 3, 4, 4, 2, 4, 3, 2,
            4, 5, 3, 5, 3, 3, 5, 5, 4, 5,
            4, 3, 4, 4, 5, 3, 5, 4, 4, 3,
            5, 4, 3, 4, 1, 4, 4, 3, 2, 4,
            3, 4, 4, 4, 4, 3, 3, 4, 5, 3,
            4, 3, 4, 4, 5, 4, 3, 3, 5, 4,
            4, 3, 4, 1, 4, 4, 4, 3, 4, 1,
            5, 4, 4, 4, 5, 4, 4, 4, 5, 3,
            4, 4, 4, 4, 5, 3, 3, 5, 3, 3,
            4, 3, 4, 4, 4, 2, 4, 4, 2, 3,
            5, 4, 4, 1, 3, 5, 4, 5, 4, 4,
            5, 4, 5, 4, 4, 4, 4, 4, 4, 5,
            4, 5, 5, 3, 4, 4, 4, 2, 5, 5,
            4, 3, 3, 2, 5, 4, 3, 4, 4, 3,
            4, 4, 3, 5, 3, 4, 5, 2, 4, 5]
print(selection)

print("---------------Выборка упорядоченная---------------")
selection.sort()
print(selection)

print("Table 1.1")
#x -- значения без повторений
x = list(np.unique(selection))
print("x", x)

#n -- количество различных значений
count = Counter(selection)
n = list(count.values())
print("n", n, "sum n", sum(n))

#w -- относительные частоты
w = [0 for i in range(len(count))]
for i in range(len(count)):
    w[i] = n[i] / 200.0
print("w", w, "sum w", round(sum(w), 5))

#Мат ожидание
_m = 0.0
for i in range(len(x)):
    _m += x[i]*w[i]
#print("M", _m)

#оценка параметра р
#насколько я поняла, вывелось из M=n*p => p = M/n
_p = _m/_n
#print("оценка параметра р", _p)

#отрисовка полигонов по отн частотам и по вероятности p и параметру n
print_polygons(x, w, _n, _p)

#таблица 1.2
print("Table 1.2")
print("x", x)
print("w", w, "sum w", round(sum(w), 5))
#p*
teor_p_i = np.zeros(len(x))
for i in range(len(x)):
    teor_p_i[i] = round((math.comb(_n, x[i]) * (_p ** x[i]) * ((1 - _p) ** (_n - x[i]))), 5)
print("p*", teor_p_i, "sum", round(sum(teor_p_i), 5))

#|w_i - p*_i|
print("|w_i - p*_i|", abs(teor_p_i - w), "max", max(abs(teor_p_i - w)))

#N(p*-w)^2:p*
num = 200
Npw2p = [0 for i in range(len(x))]
for i in range(len(x)):
    Npw2p[i] = round((num * (teor_p_i[i] - w[i])**2) / teor_p_i[i], 5)
print("N(p*-w)^2:p*", Npw2p, "sum", round(sum(Npw2p), 5))

# Число интервалов
m = len(n)

# Шаг
h = (selection[199] - selection[0]) / m

#проверка с помощью критерия хи-квадрат

hi_sq = round(sum(Npw2p), 5)
print("хи-квадрат ", hi_sq)

# число степеней свободы l
l = m - 2
alpha = 0.05  # уровень значимости

if l == 3:
    crit_meaning_hi = 7.8
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

#print(crit_meaning_hi)

if hi_sq <= crit_meaning_hi:
    print(f"{hi_sq} <= {crit_meaning_hi} Гипотеза НЕ ПРОТИВОРЕЧИТ экспериментальным данным")
else:
    print(f"{hi_sq} > {crit_meaning_hi} Гипотеза ПРОТИВОРЕЧИТ экспериментальным данным")


# Группированная выборка
# Число интервалов по формуле Стерджеса
m = 1 + int(math.log2(num))

# Шаг
h = (selection[199] - selection[0]) / m

# a_i
crit_a = [i for i in range(m+1)]
crit_a[0] = x[0]
for i in range(1, m+1):
    crit_a[i] = crit_a[i - 1] + h
print("crit a", crit_a)

# n_i
crit_n = [0 for i in range(m)]
i = 0
while crit_a[0] <= x[i] <= crit_a[1] and i < len(x):
    crit_n[0] += n[i]
    i += 1
for i in range(1, m):
    for j in range(len(x)):
        if crit_a[i] < x[j] <= crit_a[i+1]:
            crit_n[i] += n[j]
print("crit n_i", crit_n, "sum", sum(crit_n))

# w_i
crit_w = [0 for i in range(m)]
for i in range(m):
    crit_w[i] = crit_n[i]/num
print("crit w_i", crit_w, "sum", sum(crit_w))

# x*
crit_x_star = [(crit_a[i]+crit_a[i-1])/2 for i in range(1, m+1)]
print("crit x*", crit_x_star)

#M
crit_m = round(sum([crit_w[i]*crit_x_star[i] for i in range(m)]), 5)
print("crit M", crit_m)

#sigma
crit_sigma_2 = sum([crit_w[i]*(crit_x_star[i] **2) for i in range(m)]) - crit_m ** 2 - (h ** 2) / 12
crit_sigma = round(pow(crit_sigma_2, 0.5), 5)
print("crit dispersion", crit_sigma)

# crit p*
crit_p_star = [0 for i in range(m)]
crit_p_star[0] = round(scipy.stats.norm.cdf((crit_a[1] - crit_m) / crit_sigma), 5)
crit_p_star[m-1] = round(1.0 - scipy.stats.norm.cdf((crit_a[m-1] - crit_m) / crit_sigma), 5)
for i in range(1, m-1):
    crit_p_star[i] = round(scipy.stats.norm.cdf((crit_a[i+1] - crit_m) / crit_sigma) \
                  - scipy.stats.norm.cdf((crit_a[i] - crit_m) / crit_sigma), 5)
print("crit p*", crit_p_star, "sum", sum(crit_p_star))

# hi**2
hi_sq = round(sum([((crit_n[i] - num * crit_p_star[i]) ** 2) / (num * crit_p_star[i]) for i in range(m)]), 5)