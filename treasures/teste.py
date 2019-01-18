from bar_plot import barChart
import pandas as pd


df = pd.read_csv("champ_duos.csv")

df = df.loc[df['YEAR'] != 2018]
df = df.loc[df['SEASON'] != 'Summer']
df = df.loc[df['YEAR'].isin([2017])]
# df = df.loc[df['CHAMP1'].isin(["AD_CARRY", "SUPPORT"])]
# df = df.loc[df['CHAMP2'].isin(["AD_CARRY", "SUPPORT"])]

df = df.sort_values('YEAR', ascending=False)
df = df.sort_values('VICTORY', ascending=False)
dfBLue = df.loc[df['TEAM'] == 'Blue']
dfRed = df.loc[df['TEAM'] == 'Red']

print(dfBLue.head(10))
print(dfRed.head(10))
dic = dfBLue.head(10).to_dict()
print(dic.keys())
