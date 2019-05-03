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
team = "TEAM"
blue = "Blue"
red = "Red"

df_top_jungler_r = df_top_jungler.loc[df[team] == red]
df_top_jungler_b = df_top_jungler.loc[df[team] == blue]

df_mid_jungler_r = df_mid_jungler.loc[df[team] == red]
df_mid_jungler_b = df_mid_jungler.loc[df[team] == blue]

df_support_jungler_r = df_support_jungler.loc[df[team] == red]
df_support_jungler_b = df_support_jungler.loc[df[team] == blue]

df_support_ad_carry_r = df_support_ad_carry.loc[df[team] == red]
df_support_ad_carry_b = df_support_ad_carry.loc[df[team] == blue]

victory_column = "VICTORY"

dfToList_t_j_r = df_top_jungler_r[victory_column].tolist()
dfToList_t_j_b = df_top_jungler_b[victory_column].tolist()

dfToList_m_j_r = df_mid_jungler_r[victory_column].tolist()
dfToList_m_j_b = df_mid_jungler_b[victory_column].tolist()

dfToList_s_j_r = df_support_jungler_r[victory_column].tolist()
dfToList_s_j_b = df_support_jungler_b[victory_column].tolist()

dfToList_ad_s_r = df_support_ad_carry_r[victory_column].tolist()
dfToList_ad_s_b = df_support_ad_carry_b[victory_column].tolist()

f = 'vitorias_absolutas_das_duplas'

mathBoxPlot(dfToList_t_j_r,dfToList_t_j_b, 'top_jungler_red_chart',
            'Top/jungle', folder=f)

mathBoxPlot(dfToList_m_j_r,dfToList_m_j_b, 'mid_jungler_red_chart',
            'Mid/jungle', folder=f)

mathBoxPlot(dfToList_s_j_r,dfToList_s_j_b, 'support_jungler_red_chart',
            'Support/jungle', folder=f)

mathBoxPlot(dfToList_ad_s_r,dfToList_ad_s_b, 'ad_carry_support_red_chart',
            'Adc carry/support', folder=f)

