# net points type na point ni win thavama fado 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv("FrenchOpen-women-2013.csv")

plt.scatter(data["NPW.1"],data['NPA.1'],c='red')
plt.scatter(data["NPW.2"],data["NPA.2"],c="red")
plt.plot(range(50),range(50),c='green')
plt.xlabel("Net points attended")
plt.ylabel("Total net points won")
plt.show()

plt.scatter(data["NPW.1"],data['TPW.1'],c="green")
plt.scatter(data["NPW.2"],data['TPW.2'],c="green")
plt.xlabel("Net points attended")
plt.ylabel("Total points won")
plt.show()

print(np.corrcoef(data['NPW.1'],data['NPA.1']))
print(np.corrcoef(data['NPW.2'],data['NPA.2']))
