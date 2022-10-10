import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

series = pd.read_csv('ITMO_STUDY/quiz_5_2_2_data.csv',index_col = [0], names=['Y'])
# series = series.set_index(0)
print(series.info())
print('Исходный временной ряд')
print(series)

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


# Построим графики исходного и сглаженного рядов
'''
plt.figure(figsize=(20, 8))
plt.plot('Y', data = df)
plt.plot('smoothed', data = df)
plt.xlabel('Time step')
plt.ylabel('Y')
#plt.show()


# ВЫведем значение 5
print('ВЫведем значение сглаженное и начальное значение', 5)
print(df.loc[[5]])

#smoothed = series.rolling(window=7).mean()
#smoothed
'''