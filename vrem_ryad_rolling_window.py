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
# with window size = 30
smothing['SMA3'] = series['Y'].rolling(3).mean()
 
# removing all the NULL values using
# dropna() method
smothing.dropna(inplace=True)
 
# printing Dataframe
print(smothing)

'''

# Пишем функцию сглаживания
def SMA_smoothing(series, width):
    result = []
    k = (width - 1) // 2
    for index in range(k, len(series) - k):
        result.append(np.sum(series[index - k : index + k + 1])/width) 
    return result


smoothed = pd.DataFrame(SMA_smoothing(series[1].to_list(),3))
smoothed.index += 1
print('Сглаженный временной ряд-3',smoothed.head())

'''
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

'''
#smoothed = series.rolling(window=7).mean()
#smoothed
'''