import matplotlib.pyplot as plt
import numpy as np


def barChart(listNameGroups, list1, list2):
    N = len(listNameGroups)
    list1Values = tuple(list1)
    list1Std = tuple([1]*N)

    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars

    fig = plt.figure()
    ax = fig.add_subplot(111)
    rects1 = ax.bar(ind, list1Values, width, color='royalblue', yerr=list1Std)

    list2Values = tuple(list2)
    list2Std = tuple([1]*N)
    rects2 = ax.bar(ind+width, list2Values, width,
                    color='seagreen', yerr=list2Std)

    # add some
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(tuple(listNameGroups))

    ax.legend((rects1[0], rects2[0]), ('Red', 'Blue'))

    plt.show()
