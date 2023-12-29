# 	Is there any effect of round on the ratio of break points won and break points created? Analyse the same thing but using the ratio of break points won and unforced error done by that player.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('USOpen-women-2013.csv')

ans=[]
ans2=[]
ttlround=np.unique(data['ROUND'])
for i in ttlround:
    d=data[data['ROUND']==i]
    ans2.append(np.mean((d['BPC.1']/d['UFE.1'])/2+np.mean(d['BPC.2']/d['UFE.2']))/2)
    ans.append(np.mean((d['BPW.1']/d['BPC.1'])/2+np.mean(d['BPW.2']/d['BPC.2']))/2)


plt.pie(ans,labels=ttlround)
plt.ylabel("The averag of ratios of Break point won and Break point created")
plt.show()

plt.bar(range(len(ttlround)),ans2)
plt.ylabel("the average of ratios between break point won and unforced error is ")
plt.xlabel("Round")
plt.show()
