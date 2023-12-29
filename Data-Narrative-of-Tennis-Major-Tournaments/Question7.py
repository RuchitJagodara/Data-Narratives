# 	Winner points of a player should be more if opposite player does more unforced errors.

import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('Wimbledon-men-2013.csv')

plt.scatter(data['UFE.1'],data['WNR.2'],c='brown')
plt.scatter(data['UFE.2'],data['WNR.1'],c='brown')
plt.xlabel('Unforced error')
plt.ylabel("Winner points lost by the player")
plt.show()
