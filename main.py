import pandas as pd
df = pd.read_csv("titanic.csv")


#Let’s try and see a DataFrame that only has “male” in the Sex column. We can do that by using get_group(“male”).
#df = df.groupby("Sex").get_group("male")

#Let’s say, we want to just get all the people who are aged 20. We can do the same thing by grouping the dataset by “Age” and then getting the group of 20 year olds.
#df = df.groupby("Age").get_group(20)

#Quantitative Analysis with Count() and Sum().
#df = df.groupby("Sex").count()
#df = df.groupby("Sex").Fare.sum()

#Working with Multiple Groups.
#Let’s say though that we are interested in how these sums divide over Pclass.
#df = df.groupby(["Sex", "Pclass"]).Fare.sum()

#Groupings with Many Subsets.
df = pd.DataFrame(df.groupby(["Sex", "Age", "Pclass"]).Fare.sum())
print(df)