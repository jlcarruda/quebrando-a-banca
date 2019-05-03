import matplotlib.pyplot as plt
import numpy as np
import os
import errno


def mathBoxPlot(listValues,listValues2, titleFig="Default", titleChart="simple", path='box_chart_save_fig/', folder='', typeData='Quantidade', dataName="Vitorias",color1="red",color2="blue"):
    blue_diamond = dict(markerfacecolor=color2, marker='D')
    red_diamond = dict(markerfacecolor=color1, marker='D')
    
    dataRed = np.array([listValues,listValues,listValues2,listValues2])
    fig, axs = plt.subplots()
    fig.canvas.set_window_title(titleFig)

    bp = axs.boxplot(dataRed,patch_artist=True)
    bp['fliers'][1].set_data([0,0])
    bp['fliers'][3].set_data([0,0])
    axs.set_title(titleChart)
    axs.set_ylabel(typeData+' de '+ dataName)
    colors = [color1,color1,color2,color2]
    colors1 = [color1,color2]


    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    for median in bp['medians']:
        median.set(color='black', linewidth=2)
    n=0
    print(bp)
    for flier in bp['fliers']:
        flier.set(markerfacecolor=colors[n])
        n+=1
        



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
