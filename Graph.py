__author__ = 'jack'

G = {
    'A': {'B': 10, 'D': 4, 'F': 10},
    'B': {'E': 5, 'J': 10, 'I': 17},
    'C': {'A': 4, 'D': 10, 'E': 16},
    'D': {'F': 12, 'G': 21},
    'E': {'G': 4},
    'F': {'H': 3},
    'G': {'J': 3},
    'H': {'G': 3, 'J': 5},
    'I': {'F':4},
    'J': {'I': 8},
    }

def printInGraphViz(G):
    dotContents = '';
    for v, pointsTo  in G.items():
       for u, weight in pointsTo.items():
           dotContents += v + ' -> ' + u + ' [label=' + str(weight) + '];'

    print dotContents

printInGraphViz(G)