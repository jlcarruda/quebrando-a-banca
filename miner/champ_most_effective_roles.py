#!/usr/bin/python
# -*- coding: utf-8 -*-
from miner import Miner
from champ_comp_win_rate import ChampCompWinRate

class ChampMostEffectiveRoles(Miner):

  # Gera grafico de papeis mais importantes

  def __init__(self, rootpath=".."):
    self.df_champions = self.pd.read_csv(rootpath + '/datasets/championFull.csv')
    self.champConf = ChampCompWinRate("..")
    self.identifier = 'most_effective_roles'

  def process_chain(self):
    self.champConf.process()
    self.transformations()

  def transformations(self):
    byYear = self.champConf.sortedByYear()
    map(lambda x: self.__mapFunc(x), byYear)

  def __mapFunc(self, yearDataframe):
    roleCounts = {}
    sortedDf = yearDataframe.sort_values(by="quantidade_vitorias", ascending=False) # Grafico de comps mais relevantes
    # ====> contagem de papeis
    map(lambda comp: self.__countRoles(comp, roleCounts), sortedDf.values)
    self.__generateGraph(roleCounts)

  def __countRoles(self, comp, counter):
    champ1 = comp[2]
    champ2 = comp[3]

    champ1_role = self.df_champions[self.df_champions.champion_Name == champ1]["tags"].values
    if len(champ1_role) > 0:
      keys_1 = eval(champ1_role[0])
      map(lambda key: self.__addKeys(key, counter), keys_1)

    champ2_role = self.df_champions[self.df_champions.champion_Name == champ2]["tags"].values
    if len(champ2_role) > 0:
      keys_2 = eval(champ2_role[0])
      map(lambda key: self.__addKeys(key, counter), keys_2)

  def __addKeys(self, key, counter):
    if key in counter:
      counter[key] += 1
    else:
      counter[key] = 1

  def __generateGraph(self, roleCounts):
    print ""

test = ChampMostEffectiveRoles()
test.process_chain()


