import pandas as pd
#Textbook Website: http://python-textbook.pythonhumanities.com/02_pandas/02_02_02_finding_data.html#how-to-find-specific-information-in-the-dataset-with-df-loc

df = pd.read_csv("titanic.csv")

#How to Find Column Data
df.columns
cols = df.columns.tolist()

#How to Find Specific Information in the Dataset with df.loc
#In other words, we are seeking to find those who did not survive.
(df.loc[(df["Sex"] == "female") & (df["Pclass"] == 1) & (df["Survived"] == 0)])

#Total number of passengers that are identified as female, but not in first class, and then find the number of those who did not survive

(df.loc[(df["Sex"] == "female") & (df["Pclass"] > 1) & (df["Survived"] == 0)])

#How to Query with “OR” (|) on a DataFrame
print(df.loc[(df["Pclass"] == 1) | (df["Pclass"] == 2)])
