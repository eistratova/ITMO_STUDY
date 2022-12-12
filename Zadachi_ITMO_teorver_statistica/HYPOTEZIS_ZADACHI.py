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
df_aeroport = pd.read_csv('/Users/ekaterina/data4repos/hypothesis_4aeroport.csv', header=None)
print(df_aeroport)

df_aeroport = df_aeroport[0].round(3)
df_aeroport = df_aeroport.reset_index()
df_aeroport[0].index += 1
#mean = np.mean(df_aeroport)
#print(" Cреднее значение",mean)


n = 10  # объем выборки
aº = 26 # количество минут
e = 0.01 # уровень значимости
S = 6 # сигма в квадрате

#P = (n*0.5)*((mean*aº)/S)
#print ("P",P)
MEAN = df_aeroport[0].mean()
print('MEAN',df_aeroport[0].mean())

quant_0_5 = np.quantile(df_aeroport[0], 0.5)
P_руками = 3.162*((29.321-26)/2.449)

P_vib = (n**0.5)*((MEAN-aº)/(S**0.5))
print ("RUCAMI", P_руками)
print ("P_vib",P_vib)
print("C", t.ppf(1-(0.01/2), 9))
print("корень из n", n**0.5)
# If P(x)< c
print("If P(x)< c Гипотезу принимаем, если > - отвергаем ")



#print("Дисперсия смещенная", np.var(df_aeroport[1]))

#print("Дисперсия несмещенная", np.var(df_new[1], ddof=1))


#print("квантиль середина 0,5", np.quantile(df_new[1], 0.5))
#print("квантиль 0,25", np.quantile(df_new[1], 0.25))

'''
df_X = pd.read_csv('/Users/ekaterina/data4repos/Hipotezis_1_det_sad/Hyp_2_1_X.csv')
#print("X", df_X)

df_Y = pd.read_csv('/Users/ekaterina/data4repos/Hipotezis_1_det_sad/Hyp_2_1_Y.csv')
#print("Y", df_Y)

X = np.array([104.2, 123.5, 121.5, 112.6, 101.4, 98.7, 105.9, 103.6, 105.7, 102.7])
density_distribution_X = {i: np.array(X == i).sum() / X.size for i in np.unique(X)}
#print("Distribution_X", density_distribution_X)

Y = np.array([108.9, 110.3, 110.9, 113.6, 116.7])
density_distribution_Y = {i: np.array(Y == i).sum() / Y.size for i in np.unique(Y)}
##print("Distribution_Y", density_distribution_Y)

e=0.01

print("X", t.ppf(1-0.1, 10))

print("Y", t.ppf(1-0.1, 5))

#c = ((m*n/m+n)**0.5)*(Fnt - Gmt)
c = ((10*5/10+5))*0.05*0.7
print(c)
'''