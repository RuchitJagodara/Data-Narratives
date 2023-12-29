# PROFESSORS MAY BE GETTING MORE SALARY IF THEY HAVE PHD QUALIFICATIONS

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



data1=pd.read_csv('http://lib.stat.cmu.edu/datasets/colleges/aaup.data',names=list(range(17)))
data2=pd.read_csv('http://lib.stat.cmu.edu/datasets/colleges/usnews.data',names=list(range(35)))

data1[17]=data2[29]
data=data1[data1[7] != '*']
data=data1[data1[17] != '*']

data[17]=pd.to_numeric(data[17])
data[7]=pd.to_numeric(data[7])

data=data.sort_values(by=[17])
plt.plot(data[17],data[7])
plt.xlabel('Percentage of PhD qualified professors')
plt.ylabel('Average salary')
plt.show()
print(len(data[17]))
z=[]
i=0

while i<len(data[17])-1:
    z+=[np.mean((data[7])[i:i+11])]*11
    i+=11

plt.plot(data[17],z)
plt.xlabel('Percentage of PhD qualified professors')
plt.ylabel('Average salary')
plt.show()
