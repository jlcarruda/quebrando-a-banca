import pandas as pd


df_champ_duos = pd.read_csv("../treasures/champ_duos.csv")
df_champ_full = pd.read_csv("../treasures/championFull.csv")

df_tags_duos = df_champ_duos.merge(
    df_champ_full, left_on='CHAMP1', right_on='champion', how="inner").drop(['champion'], axis=1)

df_tags_duos.rename(
    columns={'tags': 'CHAMP1_TAG'}, inplace=True)

df_tags_duos = df_tags_duos.merge(
    df_champ_full, left_on='CHAMP2', right_on='champion', how="inner").drop(['champion'], axis=1)

df_tags_duos.rename(
    columns={'tags': 'CHAMP2_TAG'}, inplace=True)

df_tags_duos.drop(['CHAMP1', 'CHAMP2'], axis=1, inplace=True)

print(df_tags_duos.head())
