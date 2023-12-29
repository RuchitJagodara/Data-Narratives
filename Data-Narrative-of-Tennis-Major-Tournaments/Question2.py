# Is a good first sereve is enough to build a good score? 



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('AusOpen-women-2013.csv')

plt.bar(data['FSP.1'],data['FSW.1'])
plt.xlabel('First serve percent for player 1')
plt.ylabel("First serve won by player 1")
plt.show()

plt.bar(data['FSP.2'],data['FSW.2'])
plt.xlabel('First serve percent for player 2')
plt.ylabel("First serve won by player 2")
plt.show()


plt.scatter(data["FSW.1"], data["TPW.1"], c='orange')
plt.xlabel("First serve won by player 1")
plt.ylabel('Total points made by player 1')
z = np.polyfit(data["FSW.1"], data["TPW.1"], 1)
p = np.poly1d(z)
plt.plot(data["FSW.1"], p(data["FSW.1"]), "r--")
plt.show()

# Plot graph 4 with regression line
plt.scatter(data["FSW.2"], data["TPW.2"], c='green')
plt.xlabel("First serve won by player 2")
plt.ylabel('Total points made by player 2')
z = np.polyfit(data["FSW.2"], data["TPW.2"], 1)
p = np.poly1d(z)
plt.plot(data["FSW.2"], p(data["FSW.2"]), "r--")
plt.show()



print("Average percentage score of first serve win in total point made by player 1 : ",100*np.mean(data["FSW.1"]/data["TPW.1"]),"%")
print("Average percentage score of first serve win in total point made by player 2 : ",100*np.mean(data["FSW.2"]/data["TPW.2"]),"%")
