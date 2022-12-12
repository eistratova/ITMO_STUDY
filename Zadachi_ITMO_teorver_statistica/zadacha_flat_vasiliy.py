from locale import normalize
import numpy as np
from operator import index
from tkinter import VERTICAL
import pandas as pd 
# Библиотеки для визуализации
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

path = '/Users/ekaterina/github_repos/ITMO_STUDY/task4_213602.csv'
data =  pd.read_csv(path, index_col = 'ID')
data.info()
print(data.head())

# Делаем нормировку
data = 1 - np.exp(1 - data/data.min())
print(data)

# Сщздфум доп колонку для суммирования наших нормированных значений
#data['SUM'] = 0

#Суммируем и сортируем
data['SUM'] = data['DISTANCE'] + data['STOP_COUNT'] + data['COST']
data.sort_values(by = ['SUM'])