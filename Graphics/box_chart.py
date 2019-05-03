import matplotlib.pyplot as plt
import numpy as np
import os
import errno


def mathBoxPlot(listValues,listValues2, titleFig="Default", titleChart="simple", path='box_chart_save_fig/', folder='', typeData='Quantidade', dataName="Vitorias",color1="red",color2="blue"):
    blue_diamond = dict(markerfacecolor=color2, marker='D')
    red_diamond = dict(markerfacecolor=color1, marker='D')
    dataRed = np.array([listValues,listValues2])
    dataBlue = np.array([listValues,listValues2])
    ind = np.arange(2)
    fig, axs = plt.subplots(1,2)
    fig.canvas.set_window_title(titleFig)
    bp = axs[0].boxplot(dataRed,patch_artist=True)
    bp1 = axs[1].boxplot(dataBlue,0, '',patch_artist=True)
    axs[0].set_title(titleChart)
    axs[0].set_ylabel(typeData+' de '+ dataName)
    axs[1].set_title(titleChart+ ' sem outliers')
    axs[1].set_ylabel(typeData+' de '+ dataName)
    colors = [color1,color2]
    fig.text(0.63, 0.016, 'Team Red', color='black', backgroundcolor='red',
         weight='roman', size='medium')
    fig.text(0.823, 0.016, 'Team Blue', color='black',backgroundcolor='blue',
             weight='roman',size='medium')
    fig.text(0.125, 0.016, 'Team Red', color='black', backgroundcolor='red',
         weight='roman', size='medium')
    fig.text(0.320, 0.016, 'Team Blue', color='black',backgroundcolor='blue',
             weight='roman',size='medium')



    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    for median in bp['medians']:
        median.set(color='black', linewidth=2)
    n=0
    for flier in bp['fliers']:
        flier.set(markerfacecolor=colors[n])
        print(flier.get_data())
        n+=1
    for patch, color in zip(bp1['boxes'], colors):
        patch.set_facecolor(color)

    for median in bp1['medians']:
        median.set(color='black', linewidth=2)
    n=0
    for flier in bp1['fliers']:
        flier.set(markerfacecolor=colors[n])
        print(flier.get_data())
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
