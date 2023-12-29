# IS THERE ANY INSTITUTE THAT IS PAYING MORE SALARY TO THEIR ASSOCIATE PROFESSOR OR ASSISTANT PROFESSOR THAN THE AVERAGE SALARY OF PROFESSORS OF OTHER INSTITUTE IF TOTAL NUMBER OF PROFESSOR AND ASSISTANT PROFESSOR OR ASSOCIATE PROFESSOR ARE ALMOST SAME? IS THERE ANY TREND THAT THESE GRAPHS ARE FOLLOWING AND IF YES, THEN AT WHAT EXTENT?

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('http://lib.stat.cmu.edu/datasets/colleges/aaup.data',names=list(range(17)))

data=data.sort_values(by=12,ascending=True)
data=data[data[4] != '*']
data=data[data[12] != '*']

x=pd.to_numeric(data[12])
x=x.drop(1)
y=pd.to_numeric(data[4])
y=y.drop(1)
z=[]
i=0

while i<len(x)-1:
    z+=[np.mean(y[i:i+12])]*12
    i+=12


#Average salary of associate professors

data=pd.read_csv('http://lib.stat.cmu.edu/datasets/colleges/aaup.data',names=list(range(17)))

data=data.sort_values(by=13,ascending=True)

data=data[data[8] != '*']
data=data[data[13] != '*']

xx=pd.to_numeric(data[13])
xx=xx.drop(1)
yy=pd.to_numeric(data[8])
yy=yy.drop(1)
zz=[]
i=0

while i<len(xx)-1:
    zz+=[np.mean(yy[i:i+12])]*12
    i+=12

plt.plot(x,y,'-b',scaley=range(200,900,100))
plt.plot(xx,yy,'-r',scaley=range(200,900,100))
plt.xlabel('Total number of professors/associate professors')
plt.ylabel('Average salary')
plt.legend(['Full professors', 'Associate professors'])
plt.show()


plt.plot(x,z,'-b',scaley=range(200,900,100))
plt.plot(xx,zz,'-r',scaley=range(200,900,100))
plt.xlabel('Total number of professors/associate professors')
plt.ylabel('Average salary')
plt.legend(['Full professors', 'Associate professors'])

plt.show()

print(np.corrcoef(z,zz))


#Average salary of assistant professors

data=pd.read_csv('http://lib.stat.cmu.edu/datasets/colleges/aaup.data',names=list(range(17)))

data=data.sort_values(by=14,ascending=True)

data=data[data[8] != '*']
data=data[data[14] != '*']

xx=pd.to_numeric(data[14])
xx=xx.drop(1)
yy=pd.to_numeric(data[8])
yy=yy.drop(1)
zz=[]
print(len(xx))
i=0

while i<len(xx)-1:
    zz+=[np.mean(yy[i:i+12])]*12
    i+=12

plt.plot(x,y,'-b',scaley=range(200,900,100))
plt.plot(xx,yy,'-r',scaley=range(200,900,100))
plt.xlabel('Total number of professors/Assistant professors')
plt.ylabel('Average salary')
plt.legend(['Full professors', 'Assistant professors'])

plt.show()


plt.plot(x,z,'-b',scaley=range(200,900,100))
plt.plot(xx,zz,'-r',scaley=range(200,900,100))
plt.xlabel('Total number of professors/assistant professors')
plt.ylabel('Average salary')
plt.legend(['Full professors', 'assistant professors'])

plt.show()

print(np.corrcoef(z,zz))

