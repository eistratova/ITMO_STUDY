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
