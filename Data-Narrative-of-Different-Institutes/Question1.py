#  0   FICE (Federal ID number)
#  1   College name
#  2   State (postal code)
#  3   Type  (I, IIA, or IIB)
#  4   Average salary - full professors
#  5   Average salary - associate professors
#  6   Average salary - assistant professors
#  7   Average salary - all ranks
#  8   Average compensation - full professors
#  9   Average compensation - associate professors
#  10   Average compensation - assistant professors
#  11   Average compensation - all ranks
#  12   Number of full professors
#  13   Number of associate professors
#  14   Number of assistant professors
#  15   Number of instructors
#  16   Number of faculty - all ranks

# I.	Is there any trend that average salary and average compensation of professors are following with respect to total number of professors? Are these trends similar or not? Verify your answer. 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('http://lib.stat.cmu.edu/datasets/colleges/aaup.data',names=list(range(17)))

#average salary of full professors 
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

plt.scatter(x,y)
plt.xlabel('Total number of professors')
plt.ylabel('Average salary of professors')
plt.show()

plt.plot(x,y,'-r',scaley=range(200,900,100))
plt.xlabel('Total number of professors')
plt.ylabel('Average salary of professors')

plt.show()

plt.plot(x,z,'-r',scaley=range(200,900,100))
plt.xlabel('Total number of professors')
plt.ylabel('Average salary of professors')

plt.show()


#Average compensation of full professors

data=pd.read_csv('http://lib.stat.cmu.edu/datasets/colleges/aaup.data',names=list(range(17)))

data=data.sort_values(by=12,ascending=True)

data=data[data[8] != '*']
data=data[data[12] != '*']

x=pd.to_numeric(data[12])
x=x.drop(1)
y=pd.to_numeric(data[8])
y=y.drop(1)
zz=[]
i=0

while i<len(x)-1:
    zz+=[np.mean(y[i:i+12])]*12
    i+=12


plt.plot(x,y,'-r',scaley=range(200,900,100))
plt.xlabel('Total number of professors')
plt.ylabel('Average compensation of professors')

plt.show()

plt.plot(x,zz,'-r',scaley=range(200,900,100))
plt.xlabel('Total number of professors')
plt.ylabel('Average compensation of professors')

plt.show()

print(np.corrcoef(z,zz))
