import pandas as pd

df = pd.read_csv('tweets-gempa-cianjur.csv');
df2 = pd.read_csv('tweets-gempa-cianjur2.csv');
df3 = pd.read_csv('tweets-gempa-cianjur3.csv');
df4 = pd.read_csv('tweets-gempa-cianjur4.csv');

data = [df, df2, df3, df4];

df_final = pd.concat(data, axis=0);
df_final = df_final.reset_index(drop=True)
df_final.to_csv('dataset-final.csv')
# print(df3)