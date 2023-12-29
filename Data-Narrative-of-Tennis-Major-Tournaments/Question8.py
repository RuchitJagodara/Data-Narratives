# Ace and First serve win vacche trend

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("Wimbledon-women-2013.csv")

d=data.copy()
d['ACE.1']=d['ACE.2']
d["FSW.1"]=d['FSW.2']

frame=[data,d]

result=pd.concat(frame) 

result=result.sort_values(by="ACE.1")

plt.scatter(result['ACE.1'],result['FSW.1'])
plt.plot(range(15),range(15),c='red')
plt.xlabel('Ace points')
plt.ylabel('First serve win points')
plt.show()
