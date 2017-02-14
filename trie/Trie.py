# Trie Node class
#
# Long Le
# University of Illinois
#

import numpy as np
import matplotlib.pyplot as plt
import os,sys
sys.path.append(os.path.expanduser('~')+'/randProbs/graphSearch')
from GraphNode import add_arrow

class TrieNode:
    def __init__(self,x):
        self.val = x
        self.child = None
        self.next = None

def buildTrie(words):
    root = TrieNode(-1) # dummy node

    for word in words:
        node = root
        for i in range(len(word)):
            if node.child == None:
                # move node vertically
                node.child = TrieNode(word[:i+1])
                node = node.child
            else:
                node = node.child
                # move node horizontally
                while node.val[-1] != word[i]:
                    if node.next == None:
                        node.next = TrieNode(word[:i+1])
                        node = node.next
                        break
                    node = node.next
            #print('node.val = %s' % node.val)

    # remove dummy node
    node = root
    root = root.child
    del node

    return root

def allWords(root,plot=False):
    # get all words from root
    # using preorder-DFS
    buf = []

    locMap = {}
    locMap[root] = (0,0)
    parentMap = {}
    parentMap[root] = None

    S = []
    S.append(root)
    while len(S) > 0:
        node = S.pop()
        #print('node.val = %s' % node.val)
        
        if node.child == None:
            buf.append(node.val)

        if node.next != None:
            height = 1-locMap[node][1]
            locMap[node.next] = tuple(np.array(locMap[node])+np.array((1/height,0)))
            parentMap[node.next] = node
            #print('height = %s' % height)
            #print('node.next.val,loc = %s,%s' % (node.next.val,locMap[node.next]))

            S.append(node.next)
        if node.child != None:
            locMap[node.child] = tuple(np.array(locMap[node])+np.array((0,-1)))
            parentMap[node.child] = node

            S.append(node.child)

    if plot:
        plt.figure(figsize=(12, 8), dpi= 80, facecolor='w', edgecolor='k')
        for node,loc in locMap.items():
            #print('node.val,loc = %s,%s' % (node.val,loc))
            plt.annotate(str(node.val),xy=loc,size=18)
            plt.scatter(loc[0],loc[1],lw=32)
            if parentMap[node] in locMap:
                locParent = locMap[parentMap[node]]
                #plt.plot([locParent[0],loc[0]],[locParent[1],loc[1]],marker='o',markersize=18)
                add_arrow(plt.plot([locParent[0],loc[0]],[locParent[1],loc[1]])[0])
        plt.show()
    
    return buf

def autocomplete(root,word):
    prefix = []
    node = root
    for c in word:
        # find vertically
        if node.val == c:
            node = node.child
        else:
            # find horizontally
            tmp = node
            while tmp!= None:
                if tmp.val == c:
                    node = tmp
                    break
                tmp = tmp.next

            # form the result
            rv = []
            for postfix in allWords(node):
                rv.append(word+postfix[1:])
            return rv

    return word