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
first = [12.17702, 14.01000, 12.09198, 11.18424, 11.82169, 12.18678, 9.17935,
         10.65043, 7.17028, 10.84520, 8.46016, 8.84723, 9.28104, 8.58507,
         8.56640, 7.99559]
# second ksi
second = [5.93275, 9.89971, 9.91496, 6.28285, 10.52099, 12.62202, 12.55684,
          7.37434, 6.93578, 15.83671, 12.01177, 9.66646, 4.43970, 11.35868,
          8.32329, 10.09010]
# third ksi
third = [9.84826, 5.14551, 12.46817, 11.83668, 11.19952, 5.17841, 10.08253,
         14.44858, 10.13184, 6.25333, 11.63221, 5.40682, 9.21548, 12.85413,
         9.21191, 7.85235]

sel_2d = [first, second, third]

alpha = 0.05

pval = round(scipy.stats.bartlett(first, second, third).pvalue, 5)

if pval < alpha:
    result = "   неверна"
else:
    result = "   верна"


print("pval      alpha    Вывод")
print(pval, " ", alpha, result)


