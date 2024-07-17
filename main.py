import pandas as pd
from pandas._libs.algos import diff_2d
from pandas.core.interchange.dataframe_protocol import Column

df = pd.read_csv("titanic.csv")

#How to Sort Data by Multiple Columns
print(df.sort_values(["Pclass", "Sex"]).head(100))

#How to Drop a Column in Pandas DataFrame
e = df.drop(columns=["Parch", "Ticket"])
print(e)

#How to Remove Rows that have NaN in any Column
df.dropna()

print(df[["Survived", "Name"]])

#How to Convert DataFrame Data Types (from Float to Int)
df2.Age = df2.Age.astype(int)
df2