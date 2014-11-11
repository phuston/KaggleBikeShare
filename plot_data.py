import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import csv
import datetime


data = csv.reader(open('train.csv'), delimiter=',')
data.next()
data.next()

dt = []
ssn = []
hday = []
wkd = []
wtr = []
tmp = []
atmp = []
hum = []
wspd = []
cas = []
reg = []
cnt = []


for row in data:
	dt.append(datetime.datetime.strptime(row[0],'%Y-%m-%d %H:%M:%S'))
	ssn.append(row[1])
	hday.append(row[2])
	wkd.append(row[3])
	wtr.append(row[4])
	tmp.append(row[5])
	atmp.append(row[6])
	hum.append(row[7])
	wspd.append(row[8])
	cas.append(row[9])
	reg.append(row[10])
	cnt.append(row[11])

all_features = [dt, ssn, hday, wkd, wtr, tmp, atmp, hum, wspd, cas, reg, cnt]

work_fts = []
non_work_fts = []

for i in range(len(all_features)): #Do something about splitting between workdays and non-workdays through multiplications
	work_fts[i] 