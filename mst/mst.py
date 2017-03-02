# Minimum spanning tree (MST) algorithms
#
# Long Le
# University of Illinois
#

import numpy as np
import matplotlib.pyplot as plt

class Node:
    def __init__(self,x):
        self.val = x
        self.edge = {}

def Prim(nodes):
    return

def Kruskal(nodes):
    return

def visualize(nodes,locMap)
    plt.figure()
    for node in nodes:
        loc = locMap[node]
        plt.scatter(loc[0],loc[1],lw=32)
        plt.annotate(str(node.val),xy=loc,xytext=(loc[0]+.1,loc[1]+.1),fontsize=15)
        for ngb in node.ngbs:
            locNgb = locMap[ngb]
            plt.plot([loc[0],locNgb[0]],[loc[1],locNgb[1]])

    axes = plt.axes()
    axes.axison=False
    plt.show()
    return
