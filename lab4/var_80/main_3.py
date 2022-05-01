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

sel_2d = [first, second, third]

alpha = 0.05
pval_12 = round(scipy.stats.ttest_ind(first, second, equal_var=True).pvalue, 5)
pval_13 = round(scipy.stats.ttest_ind(first, third, equal_var=True).pvalue, 5)
pval_23 = round(scipy.stats.ttest_ind(second, third, equal_var=True).pvalue, 5)

# проверка выборок 1 и 2
if pval_12 <= alpha:
    result_1_2 = "   Верна"
else:
    result_1_2 = "   Неверна"

# проверка выборок 1 и 3
if pval_13 <= alpha:
    result_1_3 = "   Верна"
else:
    result_1_3 = "   Неверна"

# проверка выборок 2 и 3
if pval_23 <= alpha:
    result_2_3 = "   Верна"
else:
    result_2_3 = "   Неверна"

print("столбцы    pval   alpha    Вывод")
print("(1,2)    ", pval_12, " ", alpha, result_1_2)
print("(1,3)    ", pval_13, " ", alpha, result_1_3)
print("(2,3)    ", pval_23, " ", alpha, result_2_3)