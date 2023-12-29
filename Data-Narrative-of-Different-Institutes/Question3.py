# WHICH TYPE OF INSTITUTE IS PAYING MORE MONEY TO THEIR STAFF? COMPARE THE HIGHEST AVERAGE SALARY PAID IN EACH TYPE OF INSTITUTE.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('http://lib.stat.cmu.edu/datasets/colleges/aaup.data',names=list(range(17)))

d=data[data[7]!='*']
d=d[d[16]!='*']

d[7]=pd.to_numeric(d[7])
d[16]=pd.to_numeric(d[16])

d[17]=d[7]*d[16]    

cc=d.groupby([3]).sum().plot(kind='pie',y=17)
plt.ylabel('Total money paid')
plt.show()

d=d.sort_values(by=[7],ascending=False)

dd=d[d[3]=='I'].head(3)
plt.bar(dd[1],dd[7])
plt.xlabel('Name of institute')
plt.ylabel('Average salary')
plt.show()

dd=d[d[3]=='IIA'].head(3)
plt.bar(dd[1],dd[7])
plt.xlabel('Name of institute')
plt.ylabel('Average salary')
plt.show()

dd=d[d[3]=='IIB'].head(3)
plt.bar(dd[1],dd[7])
plt.xlabel('Name of institute')
plt.ylabel('Average salary')
plt.show()
