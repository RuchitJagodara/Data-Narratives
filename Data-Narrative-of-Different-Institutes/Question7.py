# More No. of applications must be arrived there where fees must be less or student faculty ratio must be less or where the average sat or act score is considered to be high.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data=pd.read_csv('http://lib.stat.cmu.edu/datasets/colleges/usnews.data',names=list(range(35)))

data=data[data[31]!='*']
data=data[data[14]!='*']
data=data[data[26]!='*']


data[31]=pd.to_numeric(data[31])
data[14]=pd.to_numeric(data[14])
data[26]=pd.to_numeric(data[26])


# plt.scatter(data[14],data[31])
# plt.xlabel('Total number of application')
# plt.ylabel('Student/faculty ratio')
# plt.show()

# plt.scatter(data[14],data[26])
# plt.xlabel('Total number of application')
# plt.ylabel('Additional fees')
# plt.show()

print(np.corrcoef(data[14],data[31]))
print(np.corrcoef(data[14],data[26]))
