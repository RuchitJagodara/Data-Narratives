# in which type of institution overall cost for a student is low? It should be public.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('http://lib.stat.cmu.edu/datasets/colleges/usnews.data',names=list(range(35)))

data=data[data[23] != '*']
data=data[data[26] != '*']
data=data[data[28] != '*']
data=data[data[27] != '*']



data[23]=pd.to_numeric(data[23])
data[26]=pd.to_numeric(data[26])
data[27]=pd.to_numeric(data[27])
data[28]=pd.to_numeric(data[28])


data[35]=data[23]+data[26]+data[27]+data[28]


a=data[data[3]==1]
a1=np.mean(data[23])
a2=np.mean(data[26])
a3=np.mean(data[27])
a4=np.mean(data[28])

plt.pie([a1,a2,a3,a4],labels=['Room and board costs','Additional fees','Estimated book costs','Estimated personal spending'])
plt.ylabel('Money spent behind different things')
plt.show()

print(np.max(a[23]),np.max(a[26]),np.max(a[27]),np.max(a[28]),sep='\n')

b=data[data[3]==2]
b1=np.mean(data[23])
b2=np.mean(data[26])
b3=np.mean(data[27])
b4=np.mean(data[28])

plt.pie([b1,b2,b3,b4],labels=['Room and board costs','Additional fees','Estimated book costs','Estimated personal spending'])
plt.ylabel('Money spent behind different things')
plt.show()

print(np.max(b[23]),np.max(b[26]),np.max(b[27]),np.max(b[28]),sep='\n',end='\n\n\n\n')
