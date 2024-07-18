import pandas as pd
df = pd.read_csv("titanic.csv")

#If we wanted to know how many male passengers were on the Titanic relative to female passengers. I could grab all the value counts and look at the numbers by calling .value_counts().
#df = df['Sex'].value_counts()

#We can take that initial code we see above and append two other methods to it .plot.bar().
df = df['Sex'].value_counts().plot.bar()
print(df)

