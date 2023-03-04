import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/ekaterina/github_repos/ITMO_STUDY/Zadachi_ITMO_teorver_statistica/Data_for_exercise_3_task_2.csv', names=['Y'])
print(df.info())
print()
print(df)


def exponential_smoothing(df, alpha):
    result = [df[0]]
    for index in range(1, len(df)):
        result.append(alpha * df[index] + (1 - alpha) * result[index - 1]) 
    return result
    
#Рассмотрим отдельно значения временного ряда и соответсвующие им временные метки.
# Преобразуем тип данных в массив <code>numpy</code>:
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

f_i = df['lin_trend']
y_avg = df['y'].mean()

R2 = 1 - ((y - f_i) ** 2).sum() / ((y - y_avg) ** 2).sum()
round(R2, 3)

# coefficient_of_dermination = r2_score(Y, p(X))
#Теперь проведем экспоненциальное сглаживание нашего временного ряда, используя [функцию](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ewm.html) 

# результат запишем в новый столбец ['y_exp_norm']
#df['Y_exp_norm'] = df['Y'].ewm(alpha=0.19, adjust=False).mean()
#print(df.head())
# Построим графики исходного и сглаженного рядов



