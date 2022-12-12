import math

x = 1
a = 1 + x + (x**2/math.factorial(2))+(x**3/math.factorial(3)) + (x**4/math.factorial(4)) + (x**5/math.factorial(5))
print(a)

"""
import datetime
import pandas as pd
import glob # Библиотека для получения списка файлов
import os
import stat
from os import listdir # Библиотека для получения списка файлов
from os.path import isfile, join
from datetime import time

path = '/Users/ekaterina/data4repos/task1_4_5_391050.csv'
df = pd.read_csv(path,  index_col= 0)
df.info()
print(df)

df['Рейс 1'] = pd.to_datetime(df['Рейс 1'])
df['Рейс 2'] = pd.to_datetime(df['Рейс 2'])
df['Рейс 3'] = pd.to_datetime(df['Рейс 3'])
#df['Рейс 4'] = pd.to_datetime(df['Рейс 4'])

#df.info()
#df['Рейс 4'] = pd.to_numeric(df['Рейс 4'])

a=datetime.datetime(2014, 2, 3, 11, 14, 20)

b=datetime.datetime(2014, 2, 3, 11, 06, 10)
print(b - a)
'''
"""