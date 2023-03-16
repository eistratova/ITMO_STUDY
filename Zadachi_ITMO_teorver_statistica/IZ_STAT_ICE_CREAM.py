'''
Производитель мороженого утверждает, что вес одного эскимо составляет 102  грамм. 
Из очередной поставки в магазин случайно выбрано и взвешено 8 эскимо. 
Считается, что масса эскимо имеет нормальное распределение. 
Справедливо ли заявление продавца, если уровень значимости 0.10.
Введите оценку среднеквадратического отклонения S_0:
Введите выборочное среднее :
Введите модуль функции отклонения |P(x)| :
Ответьте на вопрос, верна ли гипотеза:
'''

from calendar import c
import pandas as pd
from scipy.stats import t, norm
from matplotlib import pyplot as plt
import numpy as np

df_ice_cream = pd.read_csv('/Users/ekaterina/github_repos/ITMO_STUDY/Zadachi_ITMO_teorver_statistica/Hypothesis_1_7.csv', header=None)
df_ice_cream.index += 1

print(df_ice_cream)

n = 8  # объем выборки
a = 102 # количество грамм
e = 0.010 # уровень значимости
MEAN = df_ice_cream.mean()
print('MEAN',MEAN)


S = (np.var(df_ice_cream[0], ddof=1))**0.5
print("Дисперсия несмещенная", S)


Po_X = (n**0.5)*(MEAN-a)/(S)

print ("Po_X",Po_X)
print("C", norm.ppf(1-e/2))

print("If Po_X < C Гипотезу принимаем, если > - отвергаем. Cогласно нашим результатам гипотеза что вес одного эскимо составляет 102  грамм не отвергаеся ")
