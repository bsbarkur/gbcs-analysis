import csv
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from lifelines.estimation import KaplanMeierFitter

# Data set can be downloaded from:
# http://www.umass.edu/statdata/statdata/data/gbcs.txt

resultFile = open("output.csv",'wb')
wr = csv.writer(resultFile, dialect='excel')

with open('gbcs.csv') as f:
	reader = csv.reader(f)
	for row in reader:
		if row[14] == "survtime":
			print row
			wr.writerow(row)
			continue
		else:
			rowitem = int(row[14])/365
			row[14] = str(rowitem)
			wr.writerow(row)

data = pd.read_csv('output.csv', header = 0, index_col=0 )
kmf = KaplanMeierFitter()

T = data["survtime"] #measure in years
C = data["censdead"]

ax = plt.subplot(111)
plt.xlabel("Years")
plt.ylabel("Percentage of Survival")
kmf.fit(T, label='KM-estimate', left_censorship=False)

ax1 = kmf.plot(ax=ax, c="#A60628", ci_force_lines=True)

ax1.get_figure().savefig("gbcs.png")



