from miner import Miner

class ChampCompWinRate(Miner):

  def __init__(self):
    self.df = self.pd.read_excel("./datasets/champ_comp.xlsx")

  def process_chain(self):
    self.__generateGlobalTreasures()

  def __getByYear(self, *args):
    return self.df[self.df.ano == args[0]]

  def __getBySide(self, *args):
    return self.df[self.df.time == args[0]]

  def after_process(self):
    self.__generateBestREDCompsBarChart()

  #   PROCESSORS
  def __generateGlobalTreasures(self):
    # created a champ comp identifier
    self.df['champComp'] = self.df.apply(lambda row: row['champ1'] + '/' + row['champ2'], axis=1)

    # Datasets Sorted by Years
    for year in [2015, 2016, 2017]:
      dfByYear = self.__getByYear(year)
      setattr(self, 'y' + str(year) + '_global', dfByYear)
      dfByYear.to_csv('./treasures/champ_comp/global_' + str(year) + '_champ_comp_list.csv')


    for side in ['RED', 'BLUE']:
      dfBySide = self.__getBySide(side)
      setattr(self, str(side) + '_global', dfBySide)
      dfBySide.to_csv('./treasures/champ_comp/global_' + str(side) + '_champ_comp_list.csv')


  def __generateBestREDCompsBarChart(self):
    universe = self.y2016_global
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


