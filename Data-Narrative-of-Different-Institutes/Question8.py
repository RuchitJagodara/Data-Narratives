# Institutes where graduation rate is low should get less admission requests


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('http://lib.stat.cmu.edu/datasets/colleges/usnews.data',names=list(range(35)))

data=data[data[34]!='*']
data=data[data[14]!='*']


data[34]=pd.to_numeric(data[34])
data[14]=pd.to_numeric(data[14])

plt.scatter(data[34],data[14])
plt.xlabel('Graduation rate')
plt.ylabel('Total number of applications received')
plt.show()

print(np.corrcoef(data[34],data[14]))
