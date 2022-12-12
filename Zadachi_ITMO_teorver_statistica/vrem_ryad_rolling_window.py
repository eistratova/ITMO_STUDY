# Считаем скользящее среднее (окно 3 и 7) SMA

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

series = pd.read_csv('ITMO_STUDY/quiz_5_2_2_data.csv',index_col = [0], names=['Y'])
# series = series.set_index(0)
print(series.info())
print('Исходный временной ряд')
print(series)

#updating our dataFrame to have only
# one column 'Close' as rest all columns
# are of no use for us at the moment
# using .to_frame() to convert pandas series
# into dataframe.
smothing = series['Y'].to_frame()
 
# calculating simple moving average
# using .rolling(window).mean() ,
# with window size = 3
smothing['SMA3'] = series['Y'].rolling(3).mean()

smothing['SMA3_w7'] = series['Y'].rolling(7).mean()
# removing all the NULL values using -  в нашем задании их удалять не нужно
# dropna() method
#smothing.dropna(inplace=True)
 
# printing Dataframe
print(smothing)
# Построим графики исходного и сглаженного рядов

plt.figure(figsize=(20, 8))
plt.plot('Y', data = smothing)
plt.plot('SMA3', data = smothing)
plt.xlabel('Time step')
plt.ylabel('Y')
#plt.show()



# ВЫведем значение 5
print('ВЫведем значение сглаженное', 5)
print(smothing.loc[[5]])

plt.figure(figsize=(20, 8))
plt.plot('Y', data = smothing)
plt.plot('SMA3_w7', data = smothing)
plt.xlabel('Time step')
plt.ylabel('Y')
plt.show()

