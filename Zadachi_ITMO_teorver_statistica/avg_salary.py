# Задача о зп 
'''
В прилагаемом файле представлена таблица о средней заработной плате в РФ по регионам 
на 1 января 2019 год по данным Росстата. Представим ситуацию, что из-за невнимательности операциониста, 
регионы: Республика Татарстан, Республика Марий Эл оказались не представлены в итоговой сводке. 
Роль невнимательного операциониста 
придется исполнить Вам (нужно удалить соответствующие строки), а далее работать уже с новой выборкой.

'''
# 
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
df = pd.read_excel('/Users/ekaterina/data4repos/AVG_salary2.xlsx', header=None)
print(df)
df.info()


# По условиям задачи нам необхоимо избавиться от 3 регионов
# для этого сначала удостоверимся-есть ли они там
mask = df[(df[0] == 'Республика Татарстан') | (df[0] == 'Республика Марий Эл')]
print(mask)

df_new = df[(df[0] != 'Республика Татарстан') & (df[0] != 'Республика Марий Эл')]
df_new


# Отсортируем данные по объему зп
df_new = df_new.sort_values(by=[1])
print(df_new)

df_new = df_new.reset_index()  #  Сбросим индекс
print(df_new)

#  У нас индекс начинается с 0, нам надо с 1, для этого повысим индекс
df_new.index += 1
print(df_new.head(20))
print("Инфо новая таблица без 2 регионов", df_new.info())

# Выводим требуемые элементы вариационного ряда
print("21, 22,77 элементы", df_new.loc[[21, 22, 77]])


print("Строим гистограмму", plt.hist(df_new[1], bins=10))
#plt.show()

print("Среднее", np.mean(df_new[1]))

print("Дисперсия смещенная", np.var(df_new[1]))
print("Дисперсия несмещенная", np.var(df_new[1], ddof=1))


print("квантиль середина 0,5", np.quantile(df_new[1], 0.5))
print("квантиль 0,25", np.quantile(df_new[1], 0.25, method='nearest'))      
print("quantil 0.75", np.quantile(df_new[1], 0.75, method='nearest'))
#n = 10
#aº = 26
#e = 0.01
#ß^2 = 6
#mean = np.mean(df_aeroport[1]
#a = n^0.5*(mean*aº/ß)
#print ("P",a)
#print("Среднее", np.mean(df_aeroport[1]))

#print("C", t.ppf(1-0.01/2, 9))

# If P(x)< c
#print("Гипотезу принимаем")
