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