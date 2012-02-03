__author__ = 'jack'
from os.path import exists
from subprocess import call

G = {
    'A': {'B': 10, 'D': 4, 'F': 10},
    'B': {'E': 5, 'J': 10, 'I': 17},
    'C': {'A': 4, 'D': 10, 'E': 16},
    'D': {'F': 12, 'G': 21},
    'E': {'G': 4},
    'F': {'H': 3},
    'G': {'J': 3},
    'H': {'G': 3, 'J': 5},
    'I': {},
    'J': {'I': 8},
    }

def printInGraphViz(G):
    dotContents = '';
    for v, pointsTo  in G.items():
       for u, weight in pointsTo.items():
           dotContents += v + ' -> ' + u + ' [label=' + str(weight) + '];'

    return dotContents

dotFile = 'dotTemp.dot'
f= open(dotFile, 'w')
f.write('digraph G {' +  printInGraphViz(G) + '}')
f.close()
output_file = 'graph.png'
if exists(output_file):
    call(['rm', output_file])
call(['dot', '-Tpng', dotFile, '-o' + output_file])

