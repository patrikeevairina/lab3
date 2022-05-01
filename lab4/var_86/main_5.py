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
first = [8.98916, 12.74455, 7.54412, 7.14413, 5.67097, 11.95328,
         8.65550, 7.89505, 12.72736, 13.46213, 8.66133, 6.77688,
         9.73556, 15.18698, 4.38339, 11.76695]
# second ksi
second = [12.11567, 9.91673, 7.23929, 12.86704, 7.02257, 9.00369,
          4.69718, 12.07695, 7.30159, 4.80794, 12.67437, 8.61648,
          6.82806, 11.53224, 11.06643, 2.19140]
# third ksi
third = [1.62073, 6.44220, 6.21874, 11.27553, 9.41593, 12.11049,
         12.98772, 7.60639, 10.80071, 10.35897, 9.74924, 11.85632,
         11.94754, 8.48395, 7.89188, 6.74048]

sel_2d = [first, second, third]

alpha = 0.05

pval = round(scipy.stats.f_oneway(first, second, third).pvalue, 5)

if pval <= alpha:
    result = "   Верна"
else:
    result = "   Неверна"


print("pval      alpha    Вывод")
print(pval, " ", alpha, result)


