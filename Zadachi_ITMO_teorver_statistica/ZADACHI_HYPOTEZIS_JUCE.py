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
df_juce = pd.read_csv('/Users/ekaterina/data4repos/hypothesis_3_Juce.csv', header=None)
print(df_juce)

n = 20  # объем выборки
a = 1000 # количество минут
e = 0.05 # уровень значимости

MEAN = df_juce.mean()
print('MEAN',df_juce.mean())


S = (np.var(df_juce[0], ddof=1))**0.5
print("Дисперсия несмещенная", S)
# P_руками = 3.162*((29.321-26)/2.449)

P_vib = ((n**0.5)*(MEAN-a))/(S**0.5)
#print ("RUCAMI", P_руками)
print ("P_vib",P_vib)
print("C", t.ppf(1-(0.05/2), 19))

print("If P(x)< c Гипотезу принимаем, если > - отвергаем ")




