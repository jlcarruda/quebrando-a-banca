#!/usr/bin/python
# -*- coding: utf-8 -*-
from miner import Miner

class ChampCompWinRate(Miner):

  # Ideias para geraçao de dados
  # - Comps que mais ganharam nos anos
  # - Comps que mais ganharam nos respectivos lados

  def __init__(self):
    self.df = self.pd.read_excel("./datasets/champ_comp.xlsx")
    self.identifier = 'champ_comp'

  def process_chain(self):
    self.__generateGlobalTreasures()
    self.matchCountByYear = {}


  def __getByYear(self, *args):
    return self.df[self.df.ano == args[0]]

  def __getBySide(self, *args):
    return self.df[self.df.time == args[0]]

  def __generateGlobalCSV(self, df, id, set_attr = False):
    if set_attr:
      setattr(self, 'att_' + str(id) + '_global', df)
    df.to_csv('./treasures/champ_comp/global_' + str(id) + '_' + self.identifier + '_list.csv')

  def __generateGlobalTreasures(self):
    # created a champ comp identifier
    self.df['champComp'] = self.df.apply(lambda row: row['champ1'] + '/' + row['champ2'], axis=1)
    self.dfByYear = map(lambda x: self.__generateGlobalCSV(self.__getByYear(x), x, True), [2015, 2016, 2017])
    self.dfBySide = map(lambda x: self.__generateGlobalCSV(self.__getBySide(x), x, True), ['RED', 'BLUE'])

  def __generateBestREDCompsBarChart(self):
    universe = self.att_2016_global
    data = universe.head(10)
    data_values = data.values
    aux = []

    for k in data_values:
      group = {}
      group[2015] = universe[universe.champComp == k[-1]][universe.ano == 2016].values

      aux.append(group)

    # get the same pair for each year
    print aux[0]
    return
    spacing = self.np.arange(len(data))

    tick_labels = [k[-1] for k in data_values]
    fig, ax1 = self.plt.subplots()

    rects = ax1.barh(spacing, 3, align='center', tick_label=tick_labels)
    ax1.set_title("(2015-2017) - Melhores Duplas do Lado Vermelho")

    self.plt.show()


