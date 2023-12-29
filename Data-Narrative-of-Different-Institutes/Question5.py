#  FIND THE PROBABILITY THAT IF I CHOOSE A PUBLIC INSTITUTE, IT TURNS OUT TO BE TYPE I. ALSO, FIND THE PROBABILITY IF PRIVATE INSTITUTE WAS SELECTED.
from pandas.plotting import table
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data1=pd.read_csv('http://lib.stat.cmu.edu/datasets/colleges/aaup.data',names=list(range(17)))
data2=pd.read_csv('http://lib.stat.cmu.edu/datasets/colleges/usnews.data',names=list(range(35)))

data1[17]=data2[3]

data3=data1.sort_values(by=7,ascending=True)[0:10]
# plt.barh(data3[1],data3[7])
# plt.show()


# data3=pd.DataFrame(data3)

# from IPython.display import display

# display(data3)

d=data1[data1[17]==1]
p1=len(d)/len(data2)

p1a=len(d[d[3]=='I'])/len(d)
p1b=len(d[d[3]=='IIA'])/len(d)
p1c=len(d[d[3]=='IIIB'])/len(d)


# d[3].value_counts().plot(kind='pie')
# plt.ylabel('Type')
# plt.show()


dd=data1[data1[17]==2]
p2=len(dd)/len(data2)

p2a=len(dd[dd[3]=='I'])/len(dd)
p2b=len(dd[dd[3]=='IIA'])/len(dd)
p2c=len(dd[dd[3]=='IIIB'])/len(dd)

# dd[3].value_counts().plot(kind='pie')
# plt.ylabel('Type')
# plt.show()



print(p1)
print(p1a)
print(p1b)
print(p1c)
print(p2)
print(p2a)
print(p2b)
print(p2c)
