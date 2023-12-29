


#  REJECTION RATIO MAY BE DEPENDS ON THE VALUE OF INSTITUTE LIKE WHERE ONLY SCHOLAR STUDENTS ARE GOING AND WHERE MORE NUMBER OF APPLICATIONAS ARE COMING

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data=pd.read_csv('http://lib.stat.cmu.edu/datasets/colleges/usnews.data',names=list(range(35)))

data=data[data[17]!='*']
data=data[data[14]!='*']
data=data[data[15]!='*']
data=data[data[7]!='*']
data=data[data[6]!='*']     


data[17]=pd.to_numeric(data[17])
data[14]=pd.to_numeric(data[14])
data[15]=pd.to_numeric(data[15])
data[7]=pd.to_numeric(data[7])
data[6]=pd.to_numeric(data[6])


data[35]=data[14]-data[15]
d=data[35]/data[14]

plt.scatter(data[14],d)
plt.xlabel('Total number of application received')
plt.ylabel('Rejection ratio')
plt.show()

plt.scatter(data[17],d)
plt.xlabel('percentage new students from top 10 % of H.S. classes')
plt.ylabel('Rejection ratio')
plt.show()


plt.scatter(data[7],d)
plt.xlabel('Average ACT score')
plt.ylabel('Rejection ratio')
plt.show()

plt.scatter(data[6],d)
plt.xlabel('Average SAT score')
plt.ylabel('Rejection ratio')
plt.show()
