from calendar import c
import pandas as pd
from scipy.stats import t
from matplotlib import pyplot as plt
import numpy as np
'''
df = pd.read_csv('/Users/ekaterina/data4repos/hypothesis_2.csv')
#print(df)

df.index += 1
print(df.head(20))

print(t.ppf(1-0.05/2, 99))
'''
df_ice_cream = pd.read_csv('/Users/ekaterina/data4repos/Hypothesis_1_7_ICE_CREAM.csv', header=None)
df_ice_cream.index += 1

print(df_ice_cream)

n = 8  # объем выборки
a = 102 # количество грамм
e = 0.010 # уровень значимости
MEAN = df_ice_cream.mean()
print('MEAN',MEAN)


S = (np.var(df_ice_cream[0], ddof=1))**0.5
print("Дисперсия несмещенная", S)


P_vib = (n**0.5)*(MEAN-a)/(S**0.5)

print ("P_vib",P_vib)
print("C", t.ppf(1-(e/2), 7))

print("If P(x)< c Гипотезу принимаем, если > - отвергаем ")
