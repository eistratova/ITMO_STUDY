from calendar import c
import pandas as pd
from scipy.stats import t
from matplotlib import pyplot as plt
import numpy as np
'''
Найти выборочные характеристики .
X_m^ S_0^2
2. Построить гистограмму ( равных интервалов) как оценку плотности распределения и на ее основе сделать 
предположение о типе распределения.
3. Опираясь на предположение о типе распределения, найти точечные оценки ø параметров распределения. 
Используйте метод максимального правдоподобия.
Напомним оценки параметров для некоторых распределений в случае использования ММП:


'''
df = pd.read_csv('/Users/ekaterina/data4repos/itog_sample_11 (1).csv', header=None)
df.index += 1
print(df)

MEAN = df.mean()
print('MEAN',MEAN)


S_2 = (np.var(df[0], ddof=1))
print("Дисперсия несмещенная", S_2)

"""
P_vib = (n**0.5)*(MEAN-a)/(S**0.5)

print ("P_vib",P_vib)
print("C", t.ppf(1-(e/2), 7))

print("If P(x)< c Гипотезу принимаем, если > - отвергаем ")
"""
# Строим Гистограмму
#plt.hist(df, bins=10)
plt.hist(df[0], bins=10)

#plt.show()
O_1 = MEAN-(3*S_2)**0.5
print("O_1", O_1)
O_2 = MEAN+(3*S_2)**0.5
print("O_2", O_2)

# Тета 1 и тета 2 - для равномерного распределения - берем минимум и максимум вариационного ряда

print("max", df[0].max())
print("min", df[0].min())