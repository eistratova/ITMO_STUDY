# Коэф-т сглаживания с пом экспоненциальной ф-ии
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/ekaterina/github_repos/ITMO_STUDY/ datasets/quiz_5_2_3_data.csv', index_col = [0], names=['Y'])
print(df.info())
print()
print(df)


def exponential_smoothing(df, alpha):
    result = [df[0]]
    for index in range(1, len(df)):
        result.append(alpha * df[index] + (1 - alpha) * result[index - 1]) 
    return result

# Определяем коэффициенты сглаживания с пом эксп функции с коэф-ми 0.1 и 0.3

df['y_exp_norm_0.1'] = df['Y'].ewm(alpha=0.1, adjust=False).mean()
df['y_exp_norm_0.3'] = df['Y'].ewm(alpha=0.3, adjust=False).mean()
print("Коэффициенты сглаживания с пом эксп функции с коэф-ми 0.1 и 0.3", df)


# ВЫведем значение 5
print('ВЫведем значение сглаженное и начальное значение', 5)
print(df.loc[[5]])

# ВЫведем только сглаженное значение 5
print('ВЫведем только сглаженное значение', 5)
print(df['y_exp_norm_0.3'].loc[[5]])


plt.figure(figsize=(20, 8)) 
plt.plot('Y', data = df)

#plt.plot('Y_exp_norm_user', data = df) original
plt.plot('y_exp_norm_0.3', data = df)
plt.xlabel('Time step')
plt.ylabel('Y')
plt.show()
'''


# ВЫведем значение только сглаженное значение 5
print('ВЫведем значение только сглаженное значение', 5)
print(df['R_exp_norm_user'].loc[[5]])


#  округлим до сотых
R5 = df['R_exp_norm_user'].loc[[5]]
round(R5, 2)



plt.figure(figsize=(20, 8))
plt.plot('R', data = df)
plt.plot('R_exp_norm', data = df)
plt.plot('R_exp_norm_user', data = df)
plt.xlabel('Time step')
plt.ylabel('R')
plt.show()


#Рассмотрим отдельно значения временного ряда и соответсвующие им временные метки.
# Преобразуем тип данных в массив <code>numpy</code>:
import numpy as np
X = df.index.to_numpy()
y = df['R'].to_numpy()
print('Значения временного ряда и соответсвующие им временные метки',X)

# Найдем уравнение линейного тренда, используя функцию <code>polyfit</code>

poly = np.polyfit(X, y, 1)
print('', poly)

a = poly[0]
b = poly[1]

# Найдем значения ряда, используя уравнение тренда

x = np.arange(1, 101)
df['lin_trend'] = a * x + b
#  Строим график тренда

plt.figure(figsize=(20, 8))
plt.plot('y', data=df)
plt.plot('lin_trend', data=df)
plt.xlabel('Time step')
plt.ylabel('y')
plt.show()

# Вычислим коэффициент [детерминации]
# (http://statistica.ru/theory/koeffitsient-determinatsii-i-lineynaya-regressiya/)

## $R^{2}=1-\frac{\sum\limits_{i=1}^{n}\left(y_{i}-f_{i}\right)^{2}}{\sum\limits_{i=1}^{n}\left(y_{i}-y_{\mathrm{avg}}\right)^{2}}$


f_i = df['lin_trend']
y_avg = df['y'].mean()

R2 = 1 - ((y - f_i) ** 2).sum() / ((y - y_avg) ** 2).sum()
round(R2, 3)

# Спрогнозируем 101 член
y_101 = a * 101 + b
round(y_101, 0)

'''
# Определяем коэффициенты сглаживания с пом эксп функции с коэф-ми 0.1 и 0.3




'''
df['y_exp_norm_0.1'] = df['Y'].ewm(alpha=0.1, adjust=False).mean()
df['y_exp_norm_0.3'] = df['Y'].ewm(alpha=0.3, adjust=False).mean()
print("Коэффициенты сглаживания с пом эксп функции с коэф-ми 0.1 и 0.3", df)

# ВЫведем значение 5
print('ВЫведем значение сглаженное и начальное значение', 5)
print(df.loc[[5]])

# ВЫведем значение только сглаженное значение 5
print('ВЫведем значение только сглаженное значение', 5)
print(df['y_exp_norm_user'].loc[[5]])



##### SMA

def SMA_smoothing(series, width):
    result = []
    k = (width - 1) // 2
    for index in range(k, len(series) - k):
        result.append(np.sum(series[index - k : index + k + 1])/width) 
    return result

series = pd.read_csv('ITMO_STUDY/quiz_5_2_2_data.csv', !!!!! заменить источник!!!
                     header=None)
series = series.set_index(0)

print(series.head())

smoothed = pd.DataFrame(SMA_smoothing(series[1].to_list(),3))
smoothed.index += 1
smoothed.head()

smoothed = pd.DataFrame(SMA_smoothing(series[1].to_list(),7))
smoothed.index += 1
smoothed.head()

smoothed = series.rolling(window=7).mean()
smoothed
'''


