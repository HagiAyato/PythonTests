import csv
import numpy as np
import copy
import time

with open('10000data.csv') as f:
	reader = csv.reader(f)
	list = [row for row in reader]
listHeader = list.pop(0)

listHeader.extend(['average'])
# 平均(計測用)
start = time.time()
for i in range(10):
	list2 = copy.deepcopy(list)
	for idx, row in enumerate(list2):
		row.extend('0')
		row[7] = str((float(row[2]) + float(row[3]) + float(row[4]) + float(row[5]) + float(row[6]))/5.0)
elapsed_time = time.time() - start
print ("平均処理10回平均所要時間:{0}".format(elapsed_time/10) + "[sec]")

# 平均
for idx, row in enumerate(list):
	row.extend('0')
	row[7] = str((float(row[2]) + float(row[3]) + float(row[4]) + float(row[5]) + float(row[6]))/5.0)

# ソート(計測用)
start = time.time()
for i in range(10):
	list2 = sorted(list, key=lambda x: x[7], reverse=True)
elapsed_time = time.time() - start
print ("ソート10回平均所要時間:{0}".format(elapsed_time/10) + "[sec]")

# ソート
for i in range(10):
	list = sorted(list, key=lambda x: x[7], reverse=True)

# 絞り込み(計測用)
start = time.time()
for i in range(10):
	list2 = []
	for idx, row in enumerate(list):
		if 50 <= float(row[7]):
			list2.append(row)
elapsed_time = time.time() - start
print ("絞り込み10回平均所要時間:{0}".format(elapsed_time/10) + "[sec]")