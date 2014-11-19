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
	ssn.append(int(row[1]))
	hday.append(int(row[2]))
	wkd.append(int(row[3]))
	wtr.append(int(row[4]))
	tmp.append(float(row[5]))
	atmp.append(float(row[6]))
	hum.append(int(row[7]))
	wspd.append(float(row[8]))
	cas.append(int(row[9]))
	reg.append(int(row[10]))
	cnt.append(int(row[11]))

all_features = np.array([dt, ssn, hday, wkd, wtr, tmp, atmp, hum, wspd, cas, reg, cnt])

work_fts = np.arange(12)
non_work_fts = np.arange(12)

for i in range(len(wkd)):
    if wkd[i] == 1:
        work_fts = np.vstack((work_fts,all_features[:,i].reshape(1,12)))
    if wkd[i] == 0:
        non_work_fts = np.vstack((non_work_fts,all_features[:,i].reshape(1,12)))

print(work_fts)


plt.plot(work_fts[:,11])
plt.show()
