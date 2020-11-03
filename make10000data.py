import pandas as pd
from numpy.random import *

print("make10000data START")

df = pd.DataFrame(columns=['studentNo', 'subjectA', 'subjectB', 'subjectC', 'subjectD', 'subjectE'])
dfcol = df.columns

for idx in range(10000):
	studentNo = str(idx + 1)
	df = df.append(pd.Series([studentNo, randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)], index = dfcol, name = studentNo))
	if(idx % 100 == 0):
		print(str(idx) + "件目完了")
df.to_csv('10000data.csv')

print("make10000data END")