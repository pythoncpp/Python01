import pandas as pd

df = pd.read_csv('/Volumes/Data/Sunbeam/2019/August/workshops/Python01/day_16/temp.csv')
print(df.describe())
print()
print(df.info())
print()
df['expected'] = df.high + 10
print(df.info())
df.to_csv('/Volumes/Data/Sunbeam/2019/August/workshops/Python01/day_16/temp_modified.csv')
