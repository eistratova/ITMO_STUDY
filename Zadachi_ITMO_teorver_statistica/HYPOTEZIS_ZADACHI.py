'''
Представитель аэропорта на встрече с руководством авиакомпании заявил, 
что среднее время подготовки самолета к вылету составляет а_0=26 минут. 
В авиакомпании решили проанализировать, не ошибается ли представитель аэропорта
и решили рассмотреть последние т=10 обслуживаний. Считается, что время обслуживания 
распределено нормально, причем дисперсия известна и равна S^2=6. 
Справедливо ли заявление представителя аэропорта, если уровень значимости e = 0.01. 
Ответьте на вопрос, верна ли гипотеза?

Введите выборочное среднее, Введите модуль функции отклонения Po(X) :
'''

from calendar import c
import pandas as pd
from scipy.stats import norm
from matplotlib import pyplot as plt
import numpy as np

df_aeroport = pd.read_csv('/Users/ekaterina/github_repos/ITMO_STUDY/Zadachi_ITMO_teorver_statistica/hypothesis_4.csv', header=None)
print(df_aeroport)

df_aeroport = df_aeroport[0].round(3)
df_aeroport = df_aeroport.reset_index()
df_aeroport[0].index += 1

n = 10  # объем выборки
aº = 26 # количество минут
e = 0.01 # уровень значимости
S = 6 # сигма в квадрате


X_m = df_aeroport[0].mean()
print('Cреднее X_m',df_aeroport[0].mean())

# Формула для рассчета Ро
# Po = (n**0.5)*((mean*aº)/S)
Po_vib = (n**0.5)*((X_m-aº)/(S**0.5))

print ("P_vib",Po_vib)
print("C", norm.ppf(1-e/2), 10)

print("If Po(x)< c Гипотезу принимаем, если > - отвергаем: Po_vib, C ",Po_vib, norm.ppf(1-e/2), 10 )
print("If Po(x)< c Гипотезу то гипотеза о том, что среднее время обслуживания составляет 26 минут, не находит подтверждения-отвергаем, т к Ро > C")
'''
какие-то след задачи
df = pd.read_csv('/Users/ekaterina/data4repos/hypothesis_2.csv')
#print(df)

df.index += 1
print(df.head(20))

print(t.ppf(1-0.05/2, 99))
'''
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