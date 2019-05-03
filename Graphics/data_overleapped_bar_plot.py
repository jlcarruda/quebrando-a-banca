import pandas as pd
import json
from overleapped_bar import overleapped_bar_plot
from pylab import *


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

# print(df_top_jungler.head(5))
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
defeat_column = "DEFEAT"

dfToList_t_j_r = df_top_jungler_r[victory_column].tolist()
dfToList_t_j_b = df_top_jungler_b[victory_column].tolist()

dfToList_m_j_r = df_mid_jungler_r[victory_column].tolist()
dfToList_m_j_b = df_mid_jungler_b[victory_column].tolist()

dfToList_s_j_r = df_support_jungler_r[victory_column].tolist()
dfToList_s_j_b = df_support_jungler_b[victory_column].tolist()

dfToList_ad_s_r = df_support_ad_carry_r[victory_column].tolist()
dfToList_ad_s_b = df_support_ad_carry_b[victory_column].tolist()

# r = boxplot(dfToList_t_j_r)
# top_points = r["fliers"][0].get_data()[1]
listDf = [dfToList_t_j_r, dfToList_t_j_b, dfToList_m_j_r, dfToList_m_j_b,
          dfToList_s_j_r, dfToList_s_j_b, dfToList_ad_s_r, dfToList_ad_s_b]
outlierslist = list([boxplot(x)["fliers"][0].get_data()[1] for x in listDf])
otl = outlierslist


def m(x):
    l = list(reversed(sorted(x)))
    return l[:4]


df_top_jungler_r = df_top_jungler.loc[df[victory_column].isin(m(otl[0]))]
df_top_jungler_b = df_top_jungler.loc[df[victory_column].isin(m(otl[1]))]

df_mid_jungler_r = df_mid_jungler.loc[df[victory_column].isin(m(otl[2]))]
df_mid_jungler_b = df_mid_jungler.loc[df[victory_column].isin(m(otl[3]))]

df_support_jungler_r = df_support_jungler.loc[df[victory_column].isin(
    m(otl[4]))]
df_support_jungler_b = df_support_jungler.loc[df[victory_column].isin(
    m(otl[5]))]

df_support_ad_carry_r = df_support_ad_carry.loc[df[victory_column].isin(
    m(otl[6]))]
df_support_ad_carry_b = df_support_ad_carry.loc[df[victory_column].isin(
    m(otl[7]))]

dfOutList = [df_top_jungler_r, df_top_jungler_b,
             df_mid_jungler_r, df_mid_jungler_b,
             df_support_jungler_r, df_mid_jungler_b,
             df_support_ad_carry_r, df_support_ad_carry_b]
c1 = 'CHAMP1'

c2 = 'CHAMP2'
response = []

for df in dfOutList:
    list_c1 = list(df[c1])
    list_c2 = list(df[c2])
    outliers = list(df[victory_column])
    defeats = list(df[defeat_column])
    d = {}
    for x in range(len(list_c1)):
        d[list_c1[x]+'/'+list_c2[x]] = (outliers[x], defeats[x])
    response.append(d)
f = 'totais_partidas_vitorias_derrotas_duplas'
tf = []
t_j = [top, jungler]
m_J = [mid, jungler]
s_J = [sup, jungler]
ad_s = [ad_carry, sup]
gNames = ['-'.join(t_j)+' red', '-'.join(t_j)+' blue',
          '-'.join(m_J)+' red', '-'.join(m_J)+' blue',
          '-'.join(s_J)+' red', '-'.join(s_J)+' blue',
          '-'.join(ad_s)+' red', '-'.join(ad_s)+' blue']


for s in range(len(response)):
    r = response[s]
    rnames = r.keys()
    rv = []
    rd = []
    for n in rnames:
        t = r[n]
        rv.append(t[0])
        rd.append(t[1])
    overleapped_bar_plot(rv, rd, rnames, titleFig=gNames[s],
                         titleChart=" "+gNames[s], folder=f)
