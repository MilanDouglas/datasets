import pandas as pd
import re

df = pd.read_csv("titanic.csv")
df = df[["Name"]]

#Finding Features within a String
#How many reverends were there on the Titanic?
names = df.Name.tolist()
revs = []
for name in names:
  if "Rev." in name:
    revs.append(name)
#print(revs)

#To find other data associated with "Rev."
df1 = df.loc[df["Name"].str.contains("Rev\.")]
print(df1)

#Finding Strings that Don’t Contain Feature "Rev.".
df2 = df.loc[~df["Name"].str.contains("Rev\.")]
print(df2)

#Using RegEx (Regular Expressions) with Pandas.
#If we were interested in finding any instance of “Rev.” or “Mr.”, we would have to write something like this WITHOUT-RegEx.
df3 = df.loc[(df["Name"].str.contains("Rev\.")) | (df["Name"].str.contains("Mr\."))]

#WITH - RegEx.
df4 = df.loc[df["Name"].str.contains("Rev\.|Mr\.", case=False,  regex=True)]
print(df4)

#To ensure that we grab both upper and lowercase forms of this sequence, let’s ignore the case by using the case keyword and setting it to False.(import re)
df5 = df.loc[df["Name"].str.contains("Rev.\|Mr\.", case=False, regex=True)]
print(df5)
