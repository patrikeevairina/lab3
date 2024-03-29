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

sel_2d = [first, second, third]

alpha = 0.05
pval_12 = round(scipy.stats.ttest_ind(first, second, equal_var=True).pvalue, 5)
pval_13 = round(scipy.stats.ttest_ind(first, third, equal_var=True).pvalue, 5)
pval_23 = round(scipy.stats.ttest_ind(second, third, equal_var=True).pvalue, 5)

# проверка выборок 1 и 2
if pval_12 > alpha:
    result_1_2 = "   Верна"
else:
    result_1_2 = "   Неверна"

# проверка выборок 1 и 3
if pval_13 > alpha:
    result_1_3 = "   Верна"
else:
    result_1_3 = "   Неверна"

# проверка выборок 2 и 3
if pval_23 > alpha:
    result_2_3 = "   Верна"
else:
    result_2_3 = "   Неверна"


print("столбцы    pval   alpha    Вывод")
print("(1,2)    ", pval_12, " ", alpha, result_1_2)
print("(1,3)    ", pval_13, " ", alpha, result_1_3)
print("(2,3)    ", pval_23, " ", alpha, result_2_3)