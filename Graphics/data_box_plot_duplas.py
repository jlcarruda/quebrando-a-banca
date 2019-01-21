import pandas as pd
import json
from box_chart import mathBoxPlot

# graficos de caixa para os valores absolutos da vitorias das duplas
# separados por lado vermelho e azul

df = pd.read_csv("../treasures/champ_duos.csv")


top = "TOP_LANER"
mid = "MID_LANER"
sup = "SUPPORT"
ad_carry = "AD_CARRY"
jungler = "JUNGLER"
champ1 = "CHAMP1_POSITION"
champ2 = "CHAMP2_POSITION"
year = "YEAR"
t_j = [top, jungler]
m_J = [mid, jungler]
s_J = [sup, jungler]
ad_s = [ad_carry, sup]
years = [2016, 2017]

df_top_jungler = df.loc[(df[champ1].isin(t_j)) & (
    df[champ2].isin(t_j)) & (df[year].isin(years))]
df_mid_jungler = df.loc[(df[champ1].isin(m_J)) & (
    df[champ2].isin(m_J)) & (df[year].isin(years))]
df_support_jungler = df.loc[(df[champ1].isin(s_J)) & (
    df[champ2].isin(s_J)) & (df[year].isin(years))]
df_support_ad_carry = df.loc[(df[champ1].isin(ad_s)) & (
    df[champ2].isin(ad_s)) & (df[year].isin(years))]

print(df_top_jungler.head(5))
# print(df_mid_jungler.head(5))
# print(df_support_jungler.head(5))
# print(df_support_ad_carry.head(5))
victory_column = 'VICTORY'

dfToList_t_j = df_top_jungler[victory_column].tolist()
dfToList_m_J = df_mid_jungler[victory_column].tolist()
dfToList_s_J = df_support_jungler[victory_column].tolist()
dfToList_ad_s = df_support_ad_carry[victory_column].tolist()

mathBoxPlot(dfToList_t_j, 'top_jungler_chart', 'top/jungle')
mathBoxPlot(dfToList_m_J, 'mid_jungler_chart', 'mid/jungle')
mathBoxPlot(dfToList_s_J, 'support_jungler_chart', 'support/jungle')
mathBoxPlot(dfToList_ad_s, 'ad_carry_support_chart', 'ad carry/ support')
