import pandas as pd
import time

df = pd.read_csv('10000data.csv', index_col=0)

# 平均
start = time.time()
for i in range(10):
	# df['average'] = (df['subjectA'] + df['subjectB'] + df['subjectC'] + df['subjectD'] + df['subjectE'])/5
	df['average'] = (df[['subjectA', 'subjectB', 'subjectC', 'subjectD', 'subjectE']].sum(axis=1))/5
elapsed_time = time.time() - start
print ("平均処理10回平均所要時間:{0}".format(elapsed_time/10) + "[sec]")

# ソート
start = time.time()
for i in range(10):
	df2 = df.copy()
	df2.sort_values('average', ascending=False)
elapsed_time = time.time() - start
print ("ソート10回平均所要時間:{0}".format(elapsed_time/10) + "[sec]")
df = df2.copy()

# 絞り込み
start = time.time()
for i in range(10):
	df2 = df[50 <= df['average']]
elapsed_time = time.time() - start
print ("絞り込み10回平均所要時間:{0}".format(elapsed_time/10) + "[sec]")

# 平均 iat
start = time.time()
for i in range(10):
	for idx in range(len(df)):
		df.iat[idx, 6] = str((float(df.iat[idx, 1]) + float(df.iat[idx, 2])
			+ float(df.iat[idx, 3]) + float(df.iat[idx, 4]) + float(df.iat[idx, 5])/5.0))
elapsed_time = time.time() - start
print ("平均for10回平均所要時間:{0}".format(elapsed_time/10) + "[sec]")