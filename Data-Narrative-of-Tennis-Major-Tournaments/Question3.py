# Does the performance of the player increase as round increases?


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("FrenchOpen-men-2013.csv")
data["UFE.1"]=pd.to_numeric(data['UFE.1'])
data["UFE.2"]=pd.to_numeric(data['UFE.2'])
data["DBF.1"]=pd.to_numeric(data['DBF.1'])
data["DBF.2"]=pd.to_numeric(data['DBF.2'])

ttlround=np.unique(data["Round"])
ans1=[]
for i in ttlround:
    d=data[data['Round']==i]
    y=d['DBF.1']+d["UFE.1"]
    ans1.append(np.mean(y))

plt.pie(ans1,labels=ttlround)
plt.title("Player 1")
plt.ylabel("Average of total number points lost by unforced error \nand double fault error per round")
plt.show()

ans2=[]
for i in ttlround:
    d=data[data['Round']==i]
    y=d['DBF.2']+d["UFE.2"]
    ans2.append(np.mean(y))

plt.pie(ans2,labels=ttlround)
plt.title("Player 2")
plt.ylabel("Average of total number points lost by unforced error \nand double fault error per round")
plt.show()
