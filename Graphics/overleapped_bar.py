import matplotlib.pyplot as plt
import numpy as np
from pylab import *
import os
import errno


def overleapped_bar_plot(listValuesVictory, listValuesDefeat, listNames, titleFig="Default", titleChart="top jungle blue", path='box_chart_save_fig/', folder=''):
    # listValuesVictory = [int(x) for x in listValuesVictory]
    # listValuesDefeat = [int(x) for x in listValuesDefeat]
    print(listValuesVictory)
    print(listValuesDefeat)
    listNames = list(listNames)
    N = len(listNames)
    total = []
    for i in range(N):
        total.append(listValuesVictory[i] + listValuesDefeat[i])

    ind = np.arange(N)    # the x locations for the groups
    width = 0.35       # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, listValuesVictory, width)
    p2 = plt.bar(ind, listValuesDefeat, width, bottom=listValuesVictory)

    plt.ylabel('Total de partidas')
    plt.title('Total de vitorias e derrotas das duplas em outliers ' + titleChart)
    plt.xticks(ind, listNames)
    plt.yticks(np.arange(0, max(total), 10))
    plt.legend((p1[0], p2[0]), ('Vitorias', 'Derrotas'))

    try:
        os.makedirs(path+'/'+folder)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    if folder != '':
        path += (folder + '/')

    plt.savefig(path + titleFig + '.png')


overleapped_bar_plot([34, 42, 35, 36], [29, 33, 20, 29], [
                     'Trundle/Elise', 'Maokai/Khazix', 'Nautilus/Khazix', 'Nautilus/Graves'])
