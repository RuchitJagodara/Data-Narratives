# What is the probability of winning a match after loosing 1st and 2nd set.
import pandas as pd

data=pd.read_csv('USOpen-men-2013.csv')

# First of all we need to find the matches in which first and second match are loosen by one player.

d=data[(data['ST1.1']>data['ST1.2'])^(data['ST2.1']<data['ST2.2'])]

total=len(d)

# Now check if a player wins the match after loosing the first and the second round of the match

c1=d[d['Result']==1]
ans1=len((c1[(c1['ST1.1']<c1['ST1.2'])])[(c1['ST2.1']<c1['ST2.2'])])

c2=d[d['Result']==0]
ans2=len((c2[c2['ST1.1']>c2['ST1.2']])[c2['ST2.1']>c2['ST2.2']])

ans=ans1+ans2

print((ans)/total)
