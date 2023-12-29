# What is the probability that a person who has to play less round to win the match has less unforced error than the average of persons who has to play more rounds to win the match
import numpy as np
import pandas as pd



data=pd.read_csv("AusOpen-men-2013.csv")
data['ST4.2']=data['ST4.2'].astype(str)
d=data[data['ST4.2']==data['ST4.2'][0]]
c=data[data['ST4.2']!=data['ST4.2'][0]]

c1=c[c['Result']==0]
avg1=np.mean(c1['UFE.2'])

c2=c[c['Result']==1]
avg2=np.mean(c2['UFE.1'])

avg=(avg1+avg2)/2

d1=d[d['Result']==0]
number1=len(d1[d1['UFE.2']<avg])

d2=d[d['Result']==1]
number2=len(d2[d2['UFE.1']<avg])

final_number=number1+number2

print("Desired probability is : ",(final_number)/(len(d)))
print("Average unforced error is : ",avg )
