# Which state has highest number of institutions? In which state, professors are given more average salary and average compensation?  At which extent these two trends are related?

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data=pd.read_csv('http://lib.stat.cmu.edu/datasets/colleges/aaup.data',names=list(range(17)))
data=data[data[7] != '*']
data=data[data[11] != '*']
data['n']=1
pd.to_numeric(data[7])
pd.to_numeric(data[11])


data[2].value_counts()[0:10].plot(kind='barh')
plt.xlabel('Total number of institutes')
plt.ylabel('Pstal code of state')
plt.show()

b=data.groupby([2])
c=(b.sum())
c=c.reset_index()
c['new']=c[7]/c['n']
c=c.sort_values(by=['new'],ascending=False)[0:10]



plt.bar(c[2],c['new'])
plt.xlabel('postal code of state')
plt.ylabel('Average salary')
plt.show()

c['new2']=c[11]/c['n']
c=c.sort_values(by=['new2'],ascending=False)[0:10]



plt.bar(c[2],c['new2'])
plt.xlabel('postal code of state')
plt.ylabel('Average compensation')
plt.show()


print(np.corrcoef(c['new2'],c['new']))
