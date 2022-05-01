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

pval = round(scipy.stats.f_oneway(first, second, third).pvalue, 5)

if pval > alpha:
    result = "   Верна"
else:
    result = "   Неверна"

print("pval      alpha    Вывод")
print(pval, " ", alpha, result)


