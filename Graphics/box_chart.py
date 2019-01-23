import matplotlib.pyplot as plt
import numpy as np
import os
import errno


def mathBoxPlot(listValues, titleFig="Default", titleChart="simple", path='box_chart_save_fig/', folder=''):

    data = np.array(listValues)

    fig, axs = plt.subplots(1, 2)
    fig.canvas.set_window_title(titleFig)

    axs[0].boxplot(data)
    axs[0].set_title(titleChart)

    axs[1].boxplot(data, 0, '')
    axs[1].set_title(titleChart + " don't show\noutlier points")

    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.05, top=0.9,
                        hspace=0.4, wspace=0.3)

    try:
        os.makedirs(path+'/'+folder)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    if folder != '':
        path += (folder + '/')

    plt.savefig(path + titleFig + '.png')
